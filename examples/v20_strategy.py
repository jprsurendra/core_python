import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# -----------------------------
# SETTINGS
# -----------------------------
# TICKER = "AAPL"            # example: "AAPL", "INFY.NS", "^NSEI", "BTC-USD"
'''
Yahoo Finance uses different ticker symbols for Indian stocks.
You must append the “.NS” suffix (for NSE India) or “.BO” (for BSE India).
| Exchange     | Example             | Format |
| ------------ | ------------------- | ------ |
| NSE (India)  | Infosys → `INFY.NS` | `.NS`  |
| BSE (India)  | Infosys → `INFY.BO` | `.BO`  |
| NASDAQ (USA) | Apple → `AAPL`      | none   |
| NYSE (USA)   | IBM → `IBM`         | none   |
| ------------ | ------------------- | ------ |
'''
TICKER = "AKZOINDIA.NS"            # example: "AKZOINDIA", "Akzo Nobel India Limited", "NSE""
START_DATE = "2023-01-01"
END_DATE = "2025-01-01"

# -----------------------------
# FETCH DATA
# -----------------------------
df = yf.download(TICKER, start=START_DATE, end=END_DATE)

# Handle missing Adj Close
if "Adj Close" in df.columns:
    df["Price"] = df["Adj Close"]
else:
    df["Price"] = df["Close"]

# -----------------------------
# V20 STRATEGY (20 EMA CROSS)
# -----------------------------
df["EMA20"] = df["Price"].ewm(span=20, adjust=False).mean()

# Generate buy/sell signals
df["Signal"] = np.where(df["Price"] > df["EMA20"], 1, 0)
df["Position"] = df["Signal"].diff()

# -----------------------------
# BACKTEST LOGIC
# -----------------------------
initial_balance = 100000
balance = initial_balance
position = 0

for i in range(1, len(df)):
    if df["Position"].iloc[i] == 1:   # Buy Signal
        position = balance / df["Price"].iloc[i]
        balance = 0
    elif df["Position"].iloc[i] == -1:  # Sell Signal
        balance = position * df["Price"].iloc[i]
        position = 0

# Final portfolio value (if holding)
if position > 0:
    balance = position * df["Price"].iloc[-1]

profit_pct = ((balance - initial_balance) / initial_balance) * 100

# -----------------------------
# RESULTS
# -----------------------------
print("Strategy: V20")
print(f"Ticker: {TICKER}")
print(f"Start Date: {START_DATE}  End Date: {END_DATE}")
print(f"Final Portfolio Value: ${balance:,.2f}")
print(f"Total Return: {profit_pct:.2f}%")

USD_TO_INR = 84.5  # you can update this as per current rate
balance_in_inr = balance * USD_TO_INR
print(f"Final Portfolio Value: ₹{balance_in_inr:,.2f}")
print(f"Total Return: {profit_pct:.2f}% (converted from USD)")

# -----------------------------
# PLOT
# -----------------------------
plt.figure(figsize=(12,6))
plt.plot(df.index, df["Price"], label="Price", alpha=0.8)
plt.plot(df.index, df["EMA20"], label="EMA20", linestyle="--")

plt.scatter(df.loc[df["Position"] == 1].index,
            df.loc[df["Position"] == 1]["Price"],
            marker="^", color="g", label="Buy Signal", alpha=1)

plt.scatter(df.loc[df["Position"] == -1].index,
            df.loc[df["Position"] == -1]["Price"],
            marker="v", color="r", label="Sell Signal", alpha=1)

plt.title(f"V20 Strategy on {TICKER}")
plt.legend()


