# databricks-lakehouse-e2e
End-to-end data engineering lakehouse using Databricks

## High-Level Architecture

This project implements an **end-to-end data engineering lakehouse architecture on Databricks**, following the **Medallion (Bronze, Silver, Gold)** pattern.

![High Level Architecture](./Project_High_Level_Architecture.png)

### Architecture Overview

The platform is designed to reflect real-world enterprise data platforms where data moves through multiple layers with increasing levels of structure and business readiness.

### Source Layer
Source data is simulated using **Databricks Catalog Volumes**, representing data landing from external systems such as:
- Object storage (S3 / ADLS)
- Batch exports from operational databases
- Files delivered by upstream applications

### Bronze Layer (Raw)
- Ingests data directly from the source Volume
- Stores raw data
- No business transformations applied

### Silver Layer (Clean & Conformed)
- Cleans and standardises raw data
- Handles null values, whitespaces, and inconsistent formatting
- Applies deduplication and data quality rules
- Produces structured, analytics-ready datasets

### Gold Layer (Business-Ready)
- Contains curated datasets optimised for analytics
- Serves as the consumption layer for reporting and dashboards

### Analysis & Visualisation
- Gold layer tables are consumed for analysis and reporting

## Example Analysis – Product Category Contribution to Sales and Profitability (2013)

The Gold layer enables business-focused analysis by providing curated, aggregated metrics.  
An example analysis was performed to evaluate **product category contribution to sales and profitability for the year 2013**.

![Prd_Cat_Sales_Profit](./Prd_Cat_Sales_Profit.png)

### Key Insights

- **Bikes dominate overall performance**, generating over **40M in total sales** and approximately **18.3M in profit**, making it the primary revenue and profit driver.
- **Accessories outperform Clothing in profitability**, despite lower total sales. Accessories generate around **1.5M in profit**, driven by a relatively higher margin compared to cost.
- **Clothing is the weakest performing category**, with the **lowest total sales and lowest profit (≈471K)** among all categories.
- Although Clothing shows a **similar average sales per order** to Accessories, its overall profitability is significantly lower, indicating inefficiencies in pricing, cost structure, or product mix.

### Business Interpretation

- The **Bikes category** represents a stable and high-impact segment and should continue to be a core focus.
- The **Accessories category** demonstrates strong margin potential and may benefit from increased investment or targeted growth strategies.
- The **Clothing category is underperforming** and requires further investigation into:
  - Pricing strategy
  - Cost optimisation
  - Supplier or production costs
  - Marketing effectiveness

### Outcome

This analysis highlights how **Gold layer datasets enable actionable business insights**, supporting data-driven decision-making across product strategy, pricing, and profitability optimisation.
