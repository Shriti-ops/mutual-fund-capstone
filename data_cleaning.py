import pandas as pd

nav = pd.read_csv("data/raw/02_nav_history.csv")

nav["date"] = pd.to_datetime(nav["date"])

nav = nav.sort_values(
    ["amfi_code", "date"]
)
nav = nav.drop_duplicates()
nav["nav"] = (
    nav.groupby("amfi_code")["nav"]
    .ffill()

)
nav = nav[nav["nav"] >0]
nav.to_csv(
    "data/processed/nav_history_clean.csv",
    index=False
)
print("NAV History cleaned successfully.")

txn = pd.read_csv(
    "data/raw/08_investor_transactions.csv"
)
txn["transaction_type"] = ( txn["transaction_type"].str.strip().str.upper()
)

txn["transaction_date"] = pd.to_datetime(txn["transaction_date"]
)
txn = txn[txn["amount_inr"] > 0]

print("\nKYC Status Values:")
print(txn["kyc_status"].unique())

txn.to_csv(
    "data/processed/investor_transactions_clean.csv",
    index= False
)
print("Investment transactions cleaned successfully.")

perf = pd.read_csv("Data/raw/07_scheme_performance.csv")

return_cols = [
    "return_1yr_pct",
    "return_3yr_pct",
    "return_5yr_pct"]

for col in return_cols:
    perf[col] = pd.to_numeric(
        perf[col],
        errors = "coerce"
    )
anomalies = perf[
    (perf["expense_ratio_pct"] <0.1)
    |
    (perf["expense_ratio_pct"] >2.5)

]
print("\nAnomalies in Expense Ratio:")
print(len(anomalies))

perf.to_csv(
    "data/processed/scheme_performance_clean.csv",index= False)
print("Scheme Performance cleaned successfully.")

files = [
    "01_fund_master.csv",
    "03_aum_by_fund_house.csv",
    "04_monthly_sip_inflows.csv",
    "05_category_inflows.csv",
    "06_industry_folio_count.csv",
    "09_portfolio_holdings.csv",
    "10_benchmark_indices.csv",
   
]
for file in files:
    df = pd.read_csv(f"data/raw/{file}")
    df = df.drop_duplicates()
    output_name = file.replace(".csv", "_clean.csv")
    df.to_csv(
        f"data/processed/{output_name}",
        index=False
    )
    print(f"created: {output_name}")
print("\nALL remaining processed files created successfully.")
