---
name: appraise
description: Scores chosen sources and adds proposed claims, each with the exact source sentence (Dutch with English beside it), to the evidence log.
disable-model-invocation: true
argument-hint: "<source IDs, URLs or candidate numbers; or leave empty to choose from the latest candidate list>"
allowed-tools: AskUserQuestion, WebFetch, Read, Write, Edit, Bash, PowerShell
---

# /appraise $ARGUMENTS

If **$ARGUMENTS** is empty, read the newest `sources/candidates-*.md` and ask with AskUserQuestion *Which sources should I appraise?*: multiple-choice questions of up to 4 sources each, recommended ones first, each option saying "type · language · why it helps".

For each chosen source:

1. If it is a source ID whose text is already saved in `sources/` (for example after /add), use that saved text. Otherwise add it first, as /add does: convert it with `python tools/to_text.py` (web pages, PDF, Word, PowerPoint, Excel, CSV, text, subtitle files), using the next free source ID across both `logs/evidence-log.md` and `sources/`. The saved file's header records the address, date accessed, format, what was actually read and who chose it. If the text cannot be read at all, say so and stop.
2. Score it 1–5 on authority, recency, specificity, verifiability and transparency, with one reason per score.
3. Write one appraisal line: who says it, why they are worth believing, and the limitation.
4. Extract claims:
   - one fact per claim;
   - the exact sentence, copied word for word in the original language;
   - for Dutch sentences, an English translation beside it, marked "machine-assisted";
   - the sub-question it answers (E1–E5, I1–I5).
5. Add each claim as a new row to the table in `logs/evidence-log.md`, with the next free claim ID (C###) and status `proposed`.

Never paraphrase inside the "exact sentence" column. If you cannot find the exact sentence, do not create the claim. Only the tester changes a status to `accepted` or `rejected`.
