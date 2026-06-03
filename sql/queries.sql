SELECT COUNT(*) AS total_funds
FROM dim_fund;

SELECT AVG(nav) AS average_nav
FROM fact_nav;

SELECT MAX(nav) AS highest_nav
FROM fact_nav;

SELECT MIN(nav) AS lowest_nav
FROM fact_nav;

SELECT
    transaction_type,
    COUNT(*) AS total_transactions
FROM fact_transactions
GROUP BY transaction_type;

SELECT AVG(amount_inr) AS avg_transaction_amount
FROM fact_transactions;

SELECT
    state,
    COUNT(*) AS total_transactions
FROM fact_transactions
GROUP BY state
ORDER BY total_transactions DESC;

SELECT
    amfi_code,
    expense_ratio_pct
FROM fact_performance
WHERE expense_ratio_pct < 1;

SELECT
    amfi_code,
    return_5yr_pct
FROM fact_performance
ORDER BY return_5yr_pct DESC
LIMIT 5;

SELECT
    AVG(return_1yr_pct) AS avg_1yr_return,
    AVG(return_3yr_pct) AS avg_3yr_return,
    AVG(return_5yr_pct) AS avg_5yr_return
FROM fact_performance;