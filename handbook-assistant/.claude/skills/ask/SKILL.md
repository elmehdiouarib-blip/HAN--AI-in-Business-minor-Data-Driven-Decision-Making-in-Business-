---
name: ask
description: Answers a question from the wiki only, with a page link and citation after every claim, logs which pages were read and used, and files the answer in the wiki if a team member says so.
disable-model-invocation: true
argument-hint: "<your question, e.g. what do we know about privacy as a barrier?>"
allowed-tools: Read, Write, Edit, Glob, Grep
---

# /ask $ARGUMENTS

1. Read `wiki/index.md` first, then the pages that bear on **$ARGUMENTS**. Keep a list of every page you read. Use only the wiki: no web search, no general knowledge, no memory.
2. Answer in plain English under three headings:
   - **Accepted evidence:** lines cited `[C###, S###]`;
   - **Not yet checked:** lines cited `[S###, unchecked]`, which the tester has not accepted;
   - **Unknown:** what the wiki has no evidence for, with a suggested `/search` or `/appraise`.
   After every claim, give its citation and the page it came from, for example `[C014, S012] (topics/barriers-to-ai.md)`. Mark anything that combines lines "Interpretation:". If the wiki records a debate on the point, give both sides.
3. Add a line at the top of the list in `wiki/log.md`: date · /ask · the question · pages read · pages used in the answer · saved: no.
4. End with: *Save this answer to the wiki? Say "save it".*
5. Only if a team member then says "save it": save the answer as `wiki/answers/<short-name>.md` using the answer template in `wiki/README.md`, add it to `wiki/index.md`, link to it from the topic pages it draws on, and change the log line to "saved: yes".

An answer is never a source for a chapter. Apart from the log line and step 5, change no file.
