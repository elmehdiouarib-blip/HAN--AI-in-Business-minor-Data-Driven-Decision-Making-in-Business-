AEL · Team 08 · 26 September 2026 · Extends our Technical Blueprint · Serves our PRD

# 1. What the platform has to know

| **What**                                                                                               | **Where it comes from**                                                     |
|--------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------|
| The target reader, the sub-questions (E1–E5, I1–I5), the quality criteria (C1–C7) and the search terms | Our Research Proposal                                                       |
| What the agent must do, and how we measure it                                                          | Our PRD                                                                     |
| Its parts, its skills and the line it may not cross                                                    | Our Technical Blueprint and this document (in the project instructions)     |
| How we build and test it, week by week                                                                 | Our Build plan (week 4)                                                     |
| The claims we may cite, each with its exact source sentence and appraisal                              | The evidence log, filled by /appraise and checked by the tester             |
| Where we stopped, what we decided, and what comes next                                                 | The session log, written by /save at the end of each session                |
| This week’s source texts                                                                               | The web (CBS, EUR-Lex, the AP, KVK, trade press, vendors), found by /search |
| A short summary of each session and how the team likes to work                                         | The project’s built-in Memory, filled automatically and by /save            |

# 2. Where it lives, and how it is found again

| **Place**                          | **What lives there**                                                                          | **How it is found again**                                                    |
|------------------------------------|-----------------------------------------------------------------------------------------------|------------------------------------------------------------------------------|
| **Instructions** (project section) | Role, the six skills, tool rules, evidence rules, the line                                    | Claude follows them in every chat                                            |
| **Context** (project section)      | Research Proposal, PRD, Blueprint, this document, Build plan, evidence-log.md, session-log.md | Claude reads it in every chat. We keep it small, so everything stays in view |
| **The chat**                       | This week’s source texts, while they are being appraised                                      | Only within that chat; what counts goes into the evidence log                |
| **Memory** (project section)       | A short summary of each session and how we work                                               | Claude uses it automatically in every chat; never cited as a source          |

**Our choice:** we *compile* each source once, when it is appraised, into evidence-log rows that keep the exact source sentence. We then *look up* those rows when a chapter is drafted. Raw source texts are not stored in the Context. Memory between sessions comes from the session log.

**The path from a question to the passage that answers it** (example: the AI-safety chapter, sub-question E2):

1.  The PM types /start. Claude reads the session log: “Next: AI-safety chapter, E2 and I2.”

2.  /search E2 finds, among others, the Dutch data-protection authority’s warning about staff entering personal data into AI chatbots.

3.  /appraise proposes claim C014 with the exact sentence from the AP page and its appraisal. The tester accepts it.

4.  /draft uses only accepted rows tagged E2 and writes: “…reporting it to the AP is often mandatory [S12].”

5.  /check looks up S12 in the evidence log, finds accepted claim C014, and passes the sentence. The reader can follow [S12] to the source.

# 3. Why this, and not the alternatives

| **Option**                                                                       | **Why not (or why)**                                                                                                                                                                                                                                               |
|----------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **A. Rely on Claude’s built-in memory only**                                     | No setup, but memory is Claude’s own summary. We cannot see all of it, correct it reliably or prove what it contained, so the PRD target “/start is right every session” could not be checked. We keep it as a backup only.                                        |
| **B. Add every source to the project’s Context** and let Claude search it        | Easy, but unchecked and accepted sources would mix. The Context would fill up quickly, and Claude could no longer read all of it in every chat. We could no longer show that each sentence rests on an accepted source.                                            |
| **C. A separate database**                                                       | Precise, but it needs code and hosting a non-coder cannot run. That is far more than five chapters need.                                                                                                                                                           |
| **Our choice:** documents plus two logs in the Context; Memory as a second layer | It serves the PRD promises directly: every claim traceable to its exact sentence (PRD §2), 95% of draft sentences checkable (PRD §3), Dutch originals kept (PRD §5), and memory we can read (PRD §2, step 7). *Cost:* the PM uploads two files after each session. |

**What would make us switch:** if the evidence log grows so large that Claude can no longer read the whole Context in one go (we check at 150 rows), we move finished chapters’ rows to an archive file outside the project. If the PM forgets to upload the logs twice, we attach the session log to every /start instead.

# 4. The line, kept

Our blueprint’s line is that **interview material never enters the Claude Project**.

- **Where protected material is stored:** in a protected folder that only our team can open. It is outside Claude, and never in a drive connected to Claude. Location: [name the folder]. Recordings are deleted when the consent text says.

- **What stops the platform reading it:** there is no route in. It is never uploaded or pasted, and no connector reaches it. The project instructions tell Claude to stop and warn if such material appears. Only the PM may write an anonymised finding into the evidence log, labelled “Interview evidence”, and only if the consent text allows it.

- **If it goes wrong:** delete the chat and any related memory, write it in the session log the same day, and tell the lecturer.

# 5. The open questions

The Socratic tutor’s questions on our blueprint, with a short answer each: what we changed, or why we left it.

| **Tutor’s question**                     | **Our answer**                                                 |
|------------------------------------------|----------------------------------------------------------------|
| [question 1] | [what we changed / why we left it] |
| [question 2] | […]                                |
| [question 3] | […]                                |

## Decision log: entry 1

| **Decision**                                                                                                                      | **What failed**                                                                                                                                       | **What we changed**                                                                                                                  | **Revisit when**                                             |
|-----------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------|
| Knowledge lives in the project’s Context (our documents plus an evidence log); memory in a session log plus the project’s Memory. | Working in ordinary chats, the AI forgot our target reader and criteria between sessions, and a claim could not be traced back to where it came from. | Every claim now keeps its exact source sentence in the evidence log, and /save and /start carry memory from one session to the next. | The evidence log reaches 150 rows, or /start is wrong twice. |
