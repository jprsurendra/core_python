import yfinance as yf
import pandas as pd

# --- Configuration ---
TICKER = "AKZOINDIA.NS"     # Example: AKZOINDIA.NS
START_DATE = "2017-01-01"
END_DATE = "2025-11-01"
CSV_FILE = f"{TICKER.replace('.', '_')}_data_{START_DATE}_to_{END_DATE}.csv"

# --- Step 1: Download data ---
df = yf.download(TICKER, start=START_DATE, end=END_DATE)

# Keep only needed columns in desired order
df = df[["Close", "High", "Low", "Open", "Volume"]]

# Reset index so Date becomes a column
df.reset_index(inplace=True)

# Ensure correct column order
df = df[["Date", "Close", "High", "Low", "Open", "Volume"]]

# --- Step 2: Save in the exact format you specified ---
df.to_csv(CSV_FILE, index=False)

print(f"✅ Data saved successfully to {CSV_FILE}")
print(df.head())

# --- Step 3: Read data back cleanly ---
df2 = pd.read_csv(CSV_FILE, parse_dates=["Date"])

print("\n✅ Data read from file:")
print(df2.head())
