# Demonstration (illustrative data; not real discoveries)

When the agent runs, it creates `storage/digests/YYYY-MM-DD.md` with two sections:

**Papers worth reading** — Original links, ranked research topics, abstract-based summary, claimed contribution, methods, limitations, and paper notes.

**Robotics and AI news** — Publisher headlines, original links, source-attributed summary, and a warning about claims that are not independently verified.

Every new item receives a persistent Markdown note in `storage/notes/{paper,news}/`. You can edit notes after they are saved; rerunning a day will not overwrite them.

The `storage/catalog.json` file contains structured searchable metadata. Run `streamlit run dashboard.py` to search titles, topics, original abstracts and notes.

No synthetic source is used for normal runs. The contents of this example are explanatory only.
