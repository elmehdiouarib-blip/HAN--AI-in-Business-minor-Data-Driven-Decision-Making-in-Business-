AEL · Team 08 · 26 September 2026 · Platform: the Handbook Assistant (a Claude Project) · Pen: developer [name] · Implements our PRD of 26 September 2026

*(Figure 1, the drawing, is in the Word version of this document.)*

*Figure 1. How one chapter is made. A team member types a skill. Claude runs it, following the project instructions and reading the project’s Context (our documents plus two logs). Only /search goes out to the web. /draft produces the chapter, which people review and publish. /save writes the updated logs, which the PM uploads again: this is how the agent remembers. Interview material stays in the protected folder and never enters the project.*

# 1. The parts

| **Part**                       | **What it does (one sentence)**                                                                                        | **Done by**             | **If it fails, by hand**  |
|--------------------------------|------------------------------------------------------------------------------------------------------------------------|-------------------------|---------------------------|
| Instructions (project section) | Tells Claude its role, the six skills, when to use which tool, and the rules it may never break.                       | Text written by the PM  | —                         |
| Context (project section)      | Gives Claude our research proposal, PRD, blueprint, knowledge architecture, build plan and the two logs in every chat. | Files added by the PM   | —                         |
| /start                         | Turns the session log into a short status: where we stopped and what is next.                                          | Claude                  | PM reads the log          |
| /search                        | Turns the week’s sub-questions into a list of 6–10 candidate sources from English and Dutch web searches.              | Claude + web search     | Developer searches        |
| /appraise                      | Turns sources into scored, proposed claims, each with the exact source sentence (Dutch with English beside it).        | Claude; tester decides  | Tester writes the rows    |
| /draft                         | Turns accepted claims into a chapter on the course template, with a source on every fact.                              | Claude                  | PM writes from the log    |
| /check                         | Turns a draft into a pass/fail list against criteria C1–C7, plus every sentence without a source.                      | Claude; tester confirms | Tester uses the checklist |
| /save                          | Turns the session into a new session-log entry and an updated evidence log.                                            | Claude; PM uploads      | PM writes the entry       |
| Review and publication         | Turns an approved draft into a published chapter on the course site.                                                   | Team; deployer          | Already manual            |
| Memory (project section)       | Keeps a short summary of each session and how we work; /save adds to it; never a source.                               | Claude, automatically   | The session log           |

**Who decides what happens next:** a person, always. Nothing runs until someone types a skill; Claude never chains steps by itself and never publishes. **Who checks before publication:** /check first, then the tester, who also opens three cited sources per chapter. **When a step goes wrong:** run it once more with the problem named, then do it by hand. A draft that fails /check goes back to /draft once, and after that the PM fixes it.

# 2. What passes between the parts

**The contract: evidence-log.md.** This is the file between /appraise and /draft. It is one table in the project’s Context, with one row per claim and these fields:

- claim ID · the claim (one fact) · sub-question (E1–E5, I1–I5) · source ID · source (publisher, title, date, link)

- exact sentence from the source, in its own language · English translation if Dutch (marked machine-assisted)

- appraisal: who says it, why credible, limitation · status: proposed / accepted / rejected · checked by (name, date)

/draft may use only rows with status *accepted*, and /check flags any sentence whose source is not on an accepted row. Because the original sentence stays in the row, a claim keeps its source even after translation. If /appraise fails, a person can fill in a row by hand.

**Second file: session-log.md**, the agent’s memory. It has one entry per session, newest first: date, what we did, decisions, open questions, next step. /save writes it and /start reads it.

# 3. The line nothing may cross

**Interview material from the company visit (recordings, notes, transcripts, and anything that identifies a person or customer) never enters the Claude Project:** not in a chat, the Context, the instructions or Memory.

- **Where it runs:** between the protected folder and the project. The protected folder is access-restricted to our team and is never uploaded, pasted or connected to Claude.

- **What keeps it there:** the project instructions tell Claude to stop and warn if such material appears, and never to store names in memory. The PM checks the project’s Memory every week. Only the PM may carry an *anonymised* finding across, as an evidence-log row labelled “Interview evidence”, and only if the signed consent text allows it.

| **What leaves our hands** | **What is sent**                           | **To**                               |
|---------------------------|--------------------------------------------|--------------------------------------|
| Everything in the project | Instructions, Context files, chats, Memory | Anthropic, which runs Claude         |
| /search and /appraise     | Search terms and web addresses             | The web, through Claude’s web search |
| The protected folder      | Nothing                                    | —                                    |

Every team member switches off the setting that lets Anthropic use chats to improve its models. Text on web pages is treated as material, never as an instruction: if a page tries to instruct Claude, Claude ignores it and warns us.

# 4. The trace to the PRD

| **PRD promise**                                                                    | **Carried by**                                   |
|------------------------------------------------------------------------------------|--------------------------------------------------|
| Resume where we stopped; /start right every session (PRD §2–3)                     | /start and session-log.md                        |
| Search in English and Dutch; Dutch original kept (PRD §5)                          | /search, /appraise, evidence-log.md              |
| Every claim linked to its exact source sentence (PRD §2)                           | /appraise and evidence-log.md                    |
| Draft only from accepted claims; “evidence not found” instead of guessing (PRD §2) | /draft                                           |
| A chapter passes C1–C7 before publication (PRD §3)                                 | /check, then the tester                          |
| A non-coder runs it; manual fallback for every step (PRD §4)                       | Typed skills; the last column of the parts table |
| Interview and confidential data never enter the agent (PRD §3 guardrail)           | The line (§3)                                    |
| No automatic publishing (PRD §6)                                                   | Review and publication by people                 |

**Departures from the PRD:** none. Every promise lands in a part.

**Decision, with the option we turned down.** We keep the agent’s memory in a session log that we can read and correct, with the project’s built-in Memory as a second layer. The option we turned down was to rely on built-in memory alone. *Cost:* the PM uploads the log after every session. *Gain:* memory the whole team can see, check and fix.

**Open questions:** Can all four of us share one project (Team plan), or does the PM keep the master copy? (PM, 28 Sep) · Does /start recall the last session correctly in a new chat? (tester, 30 Sep)
