# Deep Research Radar — free-first upgrade

This feature branch adds a second phase after daily arXiv/OpenAlex/RSS discovery: attempt to read the full text of **up to two** top-ranked accessible scholarly PDFs daily, then generate structured Gemini reviews with explicit evidence and follow-up research ideas.

**You must enable Gemini manually:** GitHub repository → Settings → Secrets and variables → Actions → New repository secret → `GEMINI_API_KEY`. Get a free API key from https://aistudio.google.com/apikey . Choose a free-tier project without enabling paid billing if you require a strict £0 setup. Quotas and terms may change. The pipeline does not fall back silently to a paid model. Only public scholarly text is transmitted.

**You must enable Telegram manually:** Talk to @BotFather on Telegram and create a bot with /newbot. In Telegram, open your new bot and send /start. Find your numeric `chat_id` using `getUpdates` (or the script supplied in scripts/). Store `TELEGRAM_BOT_TOKEN` and `TELEGRAM_CHAT_ID` as GitHub Actions repository secrets. A phone number by itself does not allow a Telegram bot to message you. NEVER paste API keys, bot tokens, chat identifiers, or phone numbers into public GitHub files.

**Outputs**:
- Daily headlines: `storage/digests/YYYY-MM-DD.md`
- Full paper analyses: `storage/deep/YYYY-MM-DD.md`
- Single Telegram message with selected news, papers, deep findings, and links.

**Cost/limits:** GitHub Actions on standard runners is free for public repositories and has monthly allowances for private repos; Gemini free tier has usage/rate limits. This workflow limits PDF downloads to 12 MiB each, 35 pages, and 85k extracted text characters; it reviews at most two per day. PDFs are *not* retained in Git. A complete full-document review is not guaranteed if a PDF is scanned, unusually formatted, paywalled, has many figures, or is longer than those limits. The report labels limited coverage and unreviewed results. Source excerpts can include inaccurate text extraction; human verification is required.

**Professional follow-up practice:** For significant papers, manually verify evaluation setup, baselines and plots; check publication/peer-review status; inspect open-source code and datasets; attempt a small reproduction; record hypotheses, contradictions to prior work, and a next experiment in the archive. The current model is a *research triage assistant*, not a reliable independent referee.

**GitHub storage:** Not unlimited. Avoid archiving PDFs/embeddings/big JSON snapshots in Git. Keep compact notes and links, prune stale catalogs and move any future PDFs to a dedicated reference manager/storage provider. GitHub recommends keeping repositories small (ideally under 1 GB; strongly under 5 GB) and imposes individual file limits.

**Security:** The repository is currently public. Any pushed notes are public. Switch to private if you require confidentiality, understanding that private repositories have GitHub Actions minute quotas.

**Testing:** Local offline regression tests were run on the packaged version. Run the GitHub workflow once after merging; verify the resulting GitHub log and deep report. Missing keys are reported and do not masquerade as completed AI reviews.
