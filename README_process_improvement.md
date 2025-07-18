# Order Fulfilment Process Improvement Case Study

This case study analyses the end‑to‑end **order fulfilment** process using the open **100 Sales Records** dataset.  Each record includes the region and country, product type, sales channel, order priority, **order date** and **ship date**, units sold and financial metrics【424531801079175†L0-L4】.  These fields allow us to calculate the **cycle time**—the number of days between when an order is placed and when it is shipped.

## Objective

* Map the current order fulfilment workflow and identify where delays occur.
* Measure cycle times across regions and highlight bottlenecks.
* Provide data‑driven recommendations to reduce cycle times and improve the process.

## Dataset Overview

The dataset contains 100 orders with the following relevant columns【424531801079175†L0-L4】:

- **Region / Country** – geographical origin of each order.
- **Item Type / Sales Channel / Order Priority** – product and logistics attributes.
- **Order Date** and **Ship Date** – dates used to compute cycle time.
- **Units Sold, Unit Price, Unit Cost, Total Revenue, Total Cost, Total Profit**【424531801079175†L0-L4】.

## Methodology

1. **Process Mapping:** The core workflow was visualised as three stages—**Order Received**, **Order Processed** and **Order Shipped**—with arrows illustrating the flow between steps.  See `process_flow.png` for the diagram.
2. **Data Preparation:**  Order and ship dates were converted to datetime and cycle time was calculated in days as the difference between the two dates.
3. **Exploratory Analysis:**  Cycle times were summarised overall and by region.  Histograms and bar charts were used to visualise the distribution and regional averages.  Outliers (orders with exceptionally long cycle times) were identified.
4. **Deliverables:**  In addition to the code and notebook, the project includes use‑case definitions, functional requirements, stakeholder analysis and a gap analysis to guide process improvements.

## Results

### Cycle‑Time Distribution

Most orders are shipped within 0–40 days, but there are several orders that take longer (up to 50 days).  The histogram in `cycle_time_distribution.png` shows that delays are spread across the range, indicating inconsistent fulfilment performance.

### Average Cycle Time by Region

| Region                               | Average Cycle Time (days) |
|--------------------------------------|---------------------------|
| **Asia**                             | ~28.7                     |
| **Central America & Caribbean**      | ~26.7                     |
| **North America**                    | ~25.7                     |
| **Australia & Oceania**              | ~24.3                     |
| **Middle East & North Africa**       | ~24.2                     |
| **Europe**                           | ~24.1                     |
| **Sub‑Saharan Africa**               | ~19.9 (lowest)            |

Asia experiences the **longest average cycle time** (~29 days), while Sub‑Saharan Africa has the **shortest** (~20 days).  The bar chart (`average_cycle_time_by_region.png`) visualises these differences.

### Longest Individual Cycle Times

The five longest orders have cycle times ranging from **45 to 50 days**, with the longest occurring in Sub‑Saharan Africa and several 47‑day orders in Asia and the Middle East.  These extreme cases highlight specific orders that require investigation.

## Analysis and Recommendations

* **Automate order processing:**  Manual hand‑offs between departments contribute to long cycle times.  Integrating order management and shipping systems will reduce delays.
* **Regional process review:**  Asia shows consistently high cycle times.  Investigate local shipping partners, customs procedures and warehouse practices to identify specific bottlenecks.
* **Set cycle‑time thresholds:**  Define target cycle times (e.g. 10 days) and implement alerts when orders approach the threshold so that teams can intervene proactively.
* **Standardise workflows:**  Document and standardise order processing steps across regions; ensure staff follow best practices.
* **Continuous monitoring:**  Use the dashboards and metrics produced in this project to monitor performance and drive ongoing improvements.

## Project Structure

- `sales_data.csv` – input dataset.
- `process_improvement_analysis.py` – analysis script that computes cycle times, summarises results and generates charts.
- `Process_Improvement_Case_Study.ipynb` – notebook with narrative and code.
- `cycle_time_distribution.png` & `average_cycle_time_by_region.png` – visualisations of cycle time metrics.
- `process_flow.png` – process flow diagram.
- `use_cases.md`, `requirements.md`, `stakeholder_analysis.md`, `gap_analysis.md` – process improvement deliverables.

This project demonstrates how simple date fields can be leveraged to measure performance and drive improvements in an order fulfilment process.  By mapping the workflow, quantifying delays and providing targeted recommendations, it showcases both analytical and business‑analysis skills.
