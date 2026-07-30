
import pandas as pd

df = pd.read_csv("Nat_Gas (5).csv")

# Convert dates to datetime format
df["Dates"] = pd.to_datetime(df["Dates"], format="mixed")

# Create a dictionary for quick price lookup
price_dict = dict(zip(df["Dates"].dt.strftime("%Y-%m-%d"), df["Prices"]))



def price_storage_contract(
    injection_dates,
    withdrawal_dates,
    volumes,
    max_storage,
    inject_rate,
    withdraw_rate,
    storage_cost_per_month
):
    
    total_profit = 0

    for inj_date, wd_date, volume in zip(
        injection_dates,
        withdrawal_dates,
        volumes
    ):

        # Validate storage and rate constraints
        if volume > max_storage:
            raise ValueError("Volume exceeds maximum storage capacity.")

        if volume > inject_rate:
            raise ValueError("Injection rate exceeded.")

        if volume > withdraw_rate:
            raise ValueError("Withdrawal rate exceeded.")

        # Get prices
        buy_price = price_dict[inj_date]
        sell_price = price_dict[wd_date]

        # Calculate storage duration (months)
        months = (
            pd.to_datetime(wd_date).to_period("M")
            - pd.to_datetime(inj_date).to_period("M")
        ).n

        # Cash flows
        purchase_cost = buy_price * volume
        sale_revenue = sell_price * volume
        storage_cost = storage_cost_per_month * volume * months

        # Profit
        profit = sale_revenue - purchase_cost - storage_cost

        total_profit += profit

    return total_profit


injection_dates = [
    "2021-05-31",
    "2022-01-31"
]

withdrawal_dates = [
    "2021-10-31",
    "2022-06-30"
]

volumes = [
    1000,
    800
]

contract_value = price_storage_contract(
    injection_dates=injection_dates,
    withdrawal_dates=withdrawal_dates,
    volumes=volumes,
    max_storage=2000,
    inject_rate=1500,
    withdraw_rate=1500,
    storage_cost_per_month=0.05
)

print("Test Case 1 Contract Value =", round(contract_value, 2))



contract_value2 = price_storage_contract(
    injection_dates=["2021-03-31"],
    withdrawal_dates=["2021-09-30"],
    volumes=[500],
    max_storage=1000,
    inject_rate=1000,
    withdraw_rate=1000,
    storage_cost_per_month=0.03
)

print("Test Case 2 Contract Value =", round(contract_value2, 2))



contract_value3 = price_storage_contract(
    injection_dates=["2021-09-30"],
    withdrawal_dates=["2022-02-28"],
    volumes=[700],
    max_storage=1500,
    inject_rate=1000,
    withdraw_rate=1000,
    storage_cost_per_month=0.04
)

print("Test Case 3 Contract Value =", round(contract_value3, 2))
"""""
Natural Gas Storage Contract Pricing Model
Project Overview
This project develops a prototype pricing model for a natural gas storage contract. The model estimates the value of a contract by calculating the cash flows generated from buying (injecting) and selling (withdrawing) natural gas on specified dates. It is designed as a prototype that can be further validated and enhanced before being used for automated client pricing.

Pricing Logic
The pricing function calculates the net value of the storage contract by:

Purchasing natural gas on each injection date at the corresponding market price.
Selling the stored gas on each withdrawal date at the corresponding market price.
Calculating storage costs based on the volume of gas stored and the number of days it remains in storage.
Applying operational constraints such as:
Maximum storage capacity
Maximum injection rate
Maximum withdrawal rate
Summing the profit or loss from all injection and withdrawal transactions to determine the total contract value.
The contract value is calculated as:

Contract Value = Total Sale Revenue − Total Purchase Cost − Total Storage Cost

Assumptions
The following assumptions are made in this prototype:

Interest rates are assumed to be zero (no discounting of future cash flows).
There is no transportation delay between injection and withdrawal.
Market holidays, weekends, and bank holidays are ignored.
Commodity prices for the selected dates are known and provided as input.
Gas injected on a given date is withdrawn only on its corresponding withdrawal date.
Storage costs are charged at a constant daily rate per unit of gas.
The model validates injection rates, withdrawal rates, and storage capacity before pricing the contract.
Technologies Used
Python
Pandas
Output
The model returns the estimated net value of the natural gas storage contract based on the specified contract parameters and operational constraints.
"""