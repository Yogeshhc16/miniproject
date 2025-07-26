import yfinance as yf
import matplotlib.pyplot as plt
import pandas as pd
import csv

# Hardcoded stock prices for simple investment calc
stock_prices = {
    "AAPL": 150,
    "TSLA": 700,
    "GOOGL": 2800,
    "AMZN": 3400,
    "MSFT": 290,
    "TATA":300,
    "FLIP":1200
}

def get_user_input():
    stock_name = input("Enter stock symbol (e.g., AAPL, TSLA, GOOGL): ").upper()
    quantity = int(input("Enter the number of shares: "))
    return stock_name, quantity

def calculate_investment(stock_name, quantity):
    if stock_name in stock_prices:
        price_per_share = stock_prices[stock_name]
        total_investment = price_per_share * quantity
        return total_investment
    else:
        print(f"Warning: {stock_name} price not found in hardcoded list. Investment value can't be calculated.")
        return None

def fetch_live_data(stock_name, period="6mo", interval="1d"):
    print(f"Fetching live data for {stock_name}...")
    stock = yf.Ticker(stock_name)
    df = stock.history(period=period, interval=interval)
    if df.empty:
        print("Error: No data fetched. Check the stock symbol and your internet connection.")
        return None
    return df

def plot_stock_data(df, stock_name):
    plt.figure(figsize=(12,6))
    plt.plot(df.index, df['Close'], label="Close Price", color="blue")
    plt.plot(df['Close'].rolling(window=20).mean(), label="20-day SMA", color="green")
    plt.plot(df['Close'].rolling(window=50).mean(), label="50-day SMA", color="red")
    plt.title(f"{stock_name} Price Chart with Moving Averages")
    plt.xlabel("Date")
    plt.ylabel("Price (USD)")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()

def display_indicators(df):
    latest_close = df['Close'][-1]
    sma_20 = df['Close'].rolling(window=20).mean()[-1]
    sma_50 = df['Close'].rolling(window=50).mean()[-1]
    volume = df['Volume'][-1]
    daily_change_pct = df['Close'].pct_change()[-1] * 100

    print("\nFinancial Indicators:")
    print(f"Latest Close Price: ${latest_close:.2f}")
    print(f"20-day SMA: ${sma_20:.2f}")
    print(f"50-day SMA: ${sma_50:.2f}")
    print(f"Volume: {volume}")
    print(f"Daily Change: {daily_change_pct:.2f}%")

    return {
        "Latest Close Price": latest_close,
        "20-day SMA": sma_20,
        "50-day SMA": sma_50,
        "Volume": volume,
        "Daily Change (%)": daily_change_pct,
    }

def save_to_txt(stock_name, quantity, investment, indicators, filename="stock_investment.txt"):
    with open(filename, 'w') as file:
        file.write(f"Stock Symbol: {stock_name}\n")
        file.write(f"Number of Shares: {quantity}\n")
        if investment is not None:
            file.write(f"Total Investment: ${investment:.2f}\n")
        file.write("\nFinancial Indicators:\n")
        for key, val in indicators.items():
            if isinstance(val, float):
                file.write(f"{key}: {val:.2f}\n")
            else:
                file.write(f"{key}: {val}\n")
    print(f"Results saved to {filename}")

def save_to_csv(stock_name, quantity, investment, indicators, filename="stock_investment.csv"):
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Stock Symbol", "Number of Shares", "Total Investment"])
        investment_val = f"{investment:.2f}" if investment is not None else "N/A"
        writer.writerow([stock_name, quantity, investment_val])
        writer.writerow([])
        writer.writerow(["Indicator", "Value"])
        for key, val in indicators.items():
            if isinstance(val, float):
                writer.writerow([key, f"{val:.2f}"])
            else:
                writer.writerow([key, val])
    print(f"Results saved to {filename}")

def main():
    stock_name, quantity = get_user_input()

    investment = calculate_investment(stock_name, quantity)
    if investment is not None:
        print(f"\nTotal investment based on hardcoded price: ${investment:.2f}")

    df = fetch_live_data(stock_name)
    if df is not None:
        indicators = display_indicators(df)
        plot_stock_data(df, stock_name)

        save_option = input("\nDo you want to save the results? (yes/no): ").lower()
        if save_option == 'yes':
            file_format = input("Which file format? (txt/csv): ").lower()
            if file_format == 'txt':
                save_to_txt(stock_name, quantity, investment, indicators)
            elif file_format == 'csv':
                save_to_csv(stock_name, quantity, investment, indicators)
            else:
                print("Invalid format. Results not saved.")
        else:
            print("Results not saved.")

if __name__ == "__main__":
    main()