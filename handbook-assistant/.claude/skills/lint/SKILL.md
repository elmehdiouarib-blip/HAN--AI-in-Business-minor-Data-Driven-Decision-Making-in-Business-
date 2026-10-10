---
name: lint
description: Health check of the wiki and the evidence log against the saved sources, including a check that every quotation is really in its source. Reports problems; with "fix", repairs only the mechanical ones.
disable-model-invocation: true
argument-hint: "<leave empty to report, or 'fix' to also repair links, index and upgrades>"
allowed-tools: Read, Write, Edit, Glob, Grep
---

# /lint $ARGUMENTS

1. Read `wiki/index.md`, `wiki/log.md`, every page in `wiki/topics/`, `wiki/organisations/`, `wiki/source-notes/` and `wiki/answers/`, `logs/evidence-log.md`, and the saved texts in `sources/` that the pages and rows cite.
2. **Quotation check.** For every passage in quotation marks on a wiki page, and every "Exact passage" in the evidence log, search the cited saved text in `sources/` for that exact wording (use Grep with the literal text; ignore differences in line breaks and spacing only). Report each passage that is not found, and each source that has no saved text to check against.
3. Report, with the page and the line concerned:
   a. lines of fact with no citation;
   b. `[C###, S###]` lines whose claim is not `accepted` now, or is cited with the wrong source ID;
   c. `[S###, unchecked]` lines whose numbers, dates or names cannot be found in the saved source text;
   d. unchecked lines that an accepted claim now covers (ready to upgrade);
   e. "Interpretation:" lines that cite nothing;
   f. disagreements between pages that are not recorded under "Debates";
   g. broken links; orphan pages (not in the index, or linked from no other page); wrong counts in the index;
   h. source notes with a missing field (address, date, author, publisher, who paid, format, what was read, chosen by); accepted claims not yet in the wiki; ingested sources without a source note;
   i. sub-questions (E1–E5, I1–I5) with no accepted claims: the gaps, each with a suggested search.
4. If a page holds something that looks like interview material, or a name of a person or customer, stop. Give only the page and line, do not repeat or summarise it, and tell us to remove it.
5. Verdict: **CLEAN**, or **NEEDS FIXING** with the number of quotation misses and of problems per type (a–i).
6. Save the report as `wiki/lint-report.md` (replace the previous one), with today's date at the top, and add a line at the top of the list in `wiki/log.md`.

**With `fix`:** after the report, repair only type g (links, index entries and counts) and type d (replace the unchecked line with the accepted claim, as `/wiki` sync does). List each repair in the report and the log. Never change a quotation or what a fact says, resolve a debate or delete a line: the tester decides those, through `/wiki` or by hand.
