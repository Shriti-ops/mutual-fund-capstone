import requests
import pandas as pd
import os


schemes = {
    "HDFC_Top100_Direct": 125497,
    "SBI_Bluechip": 119551,
    "ICICI_Bluechip": 120503,
    "Nippon_Large_Cap": 118632,
    "Axis_Bluechip": 119092,
    "Kotak_Bluechip": 120841
}
os.makedirs("data/raw/live_nav", exist_ok=True)

for fund_name, scheme_code in schemes.items():

    url = f"https://api.mfapi.in/mf/{scheme_code}"

    response = requests.get(url)

    if response.status_code == 200:

        data = response.json()

        nav_df = pd.DataFrame(data["data"])

        filename = f"data/raw/live_nav/{fund_name}.csv"

        nav_df.to_csv(filename, index=False)

        print(f"Saved: {filename}")

    else:
        print(f"Failed: {fund_name}")
