"""arXiv Atom, OpenAlex JSON and publisher/Google News RSS fetchers.

No API key is required. Individual source failures are reported but don't stop the run.
"""
import logging
import os
import time
from xml.etree import ElementTree as ET
from urllib.parse import urlencode
from .common import clean_text, clean_url

import requests

LOG = logging.getLogger(__name__)
ATOM = '{http://www.w3.org/2005/Atom}'
RSS_DC = '{http://purl.org/dc/elements/1.1/}'
UA = 'RoboticsResearchRadar/1.0 (personal academic RSS monitoring; noncommercial)'


def get(session, url, *, params=None, timeout=25, retries=2):
    for attempt in range(retries + 1):
        try:
            response = session.get(url, params=params, timeout=timeout, headers={'User-Agent': UA, 'Accept': 'application/atom+xml, application/rss+xml, application/json, */*'})
            if response.status_code in (429, 500, 502, 503, 504) and attempt < retries:
                time.sleep(2 * (2 ** attempt))
                continue
            response.raise_for_status()
            return response
        except requests.RequestException:
            if attempt >= retries:
                raise
            time.sleep(2 * (2 ** attempt))
    raise RuntimeError('Request failed')


def _xml_str(el, path):
    node = el.find(path)
    return clean_text(''.join(node.itertext())) if node is not None else ''


def fetch_arxiv(session, queries, max_per_query, timeout=25, sleep_s=3.1, errors=None):
    output = []
    for idx, query in enumerate(queries):
        if idx:
            time.sleep(sleep_s)  # arXiv etiquette: at least 3 seconds between API calls
        try:
            r = get(session, 'https://export.arxiv.org/api/query', params={
                'search_query': query, 'start': 0, 'max_results': max_per_query,
                'sortBy': 'submittedDate', 'sortOrder': 'descending'}, timeout=timeout)
            root = ET.fromstring(r.content)
            for entry in root.findall(f'{ATOM}entry'):
                url = _xml_str(entry, f'{ATOM}id')
                title = _xml_str(entry, f'{ATOM}title')
                if not title:
                    continue
                authors = [_xml_str(a, f'{ATOM}name') for a in entry.findall(f'{ATOM}author')]
                categories = [c.attrib.get('term', '') for c in entry.findall(f'{ATOM}category')]
                pdf = next((link.attrib.get('href', '') for link in entry.findall(f'{ATOM}link')
                            if link.attrib.get('title') == 'pdf' or link.attrib.get('type') == 'application/pdf'), '')
                output.append({'kind':'paper','source':'arXiv','title':title,
                    'abstract':_xml_str(entry, f'{ATOM}summary'), 'url':clean_url(url), 'pdf_url':pdf,
                    'doi':'', 'authors':authors[:12], 'published':_xml_str(entry, f'{ATOM}published'),
                    'categories':categories, 'peer_reviewed':False})
        except (requests.RequestException, ET.ParseError) as exc:
            LOG.warning('arXiv query %s failed: %s', query, exc)
            if errors is not None: errors.append('arXiv: '+query)
    return output


def reconstruct_abstract(inverted):
    if not inverted:
        return ''
    max_position = max((max(v, default=-1) for v in inverted.values()), default=-1)
    if max_position < 0 or max_position > 6000:
        return ''
    words = [''] * (max_position + 1)
    for word, positions in inverted.items():
        for pos in positions:
            words[pos] = word
    return clean_text(' '.join(words))


def fetch_openalex(session, queries, since_date, max_per_query, timeout=25, errors=None):
    output=[]
    key=os.environ.get('OPENALEX_API_KEY', '').strip()
    for q in queries:
        try:
            params={'search':q, 'filter':f'from_publication_date:{since_date}',
                'sort':'publication_date:desc', 'per_page':max_per_query,
                'select':'id,title,doi,publication_date,authorships,abstract_inverted_index,primary_location,open_access,type'}
            if key: params['api_key']=key
            r=get(session,'https://api.openalex.org/works',params=params,timeout=timeout).json()
            for entry in r.get('results',[]):
                title=clean_text(entry.get('title'))
                if not title:continue
                loc=entry.get('primary_location') or {}
                location_url=loc.get('landing_page_url') or (entry.get('doi') or entry.get('id') or '')
                output.append({'kind':'paper','source':'OpenAlex', 'title':title,
                    'abstract':reconstruct_abstract(entry.get('abstract_inverted_index')),
                    'url':clean_url(location_url),'pdf_url':(loc.get('pdf_url') or ''),
                    'doi':entry.get('doi') or '',
                    'authors':[x.get('author',{}).get('display_name','') for x in entry.get('authorships',[])][:12],
                    'published':entry.get('publication_date') or '', 'categories':[],
                    'peer_reviewed':None, 'publication_type':entry.get('type') or 'unknown'})
        except (requests.RequestException, ValueError, KeyError) as exc:
            LOG.warning('OpenAlex query %s failed: %s',q,exc)
            if errors is not None: errors.append('OpenAlex: '+q)
    return output


def _rss_item_text(item, tags):
    for tag in tags:
        v = _xml_str(item,tag)
        if v:return v
    return ''


def parse_rss(xml_bytes, source_name):
    root=ET.fromstring(xml_bytes)
    items=root.findall('.//item')
    output=[]
    for item in items:
        title=_rss_item_text(item,['title'])
        link=_rss_item_text(item,['link'])
        if not link or not title:continue
        published=_rss_item_text(item,['pubDate',f'{RSS_DC}date','published','date'])
        publisher=_rss_item_text(item,['source']) or source_name
        output.append({'kind':'news','source':publisher,'feed':source_name, 'title':title,
           'abstract':_rss_item_text(item,['description','summary']), 'url':clean_url(link),
           'authors':[], 'published':published, 'doi':'','pdf_url':'','categories':[]})
    return output


def fetch_news(session, feeds, timeout=25, errors=None):
    output=[]
    for feed in feeds:
        try:
            response=get(session,feed['url'],timeout=timeout)
            output.extend(parse_rss(response.content,feed['name']))
        except (requests.RequestException, ET.ParseError, KeyError) as exc:
            LOG.warning('News feed %s failed: %s',feed.get('name'),exc)
            if errors is not None: errors.append('RSS: '+str(feed.get('name')))
    return output
