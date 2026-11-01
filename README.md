# Robotics & AI Research Radar

**A daily research-paper + robotics/AI news assistant without n8n.** Python, scheduled GitHub Actions, Git-versioned notes, optional Gemini summaries, optional Telegram notifications, and a local Streamlit search interface.

This is a *working software project* (not a live deployed account). You need to place it in **your own GitHub repository** and run the workflow once to turn on unattended collection.

## What it does

```text
07:15 Europe/London — GitHub Actions scheduler (runs without your laptop)
    ├─ arXiv: cs.RO, cs.CV, cs.AI, cs.LG, cs.CL
    ├─ OpenAlex: HRI, robot learning, swarm/robotics, CV
    └─ Industry/AI news: The Robot Report, IEEE Spectrum, Google News RSS
                ↓
       recent-date filtering (3 days) + dedup + topic weights
                ↓
       choose top relevant papers and news, avoid repeats
                ↓
       summary from abstract/RSS (optional Gemini)
                ↓
       individual Markdown notes + JSON catalog + daily digest
                ↓
       Git commit to your PRIVATE repo + optional Telegram alert

Sunday 08:45 Europe/London — seven-day trend recap
On demand — local Streamlit dashboard (search, topic/source filters)
```

Default topical priorities: **human–robot interaction / physical collaboration**, dexterous manipulation, multi-agent/swarm systems, classical and learned robotics, 3D/computer vision, AI/ML, NLP. Edit weights and keywords in `config.yaml` at any time. These are preferences, not hard exclusions: other AI discoveries can still appear.

## 1 — Get it running free, without hosting anything

**Recommended: a PRIVATE GitHub repository.** Your personal reading notes and digests will be committed to it, so *don't use a public repo unless you want those visible to the world.* A free GitHub account includes an Actions minute allowance for private repositories; quotas, scheduled delays, and rate limits vary. Public repos generally get free standard Actions runners but expose the saved content. If you don't want GitHub, use the local cron section below.

1. On https://github.com/new make a **Private** repo (e.g. `robotics-research-radar`). Do NOT pre-populate it with README/license, since this ZIP already has files.
2. Unzip this project on your computer. In Terminal from the project folder:

   ```bash
   git init
   git branch -M main
   git add .
   git commit -m "Initialize research radar"
   git remote add origin https://github.com/YOUR_USERNAME/robotics-research-radar.git
   git push -u origin main
   ```

   Use your authenticated GitHub CLI or Git Credential Manager; GitHub account passwords are **not** used for git HTTPS authentication. A manual ZIP upload through GitHub's Add file > Upload files is also possible, but check that the hidden `.github/workflows/` files actually uploaded.
3. In the repository, open **Actions → Daily research and robotics radar → Run workflow → Run workflow**. The agent attempts to retrieve real data and saves a daily digest in `storage/digests/` and notes in `storage/notes/`. Inspect the run logs for source/API failures.
4. Check **Settings → Actions → General → Workflow permissions** and allow *Read and write permissions*, if your account/repo defaults to read-only. This is needed so the bot can push daily notes to the private repository; the workflow also declares `contents: write`.
5. The workflow is scheduled **daily at 07:15 UK time** (handles GMT/BST), and the weekly report at 08:45 Sundays. GitHub scheduled jobs are best-effort and can be delayed; the repository must remain active, with Actions enabled.

**No email, LLM token or API key is needed for a basic first run.** This mode extracts concise source snapshots rather than pretending a machine generated them. It is useful for collection, ranking, sources and archiving.

## 2 — AI-written summaries (optional)

To produce a short, critical summary, **Google Gemini 2.5 Flash-Lite** is supported as an optional enhancer. Google's API currently offers a limited free tier for this model in supported regions, including the UK, subject to quotas and changing terms. **The free tier may use submitted content to improve Google's products**, so do not submit confidential/unpublished papers or private research notes. This project only sends public titles and abstracts or RSS excerpts, not your personal notes or PDFs.

1. Create a Gemini API key at https://aistudio.google.com/apikey .
2. In GitHub → your repo → Settings → Secrets and variables → Actions → **New repository secret**, add `GEMINI_API_KEY`. Never add the key to `config.yaml` or source code.
3. Run the daily workflow again when new items arrive. Already archived items are deliberately not rewritten; use new papers to evaluate LLM summaries. The optional model is `gemini-2.5-flash-lite`, controlled by `GEMINI_MODEL` in the workflow.

The agent's Gemini prompt explicitly requires **only the supplied source text**, a source-attributed finding, a note about limitations, and a short explanation of research relevance. It is **not** a full-text fact-check or a true literature review. In no-key mode `summary_mode=source_excerpt` and `method/key_finding` fields say when evidence is missing.

## 3 — Telegram morning notifications (optional)

To see a digest on your phone even when your laptop is off:

1. In Telegram chat with `@BotFather`, type `/newbot` and keep the issued **bot token** private.
2. Open a chat with your new bot, press Start, and send `/start`.
3. Get your numerical chat ID via your bot's `getUpdates` method, or locally with `python scripts/get_telegram_chat_id.py` after setting `TELEGRAM_BOT_TOKEN` as an environment variable. **Never share a bot token or paste it into public websites.**
4. Add GitHub Actions secrets `TELEGRAM_BOT_TOKEN` and `TELEGRAM_CHAT_ID`.
5. Future runs with *new relevant items* will send a compact linked list. **If nothing new is discovered, no duplicate alert is sent.** Reports are always available inside the repository.

Telegram messages contain paper titles/news headlines and public source URLs, not the full private notes.

## 4 — Run on your own computer (or Google Colab)

Python 3.11+ is recommended.

```bash
python3 -m venv .venv
source .venv/bin/activate     # Windows: .venv\Scripts\activate
python -m pip install -r requirements.txt
python -m radar.cli --dry-run
```

To use optional secrets locally, put them in shell environment variables (example entries in `.env.example`); `radar.cli` does **not** automatically read `.env`, to avoid accidental exposure. Run `python -m unittest discover -s tests -v` to verify the code.

To browse your archive:

```bash
pip install -r requirements-dashboard.txt
streamlit run dashboard.py
```

The Streamlit dashboard runs **locally** on your computer; it is not automatically a public cloud website. For a self-hosted server, run `python -m radar.cli` with a scheduling service such as cron, and back up the `storage/` directory. Colab is suitable for experimenting but **not reliable for daily unattended scheduling** because sessions time out.

Example local Linux/macOS cron (machine must be powered on; change for DST or use `systemd` calendar timers):

```text
15 7 * * * cd /absolute/path/robotics-research-radar && /absolute/path/to/python -m radar.cli
```

## 5 — Your research library

- `config.yaml` — topics, priorities, sources, result counts, recency window.
- `storage/catalog.json` — machine-readable database; updated only for new records.
- `storage/digests/YYYY-MM-DD.md` — short morning digest with paper/news sections.
- `storage/notes/paper/*.md`, `storage/notes/news/*.md` — personal editable notes, source provenance and reading checkboxes.
- `storage/weekly/YYYY-MM-DD.md` — topic counts, top research, news recap.
- `dashboard.py` — local keyword and topic search; later you can add embeddings/RAG.
- `tests/` — offline tests for parsing, ranking, deduplication, idempotency and notes.

Your manual notes are preserved when the agent runs again because previously seen items are not overwritten. If you want to mark a paper as read, edit its note directly in GitHub or your local clone.

### How newness works

- Searches the last **three days** to tolerate publication delays/weekends.
- Compares new items with archived titles and canonical identifiers, not just published dates.
- Saves a record only the first time it is discovered; a retry is safe.
- Scores the match to your topics. A paper is *relevant* if a topic matches; a news item is *reported* by the linked publisher; neither is automatically a verified scientific breakthrough.
- arXiv is a preprint server. An arXiv appearance alone **does not establish peer review**. OpenAlex has multiple work types; the agent does not guess peer-review status.

### Caveats and reliability

- **Network-dependent:** GitHub must be enabled; arXiv, OpenAlex and RSS must be reachable. Per-source errors are logged and recorded in digests. For total outages, the job may produce no news: inspect logs rather than assuming nothing happened.
- **Not full-text RAG yet:** Automated summaries operate on abstracts and RSS excerpts, not the entire PDF. That reduces cost and the risk of invented findings. Full-paper PDF extraction, evidence-linked Q&A, semantic embedding search, recommendation feedback and Zotero sync are useful future enhancements; they are not falsely labelled as implemented.
- **No public repo for private notes:** GitHub Actions does not guarantee confidentiality if you publish your repository. Avoid uploading confidential PDFs or credentials.
- **LLM budgets:** Gemini free-tier rate and token quotas can change; when the model is unavailable, the pipeline falls back to a clearly labelled source excerpt.
- **News feeds:** Google's RSS format is unofficial; publishers sometimes change RSS URLs, or have missing timestamps. Undated news is excluded rather than mislabelled as fresh.
- **Scheduling:** GitHub Actions may postpone scheduled jobs or disable them in inactive repositories; occasionally verify the Actions history.
- **Copyright:** The system links to original articles and stores only abstracts/RSS excerpts and short summaries; it does not redistribute full text, PDF collections, or premium material.

## Security and costs

The repository can be private, the code is free/open for your personal use, and no n8n, always-on PC, dedicated server or paid API is required for *basic collection + archiving*. Optional Gemini, Telegram and OpenAlex keys are in GitHub encrypted Actions Secrets. GitHub minutes/quota and provider policies may apply. Review free-tier retention/privacy terms before enabling a third-party LLM.

## Test or troubleshoot

```bash
python -m unittest discover -s tests -v
python -m radar.cli --dry-run
```

If you get no new papers, check `Actions → last run → Fetch, rank, summarize and archive` for warning messages. Confirm `config.yaml` search terms and lookback; see whether `storage/catalog.json` already contains those papers. If the repo can't push, check repository workflow permissions and branch protections. If notifications fail, check bot secrets and make sure you've started the bot conversation. For a first dry run, use a new empty catalog.

## Where the design came from

Inspired by a 2025 Medium article on a private AI research assistant (arXiv → PDF → LLM → tags → search → notifications). This implementation keeps discovery, summaries, notes and searching, adds robotics-world news, weighted HRI/swarm/dexterity ranking, cross-source dedup, source attribution, weekly trends, idempotent note updates and GitHub timezone-aware scheduling. It deliberately postpones full-PDF chunking and RAG until the foundational workflow is verified on real daily data.
