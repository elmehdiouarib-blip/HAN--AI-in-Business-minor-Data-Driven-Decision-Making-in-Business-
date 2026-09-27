---
name: search
description: Finds candidate public sources for the given sub-questions with English and Dutch web searches, and saves the list.
disable-model-invocation: true
argument-hint: "<sub-question IDs, e.g. E2 I2>"
allowed-tools: WebSearch, WebFetch, Read, Write
---

# /search $ARGUMENTS

1. Look up sub-questions **$ARGUMENTS** in the Research Proposal (§3) and the Dutch search terms (§5).
2. Run 3–5 English and 3–5 Dutch web searches. Prefer official and primary sources: legal texts (EUR-Lex), regulators (European Commission, Autoriteit Persoonsgegevens), statistics (CBS, Eurostat), sector bodies (FME, Koninklijke Metaalunie, KVK, RVO), and documented cases.
3. Show a table of 6–10 candidate sources: title · publisher · date · URL · language · type (statistics / law or regulator / case / research / trade press / vendor) · one line on why it may answer the sub-question.
4. Save the table as `sources/candidates-<sub-questions>-<date>.md`.

Do not extract claims yet. The developer decides which candidates go on to /appraise.
