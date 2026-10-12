# Demo: from an owner's problem to advice

**Goal of the demo:** show, live, that the Handbook Assistant takes an owner's real problem and turns it into advice they can act on, with every claim traceable to a checked source and a person deciding at every gate.

**Time:** about 15 minutes · **Who:** one person types, one person narrates

---

## Before the demo (5 minutes, not shown)

1. Open the `handbook-assistant` folder in the Claude app's **Code** tab.
2. Get the latest version: **Pull** in GitHub Desktop, or `git pull`.
3. Have one new source ready to add live, for example the OECD 2026 report:
   `https://www.oecd.org/content/dam/oecd/en/publications/reports/2026/04/empowering-smes-in-the-age-of-ai_7f58652c/bf5a9816-en.pdf`
4. Open these in a second window, as backups if a live step is slow:
   - `Team08_9_Handbook_AI_Use_Cases.docx`: the finished page
   - `wiki/index.md`: the wiki
   - `logs/evidence-log.md`: the claims

---

## The demo in 10 steps

| # | Say | Type | The audience sees | It proves |
|---|---|---|---|---|
| 1 | "This is the owner's problem." | (show only) | The question: *delivery dates slip; can AI help, and what would it cost?* | We start from a real problem |
| 2 | "The agent remembers where we are." | `/start` | Last session, open decisions, next step | Memory between sessions |
| 3 | "It finds sources, in English and Dutch." | `/search E4 I4` | 6–10 candidates from CBS, Eurostat, OECD, research | Research, not guessing |
| 4 | "It reads any format, here a 36-page PDF." | `/add <the OECD address>` | The source saved as text, with who wrote it and what was read | Reads reports, slides, transcripts |
| 5 | "It pulls out claims, each with the exact sentence." | `/appraise S010` | Scored source; claims marked **proposed**, quotes word for word | Every claim keeps its evidence |
| 6 | "It pauses before it writes." | `/wiki S010`, then `go ahead` | What it plans to write; then the wiki pages, with disagreements under Debates | A wrong reading is caught early |
| 7 | "A person decides what counts." | `accept C043, C044` and `reject C045 because …` | Rows turn **accepted** or **rejected**, signed with name and date | Human in control |
| 8 | "Ask it anything, and see where the answer comes from." | `/ask what do we know about predicting delivery dates?` | Answer with a source after every claim; the log lists the pages read | Answers are traceable |
| 9 | "Now it writes the page." | `/draft use cases E4 I4` | A handbook page on the course template, with [S###] after every fact | From evidence to text |
| 10 | "And it checks itself." | `/check` and `/lint` | C1–C7 pass/fail; every quotation found in its source | Nothing invented |

**Finish on the advice:** open the page's **First five steps for an owner**. That is the answer to the owner's problem. For example: *for the next 10 quotes, write the planner's date and a simple estimate side by side* (reversible, no system change).

Source and claim numbers (S010, C043) will differ; use the ones the agent prints.

---

## If a step is slow

| Step | Show this instead |
|---|---|
| 3 Search | `sources/candidates-E4-I4-2026-10-10.md` |
| 5 Appraise | `logs/evidence-log.md`, for example row C030, the 35% result |
| 6 Wiki | `wiki/topics/delivery-date-prediction.md` |
| 9 Draft | `Team08_9_Handbook_AI_Use_Cases.docx` |
| 10 Check | `chapters/use-cases-draft-2026-10-10-check.md` and `wiki/lint-report.md` |

---

## The story in one line per stage

**Problem** (step 1) → **Evidence** (steps 3–5) → **Knowledge** (step 6) → **Human check** (step 7) → **Answer** (step 8) → **Page** (step 9) → **Quality check** (step 10) → **Advice** (five first steps)

---

## Moments worth pointing out

- **The vendor catch:** the OECD blog post was written by PayPal. The agent recorded it as a vendor's view, and the tester rejected its second-hand figures.
- **The summary catch:** a search summary said a study "halved the error". The paper says the opposite, and the exact-sentence rule caught it.
- **The line:** the agent refuses audio files, so interview recordings cannot get in. Try `/add meeting.mp3` to show it.

---

## Rules during the demo

- Use only published sources. **Never interview material.**
- The agent never publishes. Publishing on the course site stays with the deployer.
- To throw the demo away afterwards, say "undo the demo changes" **before** you commit. To keep the work, run `/save` and then "commit and push".
