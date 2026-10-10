---
name: check
description: Checks the latest chapter draft against quality criteria C1–C7 and lists any sentence without an accepted source. Reports only.
disable-model-invocation: true
argument-hint: "<draft file in chapters/, or leave empty for the newest>"
allowed-tools: Read, Write
---

# /check $ARGUMENTS

1. Open the draft **$ARGUMENTS**, or the newest `*-draft-*.md` in `chapters/`.
2. Check it against C1–C7 from the Research Proposal (§4), one by one: PASS or FAIL, with the reason and the sentence concerned.
3. List every factual sentence that has no source ID, or that is not supported by an `accepted` row of that source in `logs/evidence-log.md` (a matching source ID alone is not enough). Also list any sentence that cites the wiki or is marked "unchecked".
4. Verdict: **BLOCKED** if C2, C3 or C7 fails, otherwise **READY FOR TESTER**.
5. Save the report as `chapters/<same name>-check.md`.

Do not rewrite the draft. The tester confirms the report and opens at least three cited sources.
