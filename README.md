# Executive-Intelligence (Telco Turnaround Simulator)


**Great strategy starts with clarity — not just data.**  

This project simulates how executives can use predictive insights, ROI modeling, and targeted actions to reverse business decline and drive smarter decisions.

It blends business intelligence, data science, and executive thinking into a strategic decision-support system designed to guide action, not just observation.

Built on IBM’s enterprise-grade customer dataset, the simulator empowers decision-makers to:
- Predict churn before it happens
- Simulate the ROI of targeted retention spend
- Identify high-value, at-risk segments
- Take action — not just analyze

While the dataset simulates a telecom provider, the strategic approach — churn prediction, CLTV analysis, and ROI modeling — applies broadly across subscription-driven industries.

So whether you’re in telecom, SaaS, or any subscription-driven business, this project shows how to connect insights to impact.

## Why the IBM Telco Dataset?

This project is built on the [IBM Telco Customer Churn dataset](https://www.ibm.com/docs/en/cognos-analytics/11.1.0?topic=samples-telco-customer-churn), originally released by **IBM** for use in their **Cognos Analytics enterprise BI platform**

This synthetic, enterprise-grade dataset was designed by IBM to mirror real-world customer, billing, and service patterns within a telecom provider.

✅ By leveraging this dataset, the project aligns with actual enterprise BI workflows and demonstrates skills that translate directly to consulting, strategy, and executive-facing analytics roles.


## Project Workflow 

📥 1. Load Raw Data (IBM Telco CSV)
   • Source: IBM Cognos sample dataset

🧼 2. Clean & Engineer Features
   • Script: clean_telco_data.py
   • Tasks:
     - Handle missing values
     - Create churn flag (1 = churned)
     - Estimate capped Customer Lifetime Value (CLTV_Est)

🧪 3. Score Churn Probability
   • Notebook: churn_model_with_encoding.ipynb
   • Tasks:
     - Label encode categorical variables
     - Train logistic regression model
     - Add PredictedChurnProb column
     - Save final enriched dataset → telco_turnaround_with_churn_scores.csv

📊 4. Build Executive Dashboard
   • File: dashboard.twbx *(coming soon)*
   • Tabs:
     - KPI Overview
     - Churn Risk Segmentation
     - ROI Simulator (with parameter slider)
     - Executive Summary

📄 5. Deliver Strategic Recommendations
   • File: strategy-memo.pdf *(coming soon)*
   • Output:
     - Executive summary
     - Top 3 strategic plays
     - Retention spend guidance + simulated ROI
