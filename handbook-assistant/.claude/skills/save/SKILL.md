---
name: save
description: Ends the session. Writes a new entry at the top of the session log so the next session can resume.
disable-model-invocation: true
allowed-tools: Read, Edit, Write
---

# /save: close the session

1. Add a new entry at the **top** of `logs/session-log.md` (below the title), in this format:

   ```
   ## <date> · <chapter> · <who ran the session>
   - **Done:** …
   - **Decisions (and why):** …
   - **Open questions:** …
   - **Next step:** …
   - **Evidence rows changed:** …
   - **Minutes spent:** …
   ```
2. Keep it short: at most eight lines.
3. Show the entry, and remind the team to share the updated folder (commit and push to our GitHub repository, or let the shared folder sync).

Never write interview content, names of people or customer names into the log.
