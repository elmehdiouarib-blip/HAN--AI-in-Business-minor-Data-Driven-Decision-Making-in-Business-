---
name: answer
description: Answers one owner question from problem to handbook page in one command. At every decision the team clicks a choice (which sources to read, what goes into the wiki, which claims to accept), with the assistant's recommendation shown first.
disable-model-invocation: true
argument-hint: "<sub-question codes and a short name, e.g. E5 I5 making it last>"
allowed-tools: AskUserQuestion, WebSearch, WebFetch, Read, Write, Edit, Glob, Grep, Bash, PowerShell
---

# /answer $ARGUMENTS

Run the whole flow for **$ARGUMENTS**. At every decision, ask with **AskUserQuestion** so the team can click. Rules for every choice:
- put your recommended option first, labelled "(Recommended)", and say in each option what it means;
- at most 4 options per question and 4 questions per call; use more calls when there are more items;
- the team can always type its own answer ("Other");
- never decide for the team, and stop whenever the team chooses to stop.

**1 · The question.** State the owner's question for these codes (Research Proposal §3) in one sentence. Ask: *Is this the owner's question?* → "Yes, go on (Recommended)" / "Change the wording".

**2 · Sources.** Run /search for the codes, or reuse today's `sources/candidates-<codes>-*.md`. Ask *Which sources should I read?* as multiple-choice questions of up to 4 candidates each. Label each option "Publisher, title" and describe it as "type · language · why it helps". Mark the recommended ones. /add the chosen sources.

**3 · Claims.** /appraise the chosen sources. Claims are added as `proposed`. Show a short table: ID · claim · source · your note.

**4 · Wiki (human check 1).** Collect every source for the question, as `/wiki <codes>` does, and give the pause report: per source, who wrote and paid for it, what was read, the main points, and any debates. Ask *What goes into the wiki?* → "All sources, as planned (Recommended)" / "Let me choose the sources" (then one multiple-choice question per group of 4 sources) / "Not now". Write only what was chosen.

**5 · Tester review (human check 2).** Run /review for the new claims.

**6 · Page.** /wiki (sync), then /draft for the codes, then /check and /lint.

**7 · Result.** Show the /check verdict, the page's **five first steps for the owner** (the advice), and what is still to do. Ask *What next?* → "Save and push to GitHub (Recommended)" (runs /save, then commit and push) / "Also make a Word version" / "Stop here".

Never publish. Never take in interview material.
