"""Send a single Telegram digest after the deep-review stage, using bot chat ID."""
import json, os
from pathlib import Path
from datetime import datetime
from zoneinfo import ZoneInfo
from .notify import telegram_send

def run(root="."):
    root=Path(root)
    day=datetime.now(ZoneInfo("Europe/London")).date().isoformat()
    catalog=root/"storage/catalog.json"
    if not catalog.exists():return False
    entries=[r for r in json.loads(catalog.read_text(encoding="utf-8")) if r.get("first_seen")==day]
    if not entries:return False
    state=root/"storage/telegram-delivered.json"
    past=json.loads(state.read_text(encoding="utf-8")) if state.exists() else []
    if day in past:return False
    papers=[r for r in entries if r.get("kind")=="paper"]
    news=[r for r in entries if r.get("kind")=="news"]
    chunks=[f"🤖 Robotics & AI Radar — {day}",f"📚 {len(papers)} papers · 📰 {len(news)} news"]
    report=root/"storage/deep"/(day+".md")
    if report.exists():
        text=report.read_text(encoding="utf-8")
        reviews=[]
        for block in ("\n"+text).split("\n## ")[1:]:
            if "**Status:** reviewed" not in block:continue
            finding=next((x.split("**Reported findings:**",1)[1].strip()
                          for x in block.splitlines() if x.startswith("**Reported findings:**")),"")
            if finding:reviews.append((block.splitlines()[0],finding))
        if reviews:
            chunks.append("\n🔬 DEEP-READ FINDINGS (author claims)")
            for title,finding in reviews[:2]:chunks.append(title[:105]+"\n"+finding[:250])
        else:chunks.append("\n🔬 Deep AI review not available today.")
    chunks.append("\n📚 NEW PAPERS")
    for p in papers[:3]:chunks.append("• "+p["title"][:110]+"\n"+p.get("url",""))
    chunks.append("\n🌍 AI/ROBOTICS NEWS")
    for n in news[:3]:chunks.append("• "+n["title"][:110]+"\n"+n.get("url",""))
    repo=os.getenv("GITHUB_REPOSITORY","")
    if repo:
        base="https://github.com/"+repo+"/blob/main/storage/"
        chunks.append("\nFull digest: "+base+"digests/"+day+".md")
        if report.exists():chunks.append("Deep reviews: "+base+"deep/"+day+".md")
    chunks.append("\nCheck the primary source before relying on results.")
    sent=telegram_send("\n".join(chunks)[:3900])
    if sent:state.write_text(json.dumps(past[-60:]+[day],indent=2)+"\n",encoding="utf-8")
    print("Telegram sent:",sent)
    return sent

if __name__=="__main__":run()
