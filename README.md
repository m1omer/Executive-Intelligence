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

By leveraging this dataset, the project aligns with actual enterprise BI workflows and demonstrates skills that translate directly to consulting, strategy, and executive-facing analytics roles.


## Live Tableau Dashboards

- [**Executive Intelligence Dashboard**](https://public.tableau.com/views/telcosimulatore/ExecutiveDashboard?:language=en-US&:sid=&:redirect=auth&:display_count=n&:origin=viz_share_link)  
  A top-level executive summary of customer churn metrics, lifetime value, and contract risk segmentation.

- [**Revenue Risk and Retention Strategy Simulator**](https://public.tableau.com/views/telcosimulatore2/SimulatorDashboard?:language=en-US&:sid=&:redirect=auth&:display_count=n&:origin=viz_share_link)  
  A dynamic simulator to model saved revenue and net ROI based on retention spend — powered by logistic regression modeling and interactive parameters.


## Project Workflow 

```plaintext

1. Load IBM Raw Data
   • Source: IBM Cognos Analytics sample dataset

2. Clean & Engineer Features
   • Script: clean_telco_data.py
   • Add churn flag and estimate capped CLTV (CLTV_Est)

3. Predict Churn Probability
   • Notebook: churn_model_with_encoding.ipynb
   • Train logistic regression and generate PredictedChurnProb

4. Build Executive Dashboards
   • File: telcosimulator.twbx
   • Tool: Tableau
   • Structure:
     - **Executive Intelligence Dashboard** — Combines KPI Overview and Churn Risk Segmentation to highlight key performance drivers and customer risk segments.
     - **Revenue Risk & Retention Simulator** — Allows executives to model potential revenue saved and Net ROI based on varying retention spend scenarios.

5. Deliver Strategic Memo
   • File: strategy-memo.pdf *(coming soon)*
   • Brief includes:
     - Top strategic recommendations
     - Retention spend guidance
     - Simulated ROI outcomes
