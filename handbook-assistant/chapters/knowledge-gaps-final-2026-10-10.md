# What do we not know yet about AI, and what should we find out first?

*Handbook page 1 · SME knowledge gaps · Team 08 · 10 Oct 2026*

## The question, for this kind of SME

You own or run a Dutch family firm that builds food-processing machines to order, with 50 to 249 staff, and you sell worldwide. Our working assumption, which we could not yet test with a firm: delivery dates slip when planning, suppliers and engineering changes collide. You hear that AI could help.

**Your question:** what do we not yet know about AI, and which gap should we close first before we spend money on it?

This page answers sub-questions **E3** (what Dutch manufacturing SMEs report as their main barriers to AI) and **I3** (what a firm like yours knows about its own delivery-date performance and planning data).

## The translation

**Firms your size are moving, but manufacturers lag.** AI use among Dutch firms with 50 to 250 staff rose from 20% in 2023 to 45% in 2025 [S002]. In Dutch industry, only 16% of firms used AI in 2025 [S002]. Across the EU, 30.36% of medium-sized firms used AI in 2025 [S003].

**The barriers firms name.** Among Dutch firms that considered AI but did not use it, 73% name lack of experience as the main reason [S002]. 49% name privacy [S002]. 42% name unclear legal consequences, such as liability for damage [S002]. The EU picture is the same: lack of expertise (70.89%), unclear legal consequences (52.52%) and privacy (48.83%) [S003]. In the OECD's 2026 survey, time constraints, maintenance costs and skills gaps held SMEs back [S006].

**The rules are a gap of their own.** Half of Dutch entrepreneurs do not know the EU AI Act, and only 7% are well informed [S004]. Among firms with 10 or more staff, 44% expect the AI Act to affect them [S004]. Four in ten entrepreneurs do not know whether it applies to them [S004].

**The deepest gap is inside the factory.** In 80% of the Dutch SME manufacturers surveyed, the use of data and sensors is not developed enough [S005]. 83% lack insight into which parts of their production process suit automation with AI [S005].

**What owners say they need, and what the evidence shows.** Owners of SME manufacturers say they mainly need concrete examples, practical step-by-step plans and help with investment choices [S005]. Interpretation: the evidence points to an earlier gap. Most firms do not yet know their own data and processes well enough to apply an example. That difference is the main finding of this page.

**Your own delivery dates (I3).** Unknown: we could not ask the firm what it knows about its own delivery-date performance; this is desk research. Comparable case: in two German build-to-order manufacturers, sales estimated delivery times from experience and added a large buffer [S008]. Their planning process gave a high risk that the date first promised would not match manufacturing capacity [S008]. Interpretation: a firm like yours probably faces the same gap. Do you measure how often you deliver on the promised date, and is that recorded in your ERP system (the software that holds your orders and planning)?

**The gap that matters most now.** Interpretation: knowing your own delivery-date performance and planning data. Without it you cannot choose an AI trial, and you cannot tell whether one worked.

## Illustrative use case (CRISP-DM)

**A delivery-date baseline: the first two steps of CRISP-DM**, the method for data projects in our course's chapter template. Handbook page 2 continues with the other steps.

1. **Business understanding.** The question: how often do we deliver on the promised date, and why do we miss? Success is a one-page baseline: the share of orders delivered on time, and the three most common reasons for a miss.
2. **Data understanding.** List what your ERP system already records for each order: order date, promised date, actual shipping date, engineering changes and supplier delays. Comparable case: one of the German firms used ERP data covering July 2019 to March 2022 [S008]. Unknown: whether your ERP records the promised date and the actual date for every order.

The remaining steps (preparing data, building a model, testing it and putting it to use) only make sense once this baseline exists. Handbook page 2 takes them further.

## Recommended tooling

Evidence not found: no accepted source compares tools for building this baseline. Interpretation: no AI is needed for this first step. An export from your ERP system into a spreadsheet is enough to count on-time deliveries and reasons for misses.

## Responsible AI & trust

- **Which data may leave the firm.** The baseline uses only your own order data, so keep it inside the firm. Privacy is one of the main reasons firms hold back from AI [S002]. Interpretation: do not paste customer names, drawings or prices into public AI chatbots.
- **The rules that apply.** The EU AI Act has been in force since 2024 and applies in full from 2026 [S004]. Users, not only developers, are responsible: they must check whether an application falls under the law, make agreements with suppliers, be transparent with customers and train staff [S004]. For SMEs using generative AI, the AI Act usually means limited risk, with light obligations mainly about transparency [S004]. Limitation: this is the Chamber of Commerce's summary, not the legal text.
- **Where a person decides.** Interpretation: the baseline describes the past. People still set every delivery date.
- **How staff use AI.** Unknown: we could not ask the firm how its staff use AI tools today.

## First five steps for an owner

All five can start within 30 days.

1. **Name one person** who owns the question "how reliable are our delivery dates?" *(owner, in week 1)*
2. **Export the last 12 months of orders** with promised and actual delivery dates into a spreadsheet, and note which fields are missing. *(planner or ERP key user, in weeks 1–2)* **Reversible:** a read-only export; nothing in the ERP system changes.
3. **Count on-time deliveries** and list the three most common reasons for a miss: engineering change, supplier or capacity. *(owner with the planner, in week 3)*
4. **Write a one-page rule** on which data may go into AI tools: no customer names, drawings or prices in public chatbots. *(office manager, in week 2)*
5. **Check the AI Act's user duties** against the AI tools your staff already use, and ask staff which tools those are. *(owner with the office manager, in week 4)*

## Sources

| ID | Source | Supports | Who says it and why credible | Limitation |
|---|---|---|---|---|
| S002 | CBS, *Bedrijven gebruiken AI vaakst voor marketing of verkoop*, 12 Dec 2025 | C002–C004, C006, C007 | Statistics Netherlands, the official statistics office; national survey | Self-reported; all sectors; 2025 figures provisional |
| S003 | Eurostat, *Use of artificial intelligence in enterprises*, Dec 2025 | C012, C014 | The EU statistical office; 157 000 firms surveyed | EU totals; no Dutch or sector split in these figures |
| S004 | KVK, *Ondernemers zetten nauwelijks stappen rond Europese AI-wetgeving*, 11 Sep 2025 | C017–C019, C039–C041 | Netherlands Chamber of Commerce, a public body | 651 respondents incl. self-employed; summary of the law, not the legal text |
| S005 | FME et al., *Mkb-maakindustrie zet digitaliseringsstappen*, 14 Apr 2026 | C020–C022 | Sector bodies (FME, Koninklijke Metaalunie) with Fontys | Sample size not stated; Brabant focus; press release only |
| S006 | OECD, *Empowering SMEs in the age of AI*, 13 Apr 2026 | C024 | OECD; survey of over 2,000 SMEs | Abstract only read; non-representative sample |
| S008 | Rokoss et al., *Delivery time determination using machine learning in small batch production*, 2024 | C033–C035 | Peer-reviewed, open-access study | Two German firms, not food-processing machinery |

## What our platform drafted, and what we checked

- **Drafted by the Handbook Assistant (Claude)** on 10 Oct 2026, from evidence-log claims C002, C003, C004, C006, C007, C012, C014, C017, C018, C019, C020, C021, C022, C024, C033, C034, C035, C039, C040 and C041, all accepted by the tester.
- **Checked by the assistant:** every exact source passage behind these claims was compared word for word with the saved source text and the live web page (41 of 41 found).
- **Field research and desk research.** Every claim on this page rests on desk research. None rests on field research: the interview has not taken place (plan B).
- **What this page cannot tell the owner,** because the firm itself was not asked: how reliable its delivery dates really are; which planning data its ERP system holds; how its staff use AI today; and what the firm itself says it needs.
- **Checked by the team (tester, 10 Oct 2026):** accepted every claim used on this page against its saved source; opened S002, S005 and S008 and found that the cited passages matched. Rejected C027 and C028 (not used on this page).
- **Dutch translations** of C002–C004, C006, C007, C017–C022 and C039–C041 confirmed by the team's Dutch-reading member (10 Oct 2026).
- **Still to do before publication:** a jargon check by one reader outside the team (C4).
