AEL · Team 08 · 26 September 2026 · Product: the *Handbook Assistant*, an AI agent built as a Claude Project · Author: product manager [name] · Developer [name] · Tester [name] · Deployer [name]

**What we build:** an AI agent that helps our team research and write one handbook chapter a week for owners of Dutch machine builders like Giesen. **For whom:** our four-person research team, and downstream the machine-builder owner who reads the handbook. **How we know it works:** one reviewed chapter a week, on time, in which every claim can be traced to a checked source.

# 1. Problem and users

**The problem.** Each week our team must find sources in English and Dutch, judge whether they are credible, turn them into a clear chapter and keep every claim traceable to its source. By hand this is slow, differs from member to member, and depends on who reads Dutch. A general AI chat does not help enough: it forgets our target reader and criteria between sessions, and it will write fluent claims without a source.

**Users of the platform (the research team):**

- **Product manager:** starts and closes each working session, decides the week’s questions, and keeps the files in the project’s Context up to date.

- **Developer:** runs the search and appraisal steps and maintains the agent’s instructions.

- **Tester:** accepts or rejects each claim and checks every chapter against the quality criteria.

- **Deployer:** publishes approved chapters on the course site.

**Reader of the output (never uses the platform):** the owner or manager of a Dutch machine builder, who reads one short chapter to make one decision.

**Why an agent.** Producing a chapter is a chain of steps: search, read, judge, extract, write, check. An agent can follow the same fixed steps every time, use tools (web search, file creation), read our research plan and criteria, and remember where we stopped last session. That is more than a wiki page or a single chat can do. A Claude Project gives us exactly these parts: **Instructions** (the agent’s skills and rules), **Context** (our documents and logs), **Memory** (what it remembers from our sessions) and, optionally, **Scheduled tasks**.

**Hypothesis.** With the Handbook Assistant, producing a reviewable chapter becomes faster and more reliable for our team. The time from first search to reviewable draft falls by at least 40% against a chapter made by hand, and at least 95% of the factual sentences in its first draft trace to a source the tester accepted.

# 2. What it must let a user do: from raw source to published chapter

| **Step**   | **The user types** | **The agent does**                                                                                                   | **A person does**                                    |
|------------|--------------------|----------------------------------------------------------------------------------------------------------------------|------------------------------------------------------|
| 1 Resume   | /start             | Reads the session log; says where we stopped and what is next                                                        | PM confirms this week’s sub-questions                |
| 2 Search   | /search E1 I1      | Searches the web in English and Dutch; lists 6–10 candidate sources                                                  | Developer keeps or drops sources                     |
| 3 Appraise | /appraise          | Scores each source; extracts claims with the exact sentence from the source; translates Dutch sentences into English | Tester accepts or rejects each claim                 |
| 4 Draft    | /draft             | Writes the chapter on the course template, using only accepted claims, each with its source                          | PM edits the text                                    |
| 5 Check    | /check             | Checks the draft against criteria C1–C7 and lists any sentence without a source                                      | Tester confirms; an outside reader checks for jargon |
| 6 Publish  | —                  | Nothing: the agent never publishes                                                                                   | Team approves; deployer publishes on the course site |
| 7 Remember | /save              | Writes a new session-log entry and the updated evidence log as files                                                 | PM uploads both files to the project                 |

**Must-haves:** search in English and Dutch; keep the exact source sentence with every claim; draft only from accepted claims and write “evidence not found” instead of guessing; check the chapter against the criteria; remember the previous session. **Nice to have:** chapters delivered as a ready Word file.

# 3. Output qualities: what a good chapter looks like

A good chapter passes the same seven checks as in our Research Proposal (§4):

- **C1** answers a real owner question for this sector · **C2** follows the course chapter template · **C3** every factual claim is sourced and every source appraised · **C4** clear for a non-technical owner · **C5** covers responsible AI · **C6** ends with five first steps with who does them · **C7** says what AI drafted and what we checked, and holds no confidential data.

**How we know the platform works:**

| **Measure**                                                            | **Target**                                      | **Checked by**           |
|------------------------------------------------------------------------|-------------------------------------------------|--------------------------|
| Chapters published on time (North Star)                                | 1 per week, weeks 4–6                           | Deployer                 |
| Time from first /search to reviewable draft                            | At least 40% faster than a chapter made by hand | PM, from the session log |
| Factual sentences in the first draft that trace to an accepted source  | 95% or more                                     | Tester, with /check      |
| /start correctly states what we did last session                       | Every session                                   | Tester                   |
| Interview material or confidential data entering the agent (guardrail) | Never                                           | Tester                   |

# 4. Known constraints

| **Constraint**                             | **How the Handbook Assistant meets it**                                                                                                                                |
|--------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| We direct an agent rather than hand-code   | All behaviour is written in plain language: the project instructions and six skills. No code is written. We use Claude, in a Claude Project, as our agent.             |
| We reuse the existing wiki and site        | The agent delivers each chapter as a Word or Markdown file, and the deployer publishes it on the course site. There is no new hosting and no database.                 |
| A non-coder must be able to run it         | Every step is a short command typed in a chat window, such as /search or /draft.                                                                                       |
| Every automated step has a manual fallback | Every step produces something a person can also make by hand (a source list, a claim row, a draft, a check list), and the two logs are ordinary files anyone can edit. |

# 5. The source material is partly Dutch

Much of the evidence on Dutch machine builders is Dutch: CBS, KVK, RVO, the data-protection authority (AP), and sector bodies such as FME and Koninklijke Metaalunie. The agent crosses this gap itself. /search always searches in Dutch as well as English. /appraise keeps the original Dutch sentence as the evidence, with an English translation beside it marked “machine-assisted”, so every team member can judge and use Dutch sources. Our Dutch-reading member checks only the Dutch sentences that end up in a chapter. The language no longer decides who can research. Interview recordings, which may be in Dutch, never go into the agent.

# 6. Out of scope, for now

- **No code, no database, no model training:** plain instructions and two files are enough for five chapters.

- **No chatbot for SME owners:** owners read reviewed chapters. A live answer could not be checked before they saw it.

- **No automatic publishing:** a person always approves and publishes.

- **No connection to company systems** (ERP, planning software): we have no access, and it would put company data at risk.

- **No audio:** interview recordings stay outside the agent.

# 7. Open questions and assumptions

**Assumptions**, and what happens if they are wrong:

- Claude can read our longer sources, such as legal texts and reports, in one chat. *If not:* we attach only the relevant sections.

- Our Claude plan’s usage limits allow one chapter a week. *If not:* we spread the steps over the week.

- The session log is enough to give the agent memory between chats. *If not:* we attach the log at the start of each chat.

| **Open question**                                                                                              | **Owner** | **How we find out**                                   | **By** |
|----------------------------------------------------------------------------------------------------------------|-----------|-------------------------------------------------------|--------|
| Does our plan let us share one project with all four members (Team plan), or does the PM keep the master copy? | PM        | Ask HAN and the lecturer                              | 28 Sep |
| Does the lecturer accept a Claude Project as our agentic platform?                                             | PM        | Ask in the week-4 session                             | 28 Sep |
| How long does a chapter take by hand (our baseline)?                                                           | PM        | Time the steps of one chapter                         | 30 Sep |
| Are Claude’s translations of legal Dutch good enough?                                                          | Developer | Translate 10 passages; the Dutch reader counts errors | 1 Oct  |
| Does /check find unsourced sentences reliably?                                                                 | Tester    | Compare /check with a manual check of one chapter     | 2 Oct  |
