Stock Tracker — Python Mini Project

This Python project allows users to track stock performance, calculate their investment value, and visualize price trends with moving averages. It uses hardcoded stock prices for quick investment checks and also fetches live stock data using the yfinance library.

Features

Calculate investment based on user-entered stock and quantity

Plot closing price with 20-day and 50-day Simple Moving Averages (SMA)

View latest financial indicators: Close price, SMAs, volume, daily change

Save the report to .txt or .csv format

Works both offline (with hardcoded prices) and online (via live data)


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



Note:

Only a few stock prices are hardcoded (AAPL, TSLA, GOOGL, AMZN, MSFT,)

For other stocks, live data will be fetched via yfinance

Internet connection is required for live data fetching and plotting
