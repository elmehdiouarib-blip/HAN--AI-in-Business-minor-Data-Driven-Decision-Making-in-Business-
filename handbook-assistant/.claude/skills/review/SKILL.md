---
name: review
description: The tester accepts or rejects proposed claims by clicking choices, with the assistant's recommendation shown, and the decisions are recorded in the evidence log.
disable-model-invocation: true
argument-hint: "<claim range, e.g. C043-C059, or leave empty for all proposed claims>"
allowed-tools: AskUserQuestion, Read, Edit, Write, Grep
---

# /review $ARGUMENTS

1. Take the `proposed` rows in `logs/evidence-log.md`: the range in **$ARGUMENTS**, or all of them. Show a short table: ID · claim · source · your recommendation (accept, or reject with a reason such as "second-hand", "vendor figure", "not in the source", "not relevant").
2. Ask with **AskUserQuestion** (recommended option first, at most 4 options per question and 4 questions per call):
   - *Who is checking?* Offer the names already in the "Checked by" column; the tester can type another name.
   - *How do you want to review these claims?* → "Accept my recommended set: <IDs> (Recommended)" / "Choose claim by claim" / "Accept all" / "Not now".
   In the question text, remind the tester: *only accept claims you have checked against the saved source in `sources/`.*
3. **Claim by claim:** one multiple-choice question per source, with up to 4 claims each: *Tick the claims you accept; unticked claims are rejected.* For rejected claims, ask *Why?* with reasons as options (the tester can type another).
4. Record every decision in the evidence log as `CLAUDE.md` requires: status `accepted` or `rejected`, and "Checked by" with the tester's name, the date, and the reason for a rejection.
5. Reply with the totals (accepted, rejected, still proposed) and the next step: `/wiki` to sync, then `/draft`.

Only the tester's choices change a status. Never accept or reject on your own.
