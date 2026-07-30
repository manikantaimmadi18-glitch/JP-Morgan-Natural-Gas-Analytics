import pandas as pd
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d
from statsmodels.tsa.holtwinters import ExponentialSmoothing

df = pd.read_csv("Nat_Gas.csv")


df["Dates"] = pd.to_datetime(df["Dates"], format="%m/%d/%y")


df = df.sort_values("Dates")


plt.figure(figsize=(12,6))
plt.plot(df["Dates"], df["Prices"], marker="o")
plt.title("Historical Natural Gas Prices")
plt.xlabel("Date")
plt.ylabel("Price")
plt.grid(True)
plt.savefig("historical_prices.png")
plt.close()


# -----------------------------
# Holt-Winters Forecast
# -----------------------------
model = ExponentialSmoothing(
    df["Prices"],
    trend="add",
    seasonal="add",
    seasonal_periods=12
)

fit = model.fit(optimized=True)

# Forecast next 12 months
forecast = fit.forecast(12)

future_dates = pd.date_range(
    start=df["Dates"].iloc[-1] + pd.offsets.MonthEnd(),
    periods=12,
    freq="ME"
)

forecast_df = pd.DataFrame({
    "Dates": future_dates,
    "Prices": forecast.values
})

# Combine historical and forecast data
combined_df = pd.concat([df, forecast_df], ignore_index=True)



plt.figure(figsize=(12,6))
plt.plot(df["Dates"], df["Prices"], marker="o", label="Historical")
plt.plot(
    forecast_df["Dates"],
    forecast_df["Prices"],
    linestyle="--",
    marker="o",
    label="Forecast"
)

plt.figure(figsize=(12,6))

plt.plot(
    df["Dates"],
    df["Prices"],
    marker="o",
    linewidth=2,
    label="Historical Prices"
)

plt.plot(
    forecast_df["Dates"],
    forecast_df["Prices"],
    marker="o",
    linestyle="--",
    linewidth=2,
    color="red",
    label="Holt-Winters Forecast"
)

plt.title("Natural Gas Price Forecast")
plt.xlabel("Date")
plt.ylabel("Price")
plt.legend()
plt.grid(True)

plt.savefig("forecast_prices.png")
plt.show()
plt.close()