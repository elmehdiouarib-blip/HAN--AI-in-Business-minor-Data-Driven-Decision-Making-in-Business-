# S008 · Rokoss, Syberg, Tomidei, Hülsing, Deuse and Schmidt, Case study on delivery time determination using a machine learning approach in small batch production companies
- **Address:** https://link.springer.com/article/10.1007/s10845-023-02290-2
- **Published:** *Journal of Intelligent Manufacturing* 35, December 2024 (online earlier) · **Accessed:** 10 Oct 2026
- **Format:** web page (peer-reviewed journal article, open access, CC BY 4.0)
- **What was read:** whole article; relevant paragraphs from "Comparison: case study business characteristics", "Case study 1", "Discussion of results over both cases" and "Conclusion" copied below unchanged. Some sentences and paragraphs between them (on feature tables, SHAP values and research questions 3–4) are left out.
- **Who paid:** university research; see the article's "Funding" section (not copied)
- **Chosen by:** assistant, at the team's request (10 Oct 2026); developer to confirm
- **Translation:** none

**Scores** A 4 (peer-reviewed journal, university authors) · R 4 (2024) · S 5 (make-to-order manufacturers, delivery-date prediction from offer stage) · V 4 (open access; company data not public) · T 5 (method, data and limits described)

---

Comparison: case study business characteristics

Both examined companies are make-to-order (MTO) manufacturers based in Germany. The manufacturer behind case 1 produces order-specific rubber sealings. The manufacturer behind case 2 produces metallic parts for mechanical use cases. Both companies produce in batches between 1 and 10,000 pieces for a global market. Since the global shipping times vary widely depending on the level of urgency of the shipping and the shipping provider, all delivery dates in both cases are communicated ex works.

During the offer process, the sales department estimates delivery times based on experience, taking a large buffer time into the calculation. After receiving the customer order, along with CAD (Computer Aided Design) files describing the object details, the order gets confirmed and the details are forwarded to the process planning department. On average, the process planning department is able to estimate a delivery date using manufacturing execution systems and communicate it to the customer within 7 business days for case 1 and four business days for case 2. During this time, the process planning department verifies the CAD files sent by the customer, checks the availability of raw materials, and defines process details related to manufacturing. Decisions on utilized manufacturing methods and machines are finalized and then migrated into software files for production. Finally, the order is placed into the Enterprise Resource Planning (ERP) system and the theoretical delivery date is calculated. Overall, this planning process results in a high risk of the delivery date initially communicated in the order confirmation not being matched by the manufacturing capacities.

Case study 1
Business and data understanding

Data was fetched from the company’s Enterprise Resource Planning (ERP) system including the time frame from 07/23/2019 to 03/31/2022. Table 2 gives a short description of the raw data that has been processed.

The main data set on manufacturing orders contained 16,361 single orders involving 58,344 manufacturing steps. The manufacturer finalizes approximately 300 customer orders on a weekly basis. Orders from 1,630 different customers covered 7,620 different articles to be produced. The full data set contains ten tables counting 73 columns and 2,393,353 rows.

Discussion of results over both cases

As mentioned earlier, using the baseline prediction of the mean delivery time calculated on historical data results in significant error, leading to a R2 score of 0, which means that there is no correlation between prediction and reality. The same applies to the usage of the best approach utilizing the moving average of the delivery time. In both cases, the NRSME highlights the gain in prediction accuracy when different groups of information are included in the datasets. In both cases, the NRSME decreases when all available information is given as input to the machine learning model (feature set 3). However, the decrease in case 2 derives from a global delay of all orders. After the correction of this delay, the additional decrease in prediction error for both cases is below 10%. This indicates that after scheduling all processing steps, unforeseeable changes result in an error that can neither be corrected by the ML model, nor by the process planning department. If the prediction is made earlier in the process—before the customer order is confirmed or the offer sent out—using only customer order-related data (feature set 1), the prediction error increases compared to the delivery date determined by the process planning department. Without planned delivery times from the process planning department and domain knowledge-specific features (feature set 1), the ML model scores a RMSE that adds around 50% relative error. If domain knowledge-specific features are added (feature set 2), the additional error is reduced to around 35%. However, as the domain knowledge is based on historical data, and therefore it is known prior to the order, the delivery date prediction can be done before the order gets processed by the process planning department. Although this results in less risk of late delivery when confirming the customer order, the added uncertainty results in a higher prediction error. This demonstrates the importance of the knowledge about the performance of the production system. Knowing details about production system dynamics allows the early prediction of the delivery date. From a manufacturing management perspective, the early prediction of the delivery time before the customer order is confirmed has several positive impacts on the overall production performance. Early knowledge about realistic delivery dates helps avoiding rush orders. Fewer rush orders improve the reliability of the planned schedule which improves the stability of the overall production process. Assuming a more stable production process leads to less unpredictable delays. Fewer delays will eventually result in an even more precise delivery time prediction.

For both cases, the replenishment times and overall procurement processes did not have a significant impact on the quality of the predicted delivery time. Since procurement processes can significantly delay a production process, if raw materials are not in stock, further research needs to be undertaken to investigate the impact of procurement delays on the delivery time in real world scenarios.

Conclusion

1. Can delivery times be predicted earlier in the process in the same quality the process planning department provides?

Applying ML approaches in the initial offering process or just before confirming the customer order results in less risk of late delivery. However, the added uncertainty results in a higher prediction error of + 35%. Using ML approaches in process planning just before releasing the manufacturing order can help to further reduce the prediction error of the delivery time.

2. Which domain knowledge-specific features do improve the quality of the prediction?

For the machine learning prediction, domain knowledge is extremely valuable, as it helps reducing the model error significantly. In other words, historical knowledge about the performance of the manufacturing system increases the prediction accuracy. The SHAP values showed a high relevance for all features extracted according to the Hanovarian Supply Chain Model. The identification of the current range of the bottleneck system as well as external manufacturing processes and customer rank by quantity of orders showed a high impact on the prediction in both examined cases. However, results across both case studies also show that the specification of the desired delivery date is the most valuable feature for the prediction of delivery times, as it allows the model to distinguish whether to aim for the fastest possible delivery or the delivery in a certain time frame.

Overall, this research provides contribution to both academia and industry practice by addressing existing research gaps and providing a practical solution for delivery time prediction at the same time. The ability of machine learning to make predictions earlier in the process allows to define a delivery date at the time of the first offer. This can result in increased efficiency, lower costs for the process planning department, and ultimately it can represent a competitive advantage for manufacturing companies using this approach.

As this research is based on two cases, more examples are required to strengthen the observed results.
