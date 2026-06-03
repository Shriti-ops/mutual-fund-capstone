import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy import text

# Create SQLite database
engine = create_engine("sqlite:///bluestock_mf.db")

# Load datasets
fund_master = pd.read_csv("data/raw/01_fund_master.csv")
nav = pd.read_csv("data/processed/nav_history_clean.csv")
txn = pd.read_csv("data/processed/investor_transactions_clean.csv")
perf = pd.read_csv("data/processed/scheme_performance_clean.csv")

# Load into SQLite
fund_master.to_sql(
    "dim_fund",
    engine,
    if_exists="replace",
    index=False
)

nav.to_sql(
    "fact_nav",
    engine,
    if_exists="replace",
    index=False
)

txn.to_sql(
    "fact_transactions",
    engine,
    if_exists="replace",
    index=False
)

perf.to_sql(
    "fact_performance",
    engine,
    if_exists="replace",
    index=False
)


with engine.connect() as conn:

    dim_fund_count = conn.execute(
        text("SELECT COUNT(*) FROM dim_fund")
    ).scalar()

    fact_nav_count = conn.execute(
        text("SELECT COUNT(*) FROM fact_nav")
    ).scalar()

    fact_txn_count = conn.execute(
        text("SELECT COUNT(*) FROM fact_transactions")
    ).scalar()

    fact_perf_count = conn.execute(
        text("SELECT COUNT(*) FROM fact_performance")
    ).scalar()

print("\nROW COUNT VERIFICATION")
print("----------------------")

print(
    f"dim_fund: CSV={len(fund_master)} DB={dim_fund_count}"
)

print(
    f"fact_nav: CSV={len(nav)} DB={fact_nav_count}"
)

print(
    f"fact_transactions: CSV={len(txn)} DB={fact_txn_count}"
)

print(
    f"fact_performance: CSV={len(perf)} DB={fact_perf_count}"
)
print("Database loaded successfully.")