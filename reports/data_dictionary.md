# Data Dictionary

## 01_fund_master.csv

| Column        | Data Type | Description                   |
| ------------- | --------- | ----------------------------- |
| amfi_code     | INTEGER   | Unique mutual fund identifier |
| scheme_name   | TEXT      | Name of mutual fund scheme    |
| fund_house    | TEXT      | Asset Management Company      |
| category      | TEXT      | Fund category                 |
| sub_category  | TEXT      | Fund sub-category             |
| risk_category | TEXT      | Risk classification           |


## 02_nav_history.csv

| Column    | Data Type | Description            |
| --------- | --------- | ---------------------- |
| amfi_code | INTEGER   | Mutual fund identifier |
| date      | DATE      | NAV date               |
| nav       | REAL      | Net Asset Value        |


## 07_scheme_performance.csv

| Column            | Data Type | Description                  |
| ----------------- | --------- | ---------------------------- |
| amfi_code         | INTEGER   | Mutual fund identifier       |
| return_1yr_pct    | REAL      | One-year return percentage   |
| return_3yr_pct    | REAL      | Three-year return percentage |
| return_5yr_pct    | REAL      | Five-year return percentage  |
| expense_ratio_pct | REAL      | Expense ratio percentage     |


## 08_investor_transactions.csv

| Column             | Data Type | Description                 |
| ------------------ | --------- | --------------------------- |
| investor_id        | TEXT      | Unique investor identifier  |
| transaction_date   | DATE      | Date of transaction         |
| amfi_code          | INTEGER   | Mutual fund identifier      |
| transaction_type   | TEXT      | SIP, Lumpsum, or Redemption |
| amount_inr         | REAL      | Transaction amount in INR   |
| state              | TEXT      | Investor state              |
| city               | TEXT      | Investor city               |
| city_tier          | TEXT      | Tier classification         |
| age_group          | TEXT      | Investor age category       |
| gender             | TEXT      | Investor gender             |
| annual_income_lakh | REAL      | Annual income in lakhs      |
| payment_mode       | TEXT      | Mode of payment             |
| kyc_status         | TEXT      | KYC verification status     |
