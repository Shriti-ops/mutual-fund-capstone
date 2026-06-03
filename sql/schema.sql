create table dim_fund (
    fund_id int primary key,
    amfi_code int unique,
    fund_house text,
    category text,
    sub_category text,
    risk_category text
;)
create table dim_date(
    date_id int primary key,
    full_date DATE
);
create table fact_nav (
    nav_id int primary key,
    amfi_code int,
    nav_date DATE,
    nav REAL,
    FOREIGN KEY (amfi_code) REFERENCES dim_fund(amfi_code)
);  
create table fact_transactions(
    transaction_id int primary key,
    invesror_id text,
    amfi_code int,
    transaction_date DATE,
    transaction_type text,
    amount_inr REAL,
    foreign key (amfi_code) references dim(amfi_code));
create table fact_performance (
    perf_id ingt primary key,
    amfi_code int,
    retrun_1yr-pct REAL,
    return_3yr_pct REAL,
    return_5yr_pct REAL,
    foreign key(amfi_code) references dim(amfi_code)
);
CREATE TABLE fact_aum (
    aum_id INTEGER PRIMARY KEY,
    amfi_code INTEGER,
    aum_cr REAL,
    FOREIGN KEY(amfi_code)
    REFERENCES dim_fund(amfi_code)
);
