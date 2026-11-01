import json
import tempfile
import unittest
from datetime import datetime,timezone,date
from pathlib import Path
from unittest.mock import patch
from radar.analysis import score,deduplicate,extractive_snapshot
from radar.common import canonical_key,within_lookback,clean_url
from radar.pipeline import run
from radar.sources import parse_rss,reconstruct_abstract,fetch_arxiv
from radar.weekly import generate

NOW=datetime(2026,10,31,8,0,tzinfo=timezone.utc)


def paper(title='Learning Contact-Rich Human-Robot Collaboration'):
    return {'kind':'paper','source':'arXiv','title':title,'abstract':'We introduce a robot learning method for human robot collaboration. We evaluate a benchmark.',
        'url':'https://arxiv.org/abs/2610.12345','pdf_url':'https://arxiv.org/pdf/2610.12345','authors':['A. Researcher'],
        'published':'2026-10-30T12:00:00Z','doi':'','categories':['cs.RO']}


def news(title='New robot designed for dexterous manipulation'):
    return {'kind':'news','source':'The Robot Report','feed':'The Robot Report','title':title,
       'abstract':'A company has announced a demonstration. The claims need verification.',
       'url':'https://example.com/robot','published':'2026-10-30T15:00:00Z','doi':'','categories':[]}


class RadarTests(unittest.TestCase):
    def test_duplicate_across_sources_title(self):
        p=paper(); other=dict(p,source='OpenAlex',url='https://other.example/paper')
        self.assertEqual(len(deduplicate([p,other])),1)

    def test_old_not_new(self):
        self.assertFalse(within_lookback('2026-01-02',NOW,3))
        self.assertTrue(within_lookback('2026-10-30T01:00:00Z',NOW,3))
        self.assertFalse(within_lookback(None,NOW,3))

    def test_rss_parse(self):
        raw=b'<rss><channel><item><title>Robot test</title><link>https://example.com/a</link><pubDate>Fri, 30 Oct 2026 11:00:00 GMT</pubDate><description>Robot news</description></item></channel></rss>'
        result=parse_rss(raw,'Some Feed')
        self.assertEqual(result[0]['kind'],'news');self.assertEqual(result[0]['title'],'Robot test')

    def test_openalex_abstract(self):
        self.assertEqual(reconstruct_abstract({'Robot':[0],'moves':[1],'well.':[2]}),'Robot moves well.')

    def test_arxiv_atom_parse(self):
        atom=b'''<feed xmlns="http://www.w3.org/2005/Atom"><entry><id>https://arxiv.org/abs/2610.12345</id><title>Robot manipulation</title><summary>We test a controller.</summary><published>2026-10-30T08:00:00Z</published><author><name>A. R.</name></author><category term="cs.RO"/><link title="pdf" href="https://arxiv.org/pdf/2610.12345"/></entry></feed>'''
        from unittest.mock import Mock
        response=Mock(content=atom)
        with patch('radar.sources.get',return_value=response):
            got=fetch_arxiv(None,['cat:cs.RO'],10)
        self.assertEqual(len(got),1);self.assertEqual(got[0]['authors'],['A. R.'])

    def test_excerpt_is_explicit(self):
        self.assertEqual(extractive_snapshot(paper())['summary_mode'],'source_excerpt')
        self.assertEqual(extractive_snapshot({**paper(),'abstract':''})['summary_mode'],'title_only')

    def test_relevance(self):
        cfg_path=Path(__file__).resolve().parents[1]/'config.yaml'
        import yaml
        config=yaml.safe_load(cfg_path.read_text(encoding='utf-8'))
        val,tags=score(paper(),config['interests'])
        self.assertGreater(val,4);self.assertTrue(any('Human' in t for t in tags))

    def test_notes_survive_reruns(self):
        import shutil
        source=Path(__file__).resolve().parents[1]
        with tempfile.TemporaryDirectory() as tmp:
            root=Path(tmp)
            shutil.copy(source/'config.yaml',root/'config.yaml')
            first=run(root,now=NOW,records_override=[paper(),news()],send_notifications=False)
            self.assertEqual(first['new'],2)
            self.assertTrue(Path(first['digest_path']).exists())
            self.assertEqual(len(json.loads((root/'storage/catalog.json').read_text(encoding='utf-8'))),2)
            note=next((root/'storage/notes/paper').glob('*.md'))
            note.write_text(note.read_text(encoding='utf-8')+'\nMy observation: useful.\n',encoding='utf-8')
            second=run(root,now=NOW,records_override=[paper(),news()],send_notifications=False)
            self.assertEqual(second['new'],0)
            self.assertIn('My observation: useful.',note.read_text(encoding='utf-8'))
            weekly=generate(root,today=date(2026,11,1))
            self.assertTrue(Path(weekly).exists())

    def test_url_tracking_removed(self):
        self.assertEqual(clean_url('https://example.org/a?utm_source=x&id=2'),'https://example.org/a?id=2')

if __name__=='__main__': unittest.main()

class MoreTests(unittest.TestCase):
    def test_malformed_rss_rejected(self):
        from xml.etree.ElementTree import ParseError
        with self.assertRaises(ParseError):parse_rss(b'<broken','Publisher')

    def test_gemini_json_parser_cautious(self):
        from radar.analysis import _parse_json_text
        sample=json.dumps({'summary':'Two sentences.','method':'Not specified in source',
                           'key_finding':'Author claims X','limitations':'Not specified in source',
                           'why_it_matters':'Relevant to HRI.'})
        self.assertEqual(_parse_json_text(sample)['method'],'Not specified in source')
        with self.assertRaises(ValueError):_parse_json_text('{}')

    def test_idempotent_title_duplicate_even_if_doi_changed(self):
        a=paper();b=dict(a,doi='https://doi.org/10.1000/1234')
        self.assertEqual(len(deduplicate([a,b])),1)

    def test_archive_has_both_news_and_papers_despite_paper_flood(self):
        import shutil
        source=Path(__file__).resolve().parents[1]
        with tempfile.TemporaryDirectory() as tmp:
            root=Path(tmp)
            shutil.copy(source/'config.yaml',root/'config.yaml')
            entries=[{**paper(f'Robot learning experiment number {i}'),
                      'url':f'https://arxiv.org/abs/2610.{i:05}'} for i in range(85)]
            entries += [{**news(f'Autonomous robot announcement {i}'),
                         'url':f'https://news.example/{i}'} for i in range(35)]
            out=run(root,now=NOW,records_override=entries,send_notifications=False)
            self.assertLessEqual(out['new'],55)
            self.assertGreater(out['papers'],0)
            self.assertGreater(out['news'],0)
