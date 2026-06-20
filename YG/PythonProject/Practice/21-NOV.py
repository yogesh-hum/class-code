# -*- coding: utf-8 -*-
"""
Created on Fri Nov 21 18:20:15 2025

@author: Admin
"""

"""trading"""
# import yfinance as yf
# import pandas as pd
# from time import sleep
#
# symbol = "^NSEI"        # Correct symbol for NIFTY 50
# interval = "5m"
# window_short = 5
# window_long = 20
# refresh_time = 60       # seconds
#
#
# def get_data():
#     data = yf.download(symbol, period="7d", interval=interval)
#
#     if data.empty:
#         print("No data received! yfinance issue.")
#         return None
#
#     # Moving averages
#     data["SMA_short"] = data["Close"].rolling(window=window_short).mean()
#     data["SMA_long"] = data["Close"].rolling(window=window_long).mean()
#
#     return data
#
#
# def get_signal(row):
#     short_sma = row["SMA_short"].item() if hasattr(row["SMA_short"], "item") else float(row["SMA_short"])
#     long_sma = row["SMA_long"].item() if hasattr(row["SMA_long"], "item") else float(row["SMA_long"])
#
#     if pd.isna(short_sma) or pd.isna(long_sma):
#         return "WAIT (SMA not ready)"
#
#     if short_sma > long_sma:
#         return "CALL (UP)"
#     elif short_sma < long_sma:
#         return "PUT (DOWN)"
#     else:
#         return "HOLD"
#
#
#
# while True:
#     data = get_data()
#
#     if data is None:
#         sleep(5)
#         continue
#
#     # Fix: ensure latest_row is a Series, not DataFrame
#     latest_row = data.iloc[-1].squeeze()
#
#     signal = get_signal(latest_row)
#
#     print(f"Latest Signal at {latest_row.name}: {signal}")
#
#     sleep(refresh_time)
#

"""library management"""
#
# print('1 Add book')
# print('2 Update book')
# print('3 Delate book')

list=[]
print(list)
while(True):
    print('****BOOK list****')
    print('1 Add book')
    print('2 Update book')
    print('3 Delate book')
    choice = int(input("Enter your choice1:"))
    if(choice==1):
        add=str(input("enter add Book:"))
        list.append(add)
        print(list)
    elif choice==2:
        index = str(input('Enter Your Index Posistion:'))
        update = int (input('Enter Your BOOK to be update'))
        list[index] = update
        print(list)
    elif choice==3:
        dele =int(input("enter delete Book:"))
        list.remove(dele)
        print(list)