"""Weekly topic trend report from the versioned catalog; no LLM needed."""
import json
from collections import Counter
from datetime import date,timedelta
from pathlib import Path
from .common import markdown_escape

def generate(root, today=None):
    root=Path(root)
    now=today or date.today()
    data=json.loads((root/'storage'/'catalog.json').read_text(encoding='utf-8'))
    start=now-timedelta(days=7)
    prev=start-timedelta(days=7)
    current=[r for r in data if start.isoformat() <= r.get('first_seen','') < now.isoformat()]
    previous=[r for r in data if prev.isoformat() <= r.get('first_seen','') < start.isoformat()]
    t1=Counter(t for r in current for t in r.get('topics',[]))
    t0=Counter(t for r in previous for t in r.get('topics',[]))
    lines=[f'# Weekly Robotics & AI Research Radar — {now.isoformat()}','',
      f'Papers: {sum(r["kind"]=="paper" for r in current)} · News: {sum(r["kind"]=="news" for r in current)}',
      '', '## Topic movement (item counts; not a measure of scientific progress)', '']
    for name,n in t1.most_common():lines.append(f'- {name}: {n} (previous week: {t0.get(name,0)}, change: {n-t0.get(name,0):+d})')
    if not t1:lines.append('_Nothing new was archived this week._')
    lines.extend(['','## Papers to revisit',''])
    for r in sorted((x for x in current if x['kind']=='paper'),key=lambda x:x.get('score',0),reverse=True)[:8]:
        lines.append(f'- [{markdown_escape(r["title"])}]({r["url"]}) — relevance {r.get("score",0)}')
    lines.extend(['','## News to revisit',''])
    for r in sorted((x for x in current if x['kind']=='news'),key=lambda x:x.get('score',0),reverse=True)[:5]:
        lines.append(f'- [{markdown_escape(r["title"])}]({r["url"]})')
    path=root/'storage'/'weekly'/f'{now.isoformat()}.md'
    path.parent.mkdir(parents=True,exist_ok=True)
    path.write_text('\n'.join(lines)+'\n',encoding='utf-8')
    return str(path)

if __name__=='__main__':
    print(generate(Path(__file__).resolve().parents[1]))
