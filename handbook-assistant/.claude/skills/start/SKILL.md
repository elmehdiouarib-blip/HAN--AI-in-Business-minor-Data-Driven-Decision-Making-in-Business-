---
name: start
description: Resume work. Reads the session log and evidence log and says where the team stopped and what comes next.
disable-model-invocation: true
---

# /start: resume where we stopped

1. Read the newest entry at the top of `logs/session-log.md`.
2. Read `logs/evidence-log.md` and count the rows per status (proposed / accepted / rejected) for the current chapter.
3. Reply in at most five lines:
   - what we did last session,
   - the open decisions,
   - how many claims are accepted for this chapter,
   - the next step.
4. Ask which chapter and sub-questions we work on today.

Do not search, draft or change any file in this step.
