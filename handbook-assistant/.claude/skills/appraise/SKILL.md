---
name: appraise
description: Scores chosen sources and adds proposed claims, each with the exact source sentence (Dutch with English beside it), to the evidence log.
disable-model-invocation: true
argument-hint: "<source URLs or numbers from the candidate list>"
allowed-tools: WebFetch, Read, Write, Edit
---

# /appraise $ARGUMENTS

For each source in **$ARGUMENTS**:

1. Open it and save the relevant text to `sources/S###-<short-name>.md`, with the URL and the date it was accessed at the top. Use the next free source ID from `logs/evidence-log.md`.
2. Score it 1–5 on authority, recency, specificity, verifiability and transparency, with one reason per score.
3. Write one appraisal line: who says it, why they are worth believing, and the limitation.
4. Extract claims:
   - one fact per claim;
   - the exact sentence, copied word for word in the original language;
   - for Dutch sentences, an English translation beside it, marked "machine-assisted";
   - the sub-question it answers (E1–E5, I1–I5).
5. Add each claim as a new row to the table in `logs/evidence-log.md`, with the next free claim ID (C###) and status `proposed`.

Never paraphrase inside the "exact sentence" column. If you cannot find the exact sentence, do not create the claim. Only the tester changes a status to `accepted` or `rejected`.
