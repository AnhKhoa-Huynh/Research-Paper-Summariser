"""Always give original sources and indicate excerpt-level evidence."""
from datetime import datetime
from .common import markdown_escape,slug


def note_markdown(item):
    lines=[f'# {markdown_escape(item["title"])}','',
           f'- **Type:** {item["kind"]}',f'- **Source:** {markdown_escape(item.get("source"))}',
           f'- **Published:** {item.get("published") or "Unknown"}',
           f'- **First seen:** {item.get("first_seen")}',
           f'- **Topic matches:** {", ".join(item.get("topics",[])) or "General"}',
           f'- **Relevance score:** {item.get("score",0)}',
           f'- **Evidence:** {item.get("summary_mode", "unknown").replace("_", " ")}',
           f'- **Original link:** {item.get("url")}',
           f'- **PDF:** {item.get("pdf_url") or "Not supplied"}',
           '', '## Summary / source snapshot','',item.get('summary',''),
           '', '## Method / approach','',item.get('method',''),
           '', '## Reported contribution / result','',item.get('key_finding',''),
           '', '## Limitations / evidence gaps','',item.get('limitations',''),
           '', '## Why it might matter','',item.get('why_it_matters',''),
           '', '## Personal notes','', '- [ ] Read full source', '- [ ] Save to reading list',
           '', '> Research assistant output is not a fact-checked literature review. Verify claims in the original paper or reporting.', '']
    return '\n'.join(lines)


def digest_markdown(day,papers,news,stats):
    lines=[f'# Research Radar — {day}','',
           'Research papers, AI/robotics developments and useful reading leads.',
           '', '**Evidence note:** Paper summaries are based on abstracts, and news summaries on publisher RSS excerpts. '
           'They are not full-text reviews or independently verified breakthroughs.', '',
           f'**Discovered:** {stats.get("seen",0)} · **New:** {stats.get("new",0)} · '
           f'**Featured:** {len(papers)} papers + {len(news)} news · **Sources with errors:** {stats.get("source_errors",0)}',
           '', '## Papers worth reading', '']
    if not papers:lines.append('_No new highly ranked papers found in the search window._')
    for i,p in enumerate(papers,1):
        lines.extend([f'### {i}. [{markdown_escape(p["title"])}]({p["url"]})',
          f'**{markdown_escape(p["source"])}** · {p.get("published","?")[:10]} · '
          f'Score {p.get("score",0)} · {", ".join(p.get("topics",[])[:3])}',
          '',p.get('summary',''),'',
          f'**Method:** {p.get("method", "Not specified")}',
          f'**Claimed finding:** {p.get("key_finding", "Not specified")}',
          f'**Evidence gaps:** {p.get("limitations", "Not specified")}',
          f'**Relevance:** {p.get("why_it_matters", "")}',
          f'**Summary basis:** {p.get("summary_mode","").replace("_"," ")}', ''])
    lines.extend(['## Robotics and AI news', ''])
    if not news:lines.append('_No new relevant news found in the search window._')
    for i,n in enumerate(news,1):
        lines.extend([f'### {i}. [{markdown_escape(n["title"])}]({n["url"]})',
          f'**{markdown_escape(n["source"])}** · {n.get("published", "")[:10]} · Score {n.get("score",0)}',
          '',n.get('summary',''),'',
          '**Verification:** This is a source-reported development, not a validated performance claim.',''])
    lines.extend(['---','','_Generated automatically. Edit `config.yaml` to adjust topics; personal annotations belong in `storage/notes/`._',''])
    return '\n'.join(lines)


def telegram_text(day,papers,news):
    chunks=[f'🤖 Research Radar | {day}',f'📚 {len(papers)} papers · 📰 {len(news)} news', '']
    if papers:
        chunks.append('TOP PAPERS')
        for p in papers[:5]:chunks.append('• '+p['title'][:105]+'\n  '+p.get('url',''))
    if news:
        chunks.append('\nHEADLINES')
        for n in news[:4]:chunks.append('• '+n['title'][:100]+'\n  '+n.get('url',''))
    chunks.append('\nAbstract/RSS-based summaries and full notes saved to your repository.')
    text='\n'.join(chunks)
    return text[:3900]
