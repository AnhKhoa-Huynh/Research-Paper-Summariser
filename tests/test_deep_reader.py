"""Focused offline regression tests for the evidence-linked deep reader."""
import json
import os
import unittest
from unittest.mock import patch
from radar import deep_read

class FakeResponse:
    def __init__(self,data):
        self.data=data
    def raise_for_status(self):
        pass
    def json(self):
        return self.data

class FakeSession:
    def __init__(self,output):
        self.output=output
        self.payload=None
    def post(self,url,**kwargs):
        self.payload=kwargs["json"]
        return FakeResponse(self.output)

class DeepReadTests(unittest.TestCase):
    def setUp(self):
        self.page_text="the model achieved 0.8 success rate on the benchmark task."
        self.pages=[(3,self.page_text)]
        self.text="[[PAGE 3]]\n" + ("some scientific source text. "*100)
        self.item={"title":"Robot Paper"}
        self.fields={f:"Not reported" for f in deep_read.FIELDS}
        self.fields["results"]="The authors report an experiment."
        self.fields["evidence"]=[
            {"page":3,"claim":"Author statement","quote":"the model achieved 0.8 success rate"}]
    def test_json_schema_review_and_grounded_evidence(self):
        response={"candidates":[{"finishReason":"STOP","content":{"parts":[{"text":json.dumps(self.fields)}]}}]}
        s=FakeSession(response)
        with patch.dict(os.environ,{"GEMINI_API_KEY":"test-only","GEMINI_MODEL":"gemini-3.5-flash-lite"}):
            review,error=deep_read.analyse(self.item,self.text,self.pages,s)
        self.assertEqual(error,"")
        self.assertIsNotNone(review)
        self.assertEqual(review["evidence"][0]["page"],3)
        self.assertEqual(s.payload["generationConfig"]["responseMimeType"],"application/json")
        self.assertIn("responseJsonSchema",s.payload["generationConfig"])
        self.assertGreaterEqual(s.payload["generationConfig"]["maxOutputTokens"],4000)
    def test_no_fake_success_on_empty_output(self):
        s=FakeSession({"candidates":[{"finishReason":"MAX_TOKENS","content":{"parts":[]}}]})
        with patch.dict(os.environ,{"GEMINI_API_KEY":"test-only"}):
            review,error=deep_read.analyse(self.item,self.text,self.pages,s)
        self.assertIsNone(review)
        self.assertIn("token limit",error)
    def test_invalid_evidence_quote_is_rejected(self):
        wrong=dict(self.fields)
        wrong["evidence"]=[{"page":3,"claim":"Unsupported","quote":"this invented number was proven"}]
        s=FakeSession({"candidates":[{"finishReason":"STOP","content":{"parts":[{"text":json.dumps(wrong)}]}}]})
        with patch.dict(os.environ,{"GEMINI_API_KEY":"test-only"}):
            review,_=deep_read.analyse(self.item,self.text,self.pages,s)
        self.assertEqual(review["evidence"],[])
    def test_missing_key_remains_unreviewed(self):
        with patch.dict(os.environ,{"GEMINI_API_KEY":""}):
            review,error=deep_read.analyse(self.item,self.text,self.pages,FakeSession({}))
        self.assertIsNone(review)
        self.assertIn("missing",error)
    def test_size_limit(self):
        self.assertEqual(deep_read.MAX_BYTES,40*1024*1024)

if __name__=="__main__":unittest.main()
