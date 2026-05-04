import yfinance as yf
import pandas as pd
import numpy as np
import mplfinance as mpf

# ----------------------------
# SETTINGS
# ----------------------------
SYMBOL = "TCS.NS"
START = "2017-02-01"
END = "2017-05-01"

print("Downloading Data...")
df = yf.download(SYMBOL, start=START, end=END)

# FIX: Flatten multi-index columns
df.columns = [c[0] if isinstance(c, tuple) else c for c in df.columns]

df.dropna(inplace=True)

# ----------------------------
# V20 BUY / SELL STRATEGY
# ----------------------------
buy_signal = np.full(len(df), np.nan)
sell_signal = np.full(len(df), np.nan)

buy_points = []
sell_points = []

for i in range(1, len(df)):
    prev = df.iloc[i - 1]
    curr = df.iloc[i]

    is_green_prev = bool(prev["Close"] > prev["Open"])
    is_green_curr = bool(curr["Close"] > curr["Open"])

    is_red_prev = bool(prev["Close"] < prev["Open"])
    is_red_curr = bool(curr["Close"] < curr["Open"])

    if is_green_prev and is_green_curr:
        buy_signal[i] = curr["Close"]
        buy_points.append((df.index[i], curr["Close"]))

    if is_red_prev and is_red_curr:
        sell_signal[i] = curr["Close"]
        sell_points.append((df.index[i], curr["Close"]))

# ----------------------------
# PREPARE SIGNAL PLOTS
# ----------------------------
ap = [
    mpf.make_addplot(buy_signal, type='scatter', marker='^',
                     markersize=100, color='green', label='BUY'),
    mpf.make_addplot(sell_signal, type='scatter', marker='v',
                     markersize=100, color='red', label='SELL'),
]

# ----------------------------
# SHOW CANDLESTICK CHART
# ----------------------------
mpf.plot(
    df,
    type='candle',
    style='yahoo',
    title=f"{SYMBOL} – V20 Buy/Sell Signals",
    ylabel="Price",
    addplot=ap
)

print("\nBUY SIGNALS:")
for d, p in buy_points:
    print(d.date(), "BUY @", p)

print("\nSELL SIGNALS:")
for d, p in sell_points:
    print(d.date(), "SELL @", p)
