# 5-minute activation checklist

**This ZIP contains the app, not an already-running hosted service.**

1. Create a private GitHub repository: <https://github.com/new>.
2. Upload the extracted project files to the repository (including `.github/workflows/`). Or use the `git` commands in `README.md`.
3. Go to **Actions → Daily research and robotics radar → Run workflow**.
4. Open the newly saved `storage/digests/YYYY-MM-DD.md` and `storage/notes/` in your repo. If nothing shows, inspect the action log for network/feed warnings and check repository **Settings → Actions → General → Workflow permissions: Read and write**.
5. For AI-generated source-grounded summaries add GitHub Actions secret `GEMINI_API_KEY` (optional). For phone notifications add `TELEGRAM_BOT_TOKEN` and `TELEGRAM_CHAT_ID` (optional).

**Automatically runs:** 07:15 daily, Europe/London; Sunday research trends 08:45. Your computer may be off. GitHub schedules can be delayed.

**To search your reading library on your Mac:**

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements-dashboard.txt
streamlit run dashboard.py
```

**To test locally:**

```bash
pip install -r requirements.txt
python -m unittest discover -s tests -v
python -m radar.cli --dry-run
```

No n8n, no server, and no required paid API. Keep your GitHub repo **private** if your notes are private. You can edit all interest keywords and feed URLs in `config.yaml`.
