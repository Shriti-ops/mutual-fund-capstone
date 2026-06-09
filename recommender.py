import pandas as pd

performance = pd.read_csv(
    "data/processed/scheme_performance_clean.csv"
)

risk = "Low"

recommendations = (
    performance[
        performance["risk_grade"] == risk
    ]
    .sort_values(
        "sharpe_ratio",
        ascending=False
    )
    .head(3)
)

print(recommendations[
    [
        "scheme_name",
        "risk_grade",
        "sharpe_ratio",
        "return_3yr_pct"
    ]
])