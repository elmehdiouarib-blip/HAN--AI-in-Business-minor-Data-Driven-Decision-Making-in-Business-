# Handbook Assistant · User guide

**From an SME's question → to advice → to a handbook page.**

The Handbook Assistant is an AI agent that researches an owner's question, keeps only evidence you have checked, and writes a handbook page that ends in five first steps for the owner. You make every decision by clicking a choice.

---

## Before you start (once per team member)

1. Install the **Claude desktop app**. You work in its **Code** tab.
2. Get the project from GitHub (GitHub Desktop: *File → Clone repository*). Keep it **outside OneDrive**.
3. Install the PDF reader, once: `python -m pip install -r requirements.txt`
4. In the Code tab, open the **`handbook-assistant`** folder.

## At the start of every session

- **Pull** the latest version from GitHub.
- Type **`/start`**. The agent tells you where the team stopped.

---

## Answer a question: one command

```
/answer Can AI help us write quotes faster?
```

Type the owner's question in plain words. The agent then takes you through **7 steps**.

### Step 1 · Understand the question
- **The AI:** rewrites the question as the owner would ask it, and suggests the handbook chapter it belongs to.
- **You choose:** *Yes, go on* or *Change the wording*; then the chapter, for example *Use cases (Recommended)*.

### Step 2 · Find sources
- **The AI:** searches the web in English and Dutch and lists 6–10 sources: statistics, research, government and trade press.
- **You choose:** tick the sources to read. Recommended ones are marked; vendor blogs are flagged.

### Step 3 · Read the sources and pull out claims
- **The AI:** saves each source as text (web page, PDF report, Word, slides or video transcript) and pulls out **claims**: one fact each, with the **exact sentence** from the source, and an English translation for Dutch sources.
- **You choose:** nothing. You see a table of claims, each with the agent's advice.

### Step 4 · Build the wiki *(human check 1)*
- **The AI:** tells you, per source, who wrote it, who paid for it, what it says, and where sources disagree. Then it files everything on topic pages, so the team can find it again.
- **You choose:** *All sources, as planned (Recommended)*, *Let me choose*, or *Not now*.

### Step 5 · Accept or reject the claims *(human check 2, the tester)*
- **The AI:** shows every claim with its advice: accept, or reject and why.
- **You choose:** *Accept my recommended set (Recommended)*, *Claim by claim*, *Accept all*, or *Not now*.
- **Claim by claim:** one question per source, with tick boxes. Unticked claims are rejected, and the agent asks why: *Second-hand*, *Vendor figure*, *Not in the source*, *Not relevant*, or your own reason.
- Only accept a claim you have checked against its source. Your name and the date are recorded.

### Step 6 · Write and check the page
- **The AI:** writes the handbook page on the course template, using **only accepted claims**, with a source after every fact. Then it checks the page against the seven quality criteria (C1–C7) and confirms that every quotation really is in its source.
- **You choose:** nothing. Read the page and the check report.

### Step 7 · The advice, and save
- **The AI:** shows the page's **five first steps for the owner**: the advice, each step saying who does it, at least one reversible.
- **You choose:** *Save and push to GitHub (Recommended)*, *Also make a Word version*, or *Stop here*.

**Result:** a handbook page in `chapters/`, its check report, an updated wiki, and everything saved on GitHub.

---

## After the page

1. **One reader outside the team** checks the page for jargon (criterion C4).
2. The **deployer** publishes it on the course site. The AI never publishes.

---

## Doing it one step at a time (optional)

| Step | Command |
|---|---|
| 2 · Find sources | `/search` |
| 3 · Read sources | `/add <links or files>`, then `/appraise` |
| 4 · Wiki | `/wiki` with the question's sources |
| 5 · Accept or reject | `/review` |
| 6 · Page and checks | `/draft`, then `/check` and `/lint` |
| 7 · Save | `/save`, then "commit and push" |

**Any time:** `/ask <question>` answers from the wiki, with a source after every claim.

---

## Four rules

1. **Never give it interview material.** No recordings, notes or names. It refuses audio and video files.
2. **Only claims the tester accepts go on a published page.**
3. **A vendor's own story is labelled as one.** It shows a product exists, not that it works.
4. **The GitHub repository is public.** Push nothing you would not put on the course site.

## If something goes wrong

| Problem | What to do |
|---|---|
| A new command is not recognised | Start a new session |
| A website or PDF cannot be read | The agent tries other ways; otherwise save the text by hand (see `wiki/README.md`) |
| The page check says BLOCKED | Accept or reject the remaining claims (step 5), then check again |
| The push to GitHub is refused | Someone pushed first: say "pull and push again" |
