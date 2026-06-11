Bluestock Mutual Fund Analytics Capstone
Project Overview

This project provides an end-to-end analytics solution for mutual fund data using python,SQLite,JupyterNotebook, and Power BI.
 The project covers:

 1.Data Ingestion and Validation
 2.Data Cleaning and SQL Database Creation
 3.Exploratory Data Analysis(EDA)
 4.Fund Performance Analytics
 5.Dashboard Development with Power BI
 6.Advanced Analytics and Risk Metrics
 7.Interactive Dashboards
 8. Final Report and Presentation

 Technologies used
    - Python
    - SQLite
    - Jupyter Notebook
    - Power BI
    - Pandas
    - Matplotlib
    - Seaborn
    - SQLAlchemy
    - Git & GitHub

    Project Structure
    CAPSTONE_PROJECT
    |
    - data/
    |-- raw/ (original data files)
    |-- processed/ (cleaned data files)
    |
    notebooks/
    |-- EDA_Analysis.ipynb
    |-- Performance_Analytics.ipynb
    |-- Advanced_Analytics.ipynb
    |
    reports/
    |-- var_cvar_report.csv
    |-- rolling_sharpe_chart.png
    |-- alpha_beta.csv
    |-- cagr_comparison.csv
    |
    dashboard/
    |-- bluestock_mf_Dashboard.pbix
    |-- Mutual_Fund_Performance.pbix
    |
    |-- recommender.py
    |-- data_ingestion.py
    |-- data_cleaning.py
    |-- load_to_sqlite.py
    |-- requirements.txt
    |-- README.md
   
   Dataset Descriptions

   Fund Master Dataset
   Contains scheme information including:

   1.Scheme Name
   2.Fund House
   3.Category
   4.Benchmark
   5.Expense Ratio
   6.Launch Date

   NAV History Dataset

   Contains historical Net Asset Value data:

   1.Amfi Code    
   2.Date
   3.NAV

   Used for return and risk calculations.

   Investor Transactions Dataset
   Contains investor activity:

   1.Investor ID
   2.Transaction Date
   3.Amount Invested
   4.Transaction Type
   5.State
   6.Age group 
   7.Payment Mode

   Used for investor behaviour and SIP analysis.

   Benchmark Indices Dataset

   Contains benchmark market index performance data used for alpha ,beta ,and tracking error calculations.

   ---------------------------------------------------------------------------------------------------------

   Setup Instructions

   1.Clone Repository
   git clone https://github.com/Shriti-ops/mutual-fund-capstone.git
   cd mutual-fund-capstone

   2. Create a Virtual Environment
   ---bash
   python -m venv venv
   ---
   
   3.Activate the Virtual Environment

   ---bash
   venv\Scripts\activate
   ----

   4.Install Dependencies
   ---bash
   pip install -r requirements.txt
   ---

   How to Run the ETL
   1.Data Ingestion
 python data_ingestion.py
   2.Data Cleaning
 python data_cleaning.py
   3.Load Data into SQLite
 python load_to_sqlite.py

   How to open the Dashboard

   1.Open Power BI Desktop.
   2.Navigate to:
   dashboard/bluestock_mf_dashboard.pbix
   3.Open the PBIX file.

    Key Analyses
     
    Performance Metrics

    1.CAGR
    2.Alpha
    3.Beta
    4.Sharpe Ratio
    5.Sortino Ratio
    6.Tracking Error
    7.Maximum Drawdown
    
    Risk Metrics

    1.Value at Risk (VaR)
    2. Conditional Value at Risk (CVaR)

    Advanced Analytics

    1.Investor Cohort Analysis
    2.SIP Continuity Analysis
    3.Fund Recommender System
    4.Portfolio Concentration Analysis(HHI)

    Dashboard Pages

    1.Industry Overview
    2.Fund Performance 
    3.Investor Analytics
    4.SIP & Market Trends

    Deliverables

    1.Advanced_Analytics.ipynb
    2.Power BI Dashboards
    3.Dashboard PDF
    4.Recommendation Engine
    5.Risk Reports


    Author
    Shriti Sharma

