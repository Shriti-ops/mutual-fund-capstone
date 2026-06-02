DATA QUALITY SUMMARY

1. Total datasets loaded: 10

2. Missing Values:
   - Only 04_monthly_sip_inflows.csv contains missing values.
   - Column yoy_growth_pct has 12 missing values.
   - Likely due to insufficient prior-year data for YoY calculation.

3. AMFI Code Validation:
   - Fund Master Codes: 40
   - NAV History Codes: 40
   - Missing Codes: 0
   - Validation Status: Passed

4. Dataset Integrity:
   - No major missing values detected in remaining datasets.
   - All required columns are present.
   - Data types appear consistent.

5. Live NAV API:
   - Successfully fetched NAV data for:
     - HDFC Top 100 Direct
     - SBI Bluechip
     - ICICI Bluechip
     - Nippon Large Cap
     - Axis Bluechip
     - Kotak Bluechip

6. Overall Status:
   - Day 1 ingestion completed successfully.