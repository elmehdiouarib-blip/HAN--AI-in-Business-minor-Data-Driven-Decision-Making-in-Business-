---
name: draft
description: Writes a handbook chapter on the course template, using only accepted claims from the evidence log.
disable-model-invocation: true
argument-hint: "<chapter, e.g. 'knowledge gaps E3 I3'>"
allowed-tools: Read, Write
---

# /draft $ARGUMENTS

1. From `logs/evidence-log.md`, take only the rows with status `accepted` whose sub-question belongs to **$ARGUMENTS**. List their claim IDs first. If there are fewer than three per sub-question, say so and ask whether to continue.
2. Write the chapter for the target reader in the Research Proposal (§1), with these headings in this order:
   - The question, for this kind of SME
   - The translation
   - Illustrative use case (CRISP-DM)
   - Recommended tooling
   - Responsible AI & trust
   - First five steps for an owner (exactly five, each naming who does it in brackets; at least one reversible)
   - Sources (table: ID · source · supports · who says it and why credible · limitation)
   - What our platform drafted, and what we checked
3. End every factual sentence with its source ID, for example [S007]. Where evidence is missing, write "Evidence not found: …". Never fill a gap with fluent text.
4. In the last section, list the claim IDs used, and leave "[team checks: …]" for the tester. Also say which claims rest on field research and which on desk research. If there was no interview, add what the page cannot tell the owner because the firm itself was not asked.
5. Save the chapter as `chapters/<chapter>-draft-<date>.md`.

Do not use web search in this step, and do not take content from `wiki/`: it is never a source, and its unchecked lines are not evidence.
