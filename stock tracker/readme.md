Stock Tracker — Python Mini Project

A Python-based tool to track stock performance, calculate investment value, and visualize price trends with moving averages (SMA).  
It supports both offline mode (with hardcoded stock prices) and online mode (fetching live data via the `yfinance` library).

Features

Calculate investment value** based on stock symbol and quantity entered by the user.

Plot closing price trends with 20-day and 50-day Simple Moving Averages (SMA).

View latest financial indicators:

Latest Close Price

20-day SMA

50-day SMA

Volume

Daily Percentage Change

Save reports in `.txt` or `.csv` format.

Works offline with hardcoded prices or online with live market data.


Technologies Used

Python 3

yfinance for stock data

Matplotlib for plotting

Pandas for data analysis

CSV module and file I/O for saving reports

How to Run

1. Make sure you have the required libraries installed:

pip install yfinance matplotlib pandas


2. Run the script:

python stock_tracker.py


3. Enter:

Stock symbol (e.g., AAPL, TSLA)

Number of shares

Choose to save results (optional)





