"""Idempotent daily orchestration. State is regular Git-versioned JSON and Markdown."""
import json
import logging
import os
from datetime import datetime,timedelta,timezone
from pathlib import Path
from zoneinfo import ZoneInfo

import requests
import yaml
from .analysis import deduplicate,score,summarize
from .common import canonical_key, slug, within_lookback, normalize_title
from .notify import telegram_send
from .render import digest_markdown,note_markdown,telegram_text
from .sources import fetch_arxiv,fetch_openalex,fetch_news

LOG=logging.getLogger(__name__)
UK=ZoneInfo('Europe/London')


def load_config(root):
    with (root/'config.yaml').open(encoding='utf-8') as f:return yaml.safe_load(f)


def load_archive(path):
    if not path.exists():return []
    with path.open(encoding='utf-8') as f:
        records=json.load(f)
        if not isinstance(records,list):raise ValueError('Catalog must be a list')
        return records


def write_text(path,content):
    path.parent.mkdir(parents=True,exist_ok=True)
    path.write_text(content,encoding='utf-8')


def run(root, now=None, records_override=None, send_notifications=True):
    root=Path(root).resolve()
    cfg=load_config(root)
    settings=cfg['settings']
    now=(now or datetime.now(timezone.utc)).astimezone(timezone.utc)
    day=now.astimezone(UK).date().isoformat()
    window=settings['lookback_days']
    session=requests.Session()
    errors=[]
    if records_override is not None:
        raw=records_override
    else:
        since=(now-timedelta(days=window)).date().isoformat()
        raw=(fetch_arxiv(session,cfg['arxiv_queries'],settings['arxiv_max_per_query'],settings['request_timeout_seconds'],errors=errors)+
             fetch_openalex(session,cfg['openalex_queries'],since,settings['openalex_max_per_query'],settings['request_timeout_seconds'],errors=errors)+
             fetch_news(session,cfg['rss_feeds'],settings['request_timeout_seconds'],errors=errors))
    candidates=deduplicate([i for i in raw if within_lookback(i.get('published'),now,window)])
    for p in candidates:
        p['score'],p['topics']=score(p,cfg['interests'])
    candidates=sorted(candidates,key=lambda x:(x['score'],x.get('published','')),reverse=True)
    archive_path=root/'storage'/'catalog.json'
    old=load_archive(archive_path)
    old_keys={x.get('key') or canonical_key(x) for x in old}
    old_titles={normalize_title(x['title']) for x in old}
    novel=[r for r in candidates if r['key'] not in old_keys and normalize_title(r['title']) not in old_titles]
    novel=[x for x in novel if x['score']>=settings['min_score']]
    # Maintain separate quotas so a high-volume preprint day cannot crowd out news.
    novel=([x for x in novel if x['kind']=='paper'][:settings['max_new_papers_saved']]
           +[x for x in novel if x['kind']=='news'][:settings['max_new_news_saved']])
    novel.sort(key=lambda x:(x['score'],x.get('published','')), reverse=True)
    paper_list=[r for r in novel if r['kind']=='paper']
    news_list=[r for r in novel if r['kind']=='news']
    featured=paper_list[:settings['max_papers_digest']]+news_list[:settings['max_news_digest']]
    featured_keys={x['key'] for x in featured}
    for record in novel:
        record['first_seen']=day
        if record['key'] in featured_keys:
            record.update(summarize(record,session=session))
        else:
            # Zero LLM calls for lower-ranked entries; still searchable and archived.
            from .analysis import extractive_snapshot
            record.update(extractive_snapshot(record))
        # Stable path based on canonical ID ensures retry safety.
        path=root/'storage'/'notes'/record['kind']/(slug(record['title'])+'-'+record['key'].split(':')[-1][:8]+'.md')
        record['note_path']=str(path.relative_to(root))
        write_text(path,note_markdown(record))
    # Write catalog before notification so no data is lost if sending fails.
    if novel:
        archive_path.parent.mkdir(parents=True,exist_ok=True)
        archive_path.write_text(json.dumps(old+novel,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
    papers=[p for p in novel if p['kind']=='paper'][:settings['max_papers_digest']]
    news=[n for n in novel if n['kind']=='news'][:settings['max_news_digest']]
    stats={'seen':len(raw),'new':len(novel),'source_errors':len(errors)}
    digest=digest_markdown(day,papers,news,stats)
    if errors:
        digest += "\n## Source availability warnings\n\n" + "\n".join("- Failed: " + e for e in errors) + "\n"
    digest_path=root/'storage'/'digests'/(day+'.md')
    # Avoid replacing a prior digest with an empty one on reruns. Reruns can add newly indexed items.
    if digest_path.exists() and not novel:
        LOG.info('Already processed: %s. Skipping duplicate digest and notification.',day)
        sent=False
    else:
        write_text(digest_path,digest)
        sent=bool(send_notifications and novel and telegram_send(telegram_text(day,papers,news),session))
    summary=f'### Research Radar {day}\n- Retrieved: {len(raw)}\n- Eligible: {len(candidates)}\n- New archived: {len(novel)}\n- Featured papers: {len(papers)}\n- News: {len(news)}\n- Feed/API failures: {len(errors)}\n- Telegram sent: {sent}\n'
    if os.getenv('GITHUB_STEP_SUMMARY'):
        with open(os.environ['GITHUB_STEP_SUMMARY'],'a',encoding='utf-8') as f:f.write(summary+'\n')
    return {'day':day,'retrieved':len(raw),'eligible':len(candidates),'new':len(novel),'papers':len(papers),'news':len(news),'telegram_sent':sent,'source_errors':errors,'digest_path':str(digest_path)}
