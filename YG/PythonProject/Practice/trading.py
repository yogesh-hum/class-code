import yfinance as yf
import pandas as pd
from time import sleep
import pytz

# -----------------------
# Config
# -----------------------
symbols = ["^NSEI", "BTC-USD", "ETH-USD"]  # NIFTY + crypto list
interval = "1m"
window_short = 5
window_long = 20
refresh_time = 10 # seconds

# IST timezone
ist = pytz.timezone('Asia/Kolkata')

# -----------------------
# Functions
# -----------------------
def get_data(symbol):
    data = yf.download(symbol, period="7d", interval=interval, auto_adjust=True)
    if data.empty:
        print(f"No data received for {symbol}")
        return None

    # Moving averages
    data["SMA_short"] = data["Close"].rolling(window=window_short).mean()
    data["SMA_long"] = data["Close"].rolling(window=window_long).mean()
    return data

def get_signal(short_sma, long_sma):
    # Handle NaN
    if pd.isna(short_sma) or pd.isna(long_sma):
        return "WAIT (SMA not ready)"

    # SMA strategy
    if short_sma > long_sma:
        return "CALL (UP)"
    elif short_sma < long_sma:
        return "PUT (DOWN)"
    else:
        return "HOLD"

# -----------------------
# Main Loop
# -----------------------
while True:
    for symbol in symbols:
        data = get_data(symbol)
        if data is None:
            continue

        # Latest row (scalar safe)
        latest_row = data.tail(1).squeeze()

        # Extract SMA values safely
        short_sma = latest_row["SMA_short"]
        long_sma = latest_row["SMA_long"]

        # If still Series, convert to float
        if hasattr(short_sma, "item"):
            short_sma = short_sma.item()
        if hasattr(long_sma, "item"):
            long_sma = long_sma.item()

        # Get signal
        signal = get_signal(short_sma, long_sma)

        # Convert timestamp to IST
        latest_time_ist = latest_row.name.tz_convert(ist)

        print(f"{symbol} Latest Signal at {latest_time_ist}: {signal}")

    sleep(refresh_time)
