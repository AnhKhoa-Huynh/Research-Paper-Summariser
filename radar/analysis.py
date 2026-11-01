"""Topic ranking, honest extractive fallback, and optional grounded Gemini summaries."""
import json
import logging
import os
import re
import time
from difflib import SequenceMatcher

import requests
from .common import canonical_key, clean_text, normalize_title

LOG=logging.getLogger(__name__)


def score(record, interests):
    title=record.get('title','').casefold()
    abstract=record.get('abstract','').casefold()
    hits=[]
    total=0.0
    for group in interests:
        phrases=group.get('phrases',[])
        matched=[p for p in phrases if re.search(r'(?<!\w)'+re.escape(p.casefold())+r'(?!\w)', title+' '+abstract)]
        if matched:
            # Title is strongest signal, abstract helps discovery; prevent overly broad groups dominating.
            title_match=any(re.search(r'(?<!\w)'+re.escape(p.casefold())+r'(?!\w)',title) for p in matched)
            w=float(group['weight'])
            total += w*(1.0 if title_match else 0.35) + min(len(matched)-1,3)*0.25
            hits.append(group['name'])
    if record.get('kind')=='paper' and record.get('source')=='arXiv':
        if 'cs.RO' in record.get('categories',[]):total+=1.2
    if record.get('kind')=='news' and record.get('feed') in ['The Robot Report','IEEE Spectrum Robotics']:
        total+=0.8
    return round(total,2),hits


def duplicate(a,b):
    if canonical_key(a)==canonical_key(b):return True
    if a.get('kind')!=b.get('kind'):return False
    x,y=normalize_title(a.get('title')),normalize_title(b.get('title'))
    if len(x)<18 or len(y)<18:return False
    return SequenceMatcher(None,x,y).ratio() >= 0.93


def deduplicate(records):
    # Prefer descriptions and canonical first-party arXiv links when merging records.
    ordered=sorted(records,key=lambda r:(bool(r.get('abstract')),len(r.get('abstract',''))),reverse=True)
    results=[]
    for record in ordered:
        match=next((prior for prior in results if duplicate(prior,record)),None)
        if match:
            match.setdefault('other_sources',[]).append({'source':record.get('source'), 'url':record.get('url')})
        else:
            record=dict(record)
            record['key']=canonical_key(record)
            record['other_sources']=[]
            results.append(record)
    return results


def split_sentences(text):
    parts=re.split(r'(?<=[.!?])\s+(?=[A-Z\d])',clean_text(text))
    return [p.strip() for p in parts if p.strip()]


def extractive_snapshot(record):
    # Not an LLM summary: transparently label the excerpt, never synthesize results.
    abstract=clean_text(record.get('abstract',''))
    sent=split_sentences(abstract)
    snippet=' '.join(sent[:2])[:480].strip()
    if not snippet:
        snippet='No abstract/excerpt was supplied by this source; read the linked item.'
    return {
        'summary':snippet, 'method':'Not established from the available metadata.',
        'key_finding':'Not independently verified.',
        'limitations':'Full text has not been assessed.',
        'why_it_matters':'Matched your configured research topics; inspect the source for relevance.',
        'summary_mode':'source_excerpt' if abstract else 'title_only',
    }


def _parse_json_text(value):
    content=value.strip()
    if content.startswith('```'):
        content=re.sub(r'^```(?:json)?\s*|\s*```$', '', content,flags=re.I)
    obj=json.loads(content)
    if not isinstance(obj,dict):raise ValueError('non-object')
    names=['summary','method','key_finding','limitations','why_it_matters']
    if not all(isinstance(obj.get(n),str) for n in names):raise ValueError('missing required fields')
    return {k:clean_text(obj[k])[:800] for k in names}


def summarize(record, session=None):
    default=extractive_snapshot(record)
    key=os.environ.get('GEMINI_API_KEY','').strip()
    if not key or not record.get('abstract'):
        return default
    model=os.environ.get('GEMINI_MODEL','gemini-3.5-flash-lite')
    prompt=(
      'You are a critical research assistant. Use ONLY the source metadata. Be accurate, cautious and concise. '
      'Do not infer benchmarks, methods, results or limitations absent from the supplied excerpt. '
      'For papers, describe AUTHOR CLAIMS, not verified facts. For news, attribute claims to the publisher; do not call them breakthroughs unless supported. '
      'Return a JSON object with EXACTLY these short STRING fields: summary (2 sentences in your own words), '
      'method, key_finding, limitations, why_it_matters. Use "Not specified in source" where needed. '
      'Avoid direct quotations.\n'
      f'Item type: {record.get("kind")}\nTitle: {record.get("title")}\n'
      f'Source: {record.get("source")}\nDate: {record.get("published")}\n'
      f'Abstract or publisher-provided excerpt: {clean_text(record.get("abstract"))[:7500]}')
    payload={'contents':[{'parts':[{'text':prompt}]}],
          'generationConfig':{'temperature':0.15,'responseMimeType':'application/json','maxOutputTokens':750}}
    http=session or requests.Session()
    url=f'https://generativelanguage.googleapis.com/v1beta/models/{model}:generateContent'
    try:
        for attempt in range(2):
            resp=http.post(url,headers={'x-goog-api-key':key},json=payload,timeout=45)
            if resp.status_code==429 and attempt==0:
                time.sleep(3)
                continue
            resp.raise_for_status()
            data=resp.json()
            raw=''.join(part.get('text','') for cand in data.get('candidates',[])
                        for part in cand.get('content',{}).get('parts',[]))
            result=_parse_json_text(raw)
            result['summary_mode']='gemini_from_abstract' if record['kind']=='paper' else 'gemini_from_rss'
            return result
    except (requests.RequestException, ValueError, KeyError, TypeError) as exc:
        LOG.warning('Gemini unavailable for %s: %s',record.get('title','')[:55],type(exc).__name__)
    return default
