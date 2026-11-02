"""Prevent backup schedules from repeating completed research and notifications.

Scheduled attempts run only if the day's digest has not yet been delivered.
Manual workflow_dispatch and the deployment push are allowed to run for testing.
"""
import json
import os
from datetime import datetime
from pathlib import Path
from zoneinfo import ZoneInfo


def should_run(root, event_name="schedule", now=None):
    if event_name != "schedule":
        return True
    day=(now or datetime.now(ZoneInfo("Europe/London"))).astimezone(
        ZoneInfo("Europe/London")).date().isoformat()
    root=Path(root)
    digest=(root / "storage" / "digests" / (day+".md")).exists()
    path=root / "storage" / "telegram-delivered.json"
    if not (digest and path.exists()):
        return True
    try:
        delivered=json.loads(path.read_text(encoding="utf-8"))
    except (OSError, ValueError):
        return True
    return day not in delivered


def main():
    today=datetime.now(ZoneInfo("Europe/London")).date().isoformat()
    event=os.getenv("GITHUB_EVENT_NAME", "schedule")
    proceed=should_run(Path("."), event)
    value="true" if proceed else "false"
    print(f"Research preflight {today}: event={event}; run={value}")
    if not proceed:
        print("Today's digest already delivered; skipping duplicate scheduled work.")
    output=os.getenv("GITHUB_OUTPUT")
    if output:
        with open(output, "a", encoding="utf-8") as f:
            f.write(f"run={value}\n")


if __name__=="__main__":
    main()
