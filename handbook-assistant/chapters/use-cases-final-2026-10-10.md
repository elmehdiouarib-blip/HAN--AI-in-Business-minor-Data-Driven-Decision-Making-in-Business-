# What do firms like mine use AI for, and which use is worth trying first?

*Handbook page 2 · AI use cases at SMEs · Team 08 · 10 Oct 2026*

## The question, for this kind of SME

You build food-processing machines to order, with 50 to 249 staff. Handbook page 1 showed that the gap that matters most is knowing your own delivery-date performance.

**Your question:** what do firms like mine actually use AI for, what pays off, and which one use should we try first?

This page answers sub-questions **E4** (AI applications with documented results in build-to-order manufacturing) and **I4** (the best first planning problem, and the data it needs).

## The translation

**What firms use AI for today: mostly the office.** Of Dutch firms that use AI, 35% use it for marketing or sales [S002]. 32% use it for administration or management tasks, such as risk assessment, selecting applicants, translation or planning [S002]. 18% use it for production or service processes [S002], and only 4% for logistics [S002]. EU manufacturers that use AI do so mostly for marketing and sales (30.41%) and administration (27.05%) [S003]. Small firms use AI for production processes far less than large firms: 19.02% against 33.46% of firms that use AI [S003].

**Mostly off-the-shelf.** In the OECD's 2026 survey, SMEs kept taking up off-the-shelf AI tools, but strategic, targeted and secure integration into their operations remained uneven [S006].

**What is promised.** Vendor's own story (PayPal): AI agents can automate tasks such as reordering inventory, sending invoices, updating financial records and preparing compliance reports [S007]. The Asian Productivity Organization recommends four AI strategies for SME manufacturers: predictive maintenance and visual quality inspection, digital twins, human-in-the-loop operations, and federated learning [S009]. Interpretation: these describe what could be done, not what has been shown to pay off. The OECD's survey findings above are more cautious than the vendor's promise.

**What pays off: the evidence is thin.** Unknown: our search found no documented, measured case of AI planning at a Dutch SME machine builder. What firms do instead: Dutch SME manufacturers increasingly choose small, feasible steps over large programmes [S005].

**The closest documented result to your problem.** Comparable case: a study of two German make-to-order manufacturers, producing in batches of 1 to 10,000 pieces for a global market, tested machine learning to predict delivery dates [S008]. Predicting the date at the quote stage lowered the risk of late delivery, but its prediction error was 35% higher than that of the planning department's later estimate [S008]. The customer's desired delivery date was the most valuable input [S008]. Knowing realistic dates early helps avoid rush orders, which makes the plan more reliable [S008]. But once all steps were scheduled, unforeseen changes left an error that neither the model nor the planners could correct [S008].

**Our pick: a realistic delivery date at the quote.** Interpretation: it answers the gap from page 1, it targets the problem you started with, and it can start small.

## Illustrative use case (CRISP-DM)

**A realistic delivery date at the quote**, taken through the six steps of CRISP-DM.

1. **Business understanding.** The goal is to promise dates you can keep. Success measure: the share of orders delivered on the promised date, compared with the baseline from page 1, and fewer rush orders. Interpretation: agree a stop rule at the start, for example stop if the estimates are not better than the planner's after three months.
2. **Data understanding.** You need your order history: the customer's desired date, the date you promised, the actual delivery date, the route through the factory, and any outside work. Comparable case: one of the German firms used data from its ERP system (the software that holds orders and planning) covering July 2019 to March 2022 [S008]. That data set held 16,361 orders, and the firm completes about 300 customer orders a week [S008]. **Be honest about your data.** Interpretation: a machine builder that ships a handful of large machines a month has far fewer orders, probably too few for a machine-learning model at first. Unknown: how many orders and which fields your ERP system holds.
3. **Data preparation.** Clean the dates and link each order to its engineering changes and supplier delays.
4. **Modelling.** Interpretation: start simple. Use a rule of thumb or an average based on your own history, and try machine learning only when enough history exists.
5. **Evaluation.** For three months, compare the estimate, the planner's date and the real date. Judge both accuracy and lateness. Comparable case: the early estimate was less accurate than the planners' but lowered the risk of late delivery [S008].
6. **Deployment.** The planner sees the estimate as advice. A person sets the date and tells the customer.

## Recommended tooling

Evidence not found: no accepted source compares planning tools for build-to-order SMEs. Interpretation: start with an ERP export and a spreadsheet. Look at advanced planning or AI tools only once you have a baseline. When you talk to vendors, ask for references from machine builders with delivery figures from before and after, and treat their answers as the vendor's own story.

## Responsible AI & trust

- **Which data may leave the firm.** Order and customer data stay inside the firm while you build the estimate. If you later use a vendor's cloud tool, agree in writing what the vendor may do with your data: AI Act users must make agreements with suppliers [S004].
- **Where a person decides.** AI only advises; the planner commits the date. Comparable case: unforeseen changes left errors that no model could correct [S008].
- **Staff.** Process innovation, and using AI with employees involved from the start, are the key [S005]. Interpretation: involve the planner and sales from step 1.
- **The rules that apply.** AI Act users must check whether an application falls under the law, be transparent with customers and train staff [S004]. For SMEs using generative AI, the AI Act usually means limited risk, with light obligations mainly about transparency [S004]. Unknown: whether a planning tool that sets delivery dates falls into a higher risk class; check the legal text.

## First five steps for an owner

All five can start within 30 days.

1. **Choose this use case** and name the planner as its owner. *(owner, in week 1)*
2. **Start from page 1's baseline:** the on-time share and the top reasons for misses. *(planner, in weeks 1–3)*
3. **For the next 10 quotes,** write the planner's date and a simple estimate based on your history side by side, then compare both with the real date later. *(planner with sales, from week 2)* **Reversible:** a paper exercise; no system changes and no customer sees it.
4. **Ask two planning-software vendors** for references from machine builders, with delivery figures from before and after. *(owner, in week 3)*
5. **Write down** what data a vendor may access, and that a person always sets the delivery date. *(office manager, in week 4)*

## Sources

| ID | Source | Supports | Who says it and why credible | Limitation |
|---|---|---|---|---|
| S002 | CBS, *Bedrijven gebruiken AI vaakst voor marketing of verkoop*, 12 Dec 2025 | C008–C011 | Statistics Netherlands, the official statistics office | Self-reported; all sectors; provisional |
| S003 | Eurostat, *Use of artificial intelligence in enterprises*, Dec 2025 | C015, C016 | The EU statistical office | EU totals |
| S004 | KVK, *Ondernemers zetten nauwelijks stappen rond Europese AI-wetgeving*, 11 Sep 2025 | C039, C040 | Netherlands Chamber of Commerce | Summary of the law, not the legal text |
| S005 | FME et al., *Mkb-maakindustrie zet digitaliseringsstappen*, 14 Apr 2026 | C023, C042 | Sector bodies with Fontys | Sample size not stated; Brabant focus |
| S006 | OECD, *Empowering SMEs in the age of AI*, 13 Apr 2026 | C025 | OECD; survey of over 2,000 SMEs | Abstract only; non-representative |
| S007 | OECD Cogito blog, *Agentic AI for Small Business Growth* (author: PayPal), 16 Sep 2025 | C026 | A vendor's head of government relations, on an OECD blog | Vendor's own story: shows a product idea exists, not that it works |
| S008 | Rokoss et al., *Delivery time determination using machine learning in small batch production*, 2024 | C029–C032, C035–C037 | Peer-reviewed, open-access study | Two German firms, not food-processing machinery |
| S009 | Asian Productivity Organization, *Leveraging AI for Smart Manufacturing in SMEs*, 2026 | C038 | Intergovernmental productivity body | Description only; guidance, not results |

## What our platform drafted, and what we checked

- **Drafted by the Handbook Assistant (Claude)** on 10 Oct 2026, from evidence-log claims C008, C009, C010, C011, C015, C016, C023, C025, C026, C029, C030, C031, C032, C035, C036, C037, C038, C039, C040 and C042, all accepted by the tester.
- **Rejected by the tester:** C027 and C028, second-hand survey figures in a vendor's blog post. The OECD original is to be appraised later.
- **Checked by the assistant:** every exact source passage behind these claims was compared word for word with the saved source text and the live web page.
- **Field research and desk research.** Every claim on this page rests on desk research. None rests on field research: the interview has not taken place (plan B).
- **What this page cannot tell the owner,** because the firm itself was not asked: how many orders it handles and what its ERP system records; which planning problem its own staff find most painful; and what it has already tried with AI.
- **Checked by the team (tester, 10 Oct 2026):** accepted every claim used on this page against its saved source; opened S003, S007 and S008 and found that the cited passages matched.
- **Dutch translations** of C008–C011, C023, C039, C040 and C042 confirmed by the team's Dutch-reading member (10 Oct 2026).
- **Still to do before publication:** a jargon check by one reader outside the team (C4).
