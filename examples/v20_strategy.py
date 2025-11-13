import yfinance as yf
# pip install yfinance
import pandas as pd
import numpy as np
from datetime import datetime, timedelta

def fetch_data(symbol, start, end=None):
    df = yf.download(symbol, start=start, end=end, progress=False)
    df = df[['Open','High','Low','Close','Adj Close','Volume']]
    df.rename(columns={'Adj Close':'AdjClose'}, inplace=True)
    return df

def detect_v20_streaks(df, pct_threshold=0.20, min_length=2):
    """
    Returns a list of streaks: each streak is tuple (start_idx, end_idx, low_range, high_range)
    """
    streaks = []
    n = len(df)
    i = 0
    while i < n-1:
        # start a potential green streak
        if df['Close'].iloc[i+1] > df['Close'].iloc[i]:
            j = i+1
            low = df['Low'].iloc[i]
            high = df['High'].iloc[i]
            # include the first candle in streak
            low = min(low, df['Low'].iloc[i])
            high = max(high, df['High'].iloc[i])
            # extend streak
            while j < n and df['Close'].iloc[j] > df['Close'].iloc[j-1]:
                low = min(low, df['Low'].iloc[j])
                high = max(high, df['High'].iloc[j])
                j += 1
            length = j - i
            if length >= min_length and (high / low - 1) >= pct_threshold:
                streaks.append((i, j-1, low, high))
            # move i to end of this streak
            i = j
        else:
            i += 1
    return streaks

def apply_v20_strategy(symbol, start, end=None, pct_threshold=0.20):
    df = fetch_data(symbol, start, end)
    df = df.dropna().reset_index()
    streaks = detect_v20_streaks(df, pct_threshold=pct_threshold)

    trades = []
    # For each found streak, mark range and then look for entry & exit
    for (s, e, low_range, high_range) in streaks:
        # After the streak ends at index e, we look forward for entry/exit
        for idx in range(e+1, len(df)):
            row = df.iloc[idx]
            price = row['AdjClose']
            date = row['Date']
            # Entry condition
            if price <= low_range:
                entry_date = date
                entry_price = price
                # Now look for exit after entry
                for exit_idx in range(idx+1, len(df)):
                    exit_row = df.iloc[exit_idx]
                    exit_price = exit_row['AdjClose']
                    exit_date = exit_row['Date']
                    if exit_price >= high_range:
                        trades.append({
                            'symbol': symbol,
                            'streak_start': df.iloc[s]['Date'],
                            'streak_end': df.iloc[e]['Date'],
                            'low_range': low_range,
                            'high_range': high_range,
                            'entry_date': entry_date,
                            'entry_price': entry_price,
                            'exit_date': exit_date,
                            'exit_price': exit_price,
                            'pct_gain': (exit_price/entry_price - 1) * 100
                        })
                        # stop after first exit
                        break
                break  # stop looking further for this streak after one trade
    return trades

if __name__ == "__main__":
    symbol = "AAPL"  # example
    start = "2021-01-01"
    trades = apply_v20_strategy(symbol, start, end=None, pct_threshold=0.20)
    for t in trades:
        print(t)
