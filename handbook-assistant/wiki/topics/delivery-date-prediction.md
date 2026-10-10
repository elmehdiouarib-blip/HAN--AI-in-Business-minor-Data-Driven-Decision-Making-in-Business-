# Delivery-date prediction

**Sub-questions:** E4, I4, I3 · **Last updated:** 10 Oct 2026, by /wiki

## What we know
### Accepted
- Comparable case: a study of two German make-to-order manufacturers, producing in batches of 1 to 10,000 pieces for a global market, tested machine learning to predict delivery dates. [C029, S008]
- Comparable case: predicting the date at the quote stage lowered the risk of late delivery, but its prediction error was 35% higher than the planning department's later estimate. [C030, S008]
- Comparable case: the customer's desired delivery date was the most valuable input. [C031, S008]
- Comparable case: knowing realistic dates early helps avoid rush orders, which makes the planned schedule more reliable. [C032, S008]
- Comparable case: once all steps were scheduled, unforeseen changes left an error that neither the model nor the planning department could correct. [C037, S008]
- Comparable case: sales estimated delivery times from experience, adding a large buffer. [C033, S008]
- Comparable case: the model used ERP data covering July 2019 to March 2022, with 16,361 orders. [C035, C036, S008]

### Unchecked (not evidence yet)
- With only customer-order data, the model added around 50% relative error; adding knowledge of the production system reduced that to around 35%. [S008, unchecked]
- Replenishment times and procurement did not significantly affect the quality of the prediction in either case. [S008, unchecked]

## How it fits together
Interpretation: the method works best with years of order history and knowledge of bottlenecks. A machine builder with few, large orders should start with a simple estimate and a person deciding. [C030, C036, C037]

## Debates
- None recorded.

## Open gaps
- Unknown: the partner firm's order count and which fields its ERP system holds.
- Unknown: any documented result in food-processing machinery.

## Related pages
- [Data readiness](data-readiness.md) · [What SMEs use AI for](what-smes-use-ai-for.md)

## Sources
- [S008 · Rokoss et al.](../source-notes/S008-rokoss-delivery-time-ml-2024.md)
