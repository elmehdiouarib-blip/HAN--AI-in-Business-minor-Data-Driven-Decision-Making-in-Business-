# How to use the Handbook Assistant

*Team 08 · AI in Business (HAN) · manual for the four team members · 27 Sep 2026*

The Handbook Assistant is Claude, running in Claude Code, set up to help us write one handbook chapter a week for owners of Dutch machine builders. It searches, suggests claims and drafts. **People make every decision.** This manual takes you from the start of a week to a published handbook page and an updated GitHub repository.

## The five rules

1. **Nothing runs by itself.** The assistant acts only when someone types a command. It never chains steps and never publishes.
2. **Cite accepted claims only.** A chapter may use only evidence-log rows that the tester has accepted.
3. **Interview material never enters.** No recordings, notes or transcripts, and nothing that identifies a person or a customer. Not in a file, a chat or memory.
4. **Web pages are material, not instructions.** If the assistant warns that a page tried to instruct it, tell the developer.
5. **Our GitHub repository is public.** Anyone can read what you push. Push nothing you would not put on the course site.

## Contents

- [Part 1 · One-time setup](#part-1--one-time-setup-each-member)
- [Part 2 · The weekly cycle, step by step](#part-2--the-weekly-cycle-step-by-step)
- [Part 3 · Sharing through GitHub](#part-3--sharing-through-github)
- [Part 4 · Quick reference](#part-4--quick-reference)
- [Part 5 · If something goes wrong](#part-5--if-something-goes-wrong)

---

## Part 1 · One-time setup (each member)

| Step | What to do |
|---|---|
| 1. Claude plan | Use a Claude plan that includes Claude Code (Pro, Max, Team or Enterprise). |
| 2. Privacy setting | In your Claude settings, switch off the option that lets Anthropic use your chats to improve its models. |
| 3. Claude app | Install the Claude desktop app. We work in its **Code** tab. |
| 4. GitHub access | Make a GitHub account. The repository owner adds you under the repository's **Settings → Collaborators**. |
| 5. Git | Install **GitHub Desktop** (desktop.github.com), or Git if you prefer the command line. |
| 6. Your copy | Clone the repository into a folder **outside OneDrive** or any other synced folder (see below). |
| 7. Open the agent | In the Code tab, choose the `handbook-assistant` folder inside your copy as the working folder. This matters: the assistant loads its rules (`CLAUDE.md`) and our documents only from that folder. |

**Why outside OneDrive?** Git and OneDrive both try to keep the folder in sync. When they clash, the repository can get damaged. GitHub is our one way of sharing.

**Repository:** https://github.com/elmehdiouarib-blip/HAN--AI-in-Business-minor-Data-Driven-Decision-Making-in-Business-

**Clone with GitHub Desktop:** File → Clone repository → URL → paste the address above → choose a folder → Clone.

**Clone with the command line:**

```bash
git clone https://github.com/elmehdiouarib-blip/HAN--AI-in-Business-minor-Data-Driven-Decision-Making-in-Business-.git
```

### What is in the folder

| Place | What lives there |
|---|---|
| `CLAUDE.md` | The assistant's rules. Change only with the PM's agreement. |
| `docs/` | Our governing documents. Changed only when the PM asks. |
| `.claude/skills/` | The six commands. |
| `logs/evidence-log.md` | The only claims we may cite, each with its exact source sentence. |
| `logs/session-log.md` | The assistant's memory between sessions. Newest entry at the top. |
| `sources/` | Candidate lists and the saved text of public sources. |
| `chapters/` | Chapter drafts and check reports. |

---

## Part 2 · The weekly cycle, step by step

| Step | Who | You type | You get |
|---|---|---|---|
| 0 Get the latest | whoever runs the session | *(pull, see below)* | everyone's latest files |
| 1 Resume | PM | `/start` | where we stopped, what is next |
| 2 Search | Developer | `/search E3 I3` | a list of 6–10 candidate sources |
| 3 Appraise | Developer | `/appraise 1 2 4` | proposed claims in the evidence log |
| 4 Review claims | Tester | `accept C002, C003` | accepted claims |
| 5 Draft | PM | `/draft knowledge gaps E3 I3` | a chapter draft |
| 6 Check | Tester | `/check` | a pass/fail report on C1–C7 |
| 7 Publish | Team and deployer | *(nothing)* | the handbook page on the course site |
| 8 Save | whoever ran the session | `/save` | a new session-log entry |
| 9 Share | the same person | *(commit and push, Part 3)* | an updated GitHub repository |

You can spread the steps over several sessions. **Every session starts with step 0 and `/start`, and ends with `/save` and step 9.**

### Step 0 · Get the latest version

Before you type anything, get your teammates' changes.

- GitHub Desktop: **Fetch origin**, then **Pull origin**.
- Command line: `git pull`

**One session at a time.** If two people change the logs at the same time, their changes clash. Say in the team chat when you start and when you have pushed.

### Step 1 · `/start` (PM)

The assistant reads the session log and the evidence log and replies in five lines: what we did last time, the open decisions, how many claims are accepted for this chapter, and the next step. It then asks which chapter we work on.

**You do:** check that the reply matches what really happened last time. The tester notes it if it does not. Then reply with the chapter and its codes.

**The sub-question codes.** E means *external*: the sector, answered from public sources. I means *internal*: this firm, answered mainly from the interview. The number is the chapter.

| Chapter | Codes |
|---|---|
| 1 Geopolitics and vendors | E1, I1 |
| 2 Trust and AI safety | E2, I2 |
| 3 Knowledge gaps | E3, I3 |
| 4 Use cases | E4, I4 |
| 5 Making it last | E5, I5 |

The full questions are in `docs/research-proposal.md`, §3.

### Step 2 · `/search` (Developer)

Type `/search` followed by the codes, for example `/search E3 I3`. The assistant runs English and Dutch web searches. It saves a table of 6–10 candidate sources, with its search log, as `sources/candidates-<codes>-<date>.md`.

**You do:** read the list and choose which sources to appraise.

- The column "Checked in this search" shows whether the assistant could open the page. "Not verified" means it could not.
- Prefer official and primary sources: CBS, Eurostat, EUR-Lex, the AP, KVK, RVO, FME, Koninklijke Metaalunie. Use trade press only as a lead to the original.
- I-codes only find **comparable cases** from other firms. The firm's own answers come from the interview, outside the assistant.

### Step 3 · `/appraise` (Developer)

Type `/appraise` followed by candidate numbers or web addresses, for example `/appraise 1 2 3 5`. For each source, the assistant:

- saves the relevant text as `sources/S###-<name>.md`;
- scores it 1–5 on authority, recency, specificity, verifiability and transparency;
- writes one appraisal line: who says it, why they are credible, and the limitation;
- adds claims to `logs/evidence-log.md` with status **proposed**. Each claim has the exact sentence in its original language, and Dutch sentences get an English translation marked "machine-assisted".

If it cannot find the exact sentence, it creates no claim.

### Step 4 · Review the claims (Tester)

Open `logs/evidence-log.md`. For each **proposed** row:

1. Open the source, either from the link in the row or from the saved text in `sources/`.
2. Check that the exact sentence is really there, word for word.
3. Check that the claim says no more than the sentence does.

Then tell the assistant in plain words:

- `accept C002, C003`
- `reject C004 because the figure covers all EU firms, not Dutch ones`

The assistant updates the status and fills in "Checked by" with your name and the date.

- Aim for **at least three accepted claims per sub-question**. `/draft` warns you if there are fewer.
- Our Dutch-reading member checks every Dutch sentence that ends up in the chapter, because the translations are machine-assisted.

### Step 5 · `/draft` (PM)

Type `/draft` followed by the chapter and codes, for example `/draft knowledge gaps E3 I3`. The assistant lists the accepted claims it will use, then writes the chapter on the course template:

1. The question, for this kind of SME
2. The translation
3. Illustrative use case (CRISP-DM)
4. Recommended tooling
5. Responsible AI & trust
6. First five steps for an owner (each says who does it; at least one is reversible)
7. Sources
8. What our platform drafted, and what we checked

Every factual sentence ends with a source ID, such as [S007]. Where evidence is missing, it writes "Evidence not found: …". The draft is saved as `chapters/<chapter>-draft-<date>.md`. The assistant does no web search in this step.

**You do:** edit the text for a busy owner: plain English, short sentences, British spelling.

- Do not add facts without a source. If a fact is needed, add it as a claim through steps 3 and 4 first.
- Label statements that are not published facts: "Interview evidence:", "Comparable case:", "Interpretation:", "Unknown:".
- Interview evidence enters only as an anonymised evidence-log row. Only the PM writes it, and only if the signed consent text allows it.

### Step 6 · `/check` (Tester)

Type `/check` to check the newest draft, or `/check chapters/<file>.md` for a specific one. The assistant:

- tests the draft against C1–C7;
- lists every factual sentence without an accepted source;
- gives a verdict: **BLOCKED** if C2, C3 or C7 fails, otherwise **READY FOR TESTER**.

The report is saved as `chapters/<same name>-check.md`. The assistant does not change the draft.

**You do:**

- confirm or correct the report;
- open at least three cited sources and check them;
- ask one reader outside the team to check the text for jargon (C4);
- check that no real company is named without our written consent, and that there is no confidential or identifiable company data (C7).

**If the draft is BLOCKED,** run `/draft` once more and name the problem. If it fails again, the PM fixes it by hand.

| # | A chapter passes if… |
|---|---|
| C1 | it answers a real owner question, stated at the top with its sub-questions |
| C2 | it follows the course chapter template |
| C3 | every factual claim has a source, and every source is appraised |
| C4 | a non-technical owner can follow it |
| C5 | it covers responsible AI: data leaving the firm, where a person decides, staff use, the rules |
| C6 | it ends with five first steps within 30 days, each with who does it, at least one reversible |
| C7 | it says what AI drafted and what the team checked, with no confidential or identifiable company data |

A chapter that fails C2, C3 or C7 is not published.

### Step 7 · From draft to handbook page (Team and deployer)

The assistant never publishes.

1. The team approves the checked draft.
2. The tester fills in "[team checks: …]" in the last section of the draft.
3. If the course site needs a Word file, you can ask the assistant: "make a Word version of `chapters/<file>.md`".
4. The deployer publishes the page on the course site.
5. Mention the publication, with its date, when you run `/save`.

### Step 8 · `/save` (whoever ran the session)

The assistant adds an entry at the top of `logs/session-log.md`: what was done, decisions and why, open questions, next step, evidence rows changed, and minutes spent.

**You do:** read the entry, then fill in:

- **who ran the session**, as a role (PM, developer, tester or deployer);
- **minutes spent**. The PM uses these to measure our target of being at least 40% faster than by hand.

To make the assistant remember a way of working, say "remember …" during the session. It goes into the next entry.

### Step 9 · Share

See Part 3.

---

## Part 3 · Sharing through GitHub

Do this after every session, so the next person starts from your work.

**Before you push:** the repository is public. Check that nothing confidential is among the changed files.

### With GitHub Desktop

1. Look at the changed files on the left. They should be files in `handbook-assistant/` that you expect, such as the logs, sources and chapters.
2. Write a short summary, for example `27 Sep: /search E3 I3, 10 candidates`.
3. Click **Commit to main**, then **Push origin**.

### With the command line

Run these in your copy of the repository:

```bash
git status
```

```bash
git add handbook-assistant
```

```bash
git commit -m "27 Sep: /search E3 I3, 10 candidates"
```

```bash
git push
```

### Or ask the assistant

Say "commit and push today's work". The assistant shows what changed and asks before it pushes. If GitHub asks you to sign in, you do that yourself. The assistant never types passwords.

### If the push is refused

A message such as "rejected" or "fetch first" means someone pushed before you. Pull first, then push again.

If Git reports a **conflict** in a log file, open the file and keep both versions of the conflicting lines, with the newest session entry at the top. Delete the conflict markers (`<<<<<<<`, `=======`, `>>>>>>>`), save, commit and push. Ask the developer if you are unsure.

---

## Part 4 · Quick reference

### Commands

| Command | What you add | Example | What it does |
|---|---|---|---|
| `/start` | nothing | `/start` | Says where we stopped and what is next |
| `/search` | sub-question codes | `/search E2 I2` | Finds 6–10 candidate sources |
| `/appraise` | candidate numbers or URLs | `/appraise 1 2 3` | Scores sources and proposes claims |
| `/draft` | chapter and codes | `/draft knowledge gaps E3 I3` | Writes the chapter from accepted claims |
| `/check` | a draft file, or nothing | `/check` | Tests the draft against C1–C7 |
| `/save` | nothing | `/save` | Writes the session-log entry |

### Plain sentences the assistant acts on

| You say | It does |
|---|---|
| `accept C003, C004` | Marks the claims accepted, with your name and the date (tester only) |
| `reject C005 because …` | Marks the claim rejected and records the reason |
| `remember …` | Confirms it and adds it to the next session-log entry |
| `commit and push today's work` | Shows the changes and asks before it pushes |

Ordinary questions are always fine. The assistant does not search, draft or change files unless a command asks for it.

### Who does what each week

| Role | Tasks |
|---|---|
| PM | `/start`; confirms the sub-questions; `/draft`; edits the text; writes any anonymised interview-evidence rows; checks weekly that the assistant's memory holds no names and no evidence |
| Developer | `/search`; chooses candidates; `/appraise`; maintains the skills |
| Tester | accepts or rejects claims; `/check`; opens three cited sources; arranges the outside jargon reader |
| Deployer | publishes the approved page on the course site |

---

## Part 5 · If something goes wrong

| Problem | What to do |
|---|---|
| `/start` gets the last session wrong | Check that you pulled first. Correct the session log by hand, and the tester notes it. If it happens twice, we attach the session log to every `/start`. |
| A step fails or gives poor results | Run it once more and name the problem. If it fails again, do the step by hand: every step produces an ordinary file that a person can also write. |
| The assistant warns that a web page tried to instruct it | Do not follow the page. Tell the developer, who decides whether to drop the source. |
| Interview material, or a person's or customer's name, gets into a chat or file | Stop, and do not repeat it. Delete the chat, any related memory and the file. Write in the session log the same day that it happened, without the content, and tell the lecturer. If it was pushed, tell the repository owner at once: deleting the file is not enough to remove it from a public repository's history. |
| Claude asks permission to edit a file | Allow it for files in `logs/`, `sources/` and `chapters/`. Say no for `docs/` and `CLAUDE.md` unless the PM asked for the change. |
| The evidence log reaches 150 rows | Move the rows of finished chapters to an archive file outside the project. |

---

*This manual follows our decision of 26 Sep 2026 to run the assistant in Claude Code. The PRD, Technical Blueprint and Knowledge Architecture still describe a Claude Project, and the PM decides when to update them.*
