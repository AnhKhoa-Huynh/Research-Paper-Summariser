"""Optional local Streamlit browser for your research knowledge base.
Start: streamlit run dashboard.py
"""
import json
from collections import Counter
from pathlib import Path
import streamlit as st

ROOT=Path(__file__).resolve().parent
CATALOG=ROOT/'storage'/'catalog.json'
st.set_page_config(page_title='Research Radar',page_icon='🤖',layout='wide')
st.title('RESEARCH / RADAR')
st.caption('Robotics · HRI · Embodied AI · Multi-agent systems · Computer vision · ML · NLP')
records=json.loads(CATALOG.read_text(encoding='utf-8')) if CATALOG.exists() else []
if not records:
    st.info('No papers or news yet. Run `python -m radar.cli` from the project folder first.')
    st.stop()
types=['All','Papers','News']
with st.sidebar:
    st.header('Search and filters')
    search=st.text_input('Search titles, snapshots, authors, topics')
    kind=st.selectbox('Item type',types)
    topics=sorted({topic for r in records for topic in r.get('topics',[])})
    topic=st.selectbox('Research area',['All']+topics)
    source=st.selectbox('Source',['All']+sorted({r['source'] for r in records}))
    minscore=st.slider('Minimum relevance score',0.0,20.0,0.0,0.5)
    st.caption('Your archive stays in this project. No paid search service required.')

filtered=[]
for r in records:
    hay=' '.join([r.get('title',''),r.get('abstract',''),r.get('summary',''),r.get('source',''),
         ' '.join(r.get('authors',[])),' '.join(r.get('topics',[]))]).casefold()
    if search.casefold() not in hay:continue
    if kind=='Papers' and r['kind']!='paper':continue
    if kind=='News' and r['kind']!='news':continue
    if topic!='All' and topic not in r.get('topics',[]):continue
    if source!='All' and source!=r['source']:continue
    if float(r.get('score',0))<minscore:continue
    filtered.append(r)
filtered.sort(key=lambda x:(x.get('first_seen',''),x.get('score',0)),reverse=True)
c1,c2,c3=st.columns(3)
c1.metric('Saved records',len(records))
c2.metric('Papers',sum(r['kind']=='paper' for r in records))
c3.metric('Matching items',len(filtered))
with st.expander('Research themes in the archive',expanded=False):
    counts=Counter(t for r in records for t in r.get('topics',[]))
    st.bar_chart(dict(counts.most_common()))
st.divider()
for r in filtered[:300]:
    with st.container(border=True):
        category='📖 Paper' if r['kind']=='paper' else '📰 News'
        st.subheader(r['title'])
        st.caption(f'{category} · {r.get("source")} · Published {r.get("published", "?")[:10]} · '
                   f'First seen {r.get("first_seen", "?")} · Relevance {r.get("score", 0)}')
        if r.get('topics'):st.write(' · '.join(r['topics']))
        st.write(r.get('summary') or 'No excerpt supplied by source.')
        st.caption('Basis: '+(r.get('summary_mode') or 'unknown').replace('_',' '))
        link=r.get('url')
        if link:st.markdown(f'[Read the original source]({link})')
        note=ROOT/r.get('note_path','')
        if note.is_file():
            with st.expander('Full research note'):
                st.markdown(note.read_text(encoding='utf-8'))
if len(filtered)>300:st.caption('Showing first 300 results. Refine your filters to see more.')
