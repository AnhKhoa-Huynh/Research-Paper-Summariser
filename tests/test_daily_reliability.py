"""Offline tests for missed-run backups and at-most-once Telegram delivery."""
import json
import tempfile
import unittest
from datetime import datetime
from pathlib import Path
from unittest.mock import patch
from zoneinfo import ZoneInfo
from radar.guard import should_run
from radar.deliver import run as deliver


class DailyReliabilityTests(unittest.TestCase):
    def setUp(self):
        self.folder=tempfile.TemporaryDirectory()
        self.addCleanup(self.folder.cleanup)
        self.root=Path(self.folder.name)
        self.store=self.root/"storage"
        self.store.mkdir()
        self.day=datetime.now(ZoneInfo("Europe/London")).date().isoformat()

    def test_first_schedule_runs(self):
        now=datetime(2026,11,2,5,0,tzinfo=ZoneInfo("Europe/London"))
        self.assertTrue(should_run(self.root,"schedule",now))

    def test_backup_skips_if_delivered(self):
        now=datetime(2026,11,2,6,0,tzinfo=ZoneInfo("Europe/London"))
        (self.store/"digests").mkdir()
        (self.store/"digests"/"2026-11-02.md").write_text("Today's report",encoding="utf-8")
        (self.store/"telegram-delivered.json").write_text('["2026-11-02"]',encoding="utf-8")
        self.assertFalse(should_run(self.root,"schedule",now))
        self.assertTrue(should_run(self.root,"workflow_dispatch",now))

    def test_empty_day_still_sends_telegram(self):
        (self.store/"catalog.json").write_text("[]",encoding="utf-8")
        with patch("radar.deliver.telegram_send",return_value=True) as send:
            self.assertTrue(deliver(self.root))
            self.assertEqual(send.call_count,1)
            self.assertIn("No newly qualifying",send.call_args[0][0])
            self.assertIn(self.day,json.loads(
                (self.store/"telegram-delivered.json").read_text(encoding="utf-8")))
            self.assertTrue(deliver(self.root))
            self.assertEqual(send.call_count,1)

    def test_failed_delivery_is_not_marked_successful(self):
        (self.store/"catalog.json").write_text("[]",encoding="utf-8")
        with patch("radar.deliver.telegram_send",return_value=False):
            self.assertFalse(deliver(self.root))
        self.assertFalse((self.store/"telegram-delivered.json").exists())


if __name__=="__main__":
    unittest.main()
