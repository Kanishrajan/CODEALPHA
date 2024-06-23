import matplotlib.pyplot as plt
import yfinance as yf  # For data retrieval
from datetime import date, timedelta

class StockTracker:
    def __init__(self):
        self.stocks = {}

    def add(self, symbol):
        symbol = symbol.upper()
        try:
            # Use yfinance for data retrieval
            today = date.today()
            past = today - timedelta(days=365 * 20)
            stock_data = yf.download(symbol, start=past, end=today)
            self.stocks[symbol] = stock_data
            return True
        except (yf.DownloadError, ValueError):
            print(f"Error: Invalid symbol '{symbol}")
            return False

    def remove(self, symbol):
        symbol = symbol.upper()
        if symbol in self.stocks:
            del self.stocks[symbol]
            return True
        else:
            print(f"Error: Stock '{symbol}' not found.")
            return False

    def display(self):
        if not self.stocks:
            print("No stocks currently found.")
            return

        print("\n\t\t\t\t\t\t\tStock Tracker:")
        print("-" * 75)
        print("{:<15} {:>25} {:>25}".format("Symbol", "Current Price", "Performance (%)"))
        print("-" * 75)

        for symbol, data in self.stocks.items():
            current_price = data.iloc[-1]["Close"]
            # Calculate performance since the first closing price in the data
            start_price = data.iloc[0]["Close"]
            performance = ((current_price - start_price) / start_price) * 100
            print("{:<15} {:>25.2f} {:>25.2f}%".format(symbol, current_price, performance))
            print("-" * 75)
    def view(self, symbol):
        symbol = symbol.upper()
        if symbol not in self.stocks:
            print(f"Error: Stock '{symbol}' not found.")
            return

        data = self.stocks[symbol]
        plt.figure(figsize=(10, 5))
        plt.plot(data.index, data["Close"], label="Stocks Close Price")
        plt.xlabel("Date")
        plt.ylabel("Stocks Closing Price")
        plt.title(f"{symbol} Stocks' Closing Price (Past 20 Years)")
        plt.xticks(rotation=45)
        plt.grid(True)
        plt.legend()
        plt.tight_layout()
        plt.show()

tracker = StockTracker()

while True:
    print("\nStock Tracker Menu:")
    print("1. Add Stock")
    print("2. Remove Stock")
    print("3. Display Stocks")
    print("4. View Stock Graph")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == '1':
        symbol = input("Enter stock symbol: ").upper()
        added = tracker.add(symbol)
        if added:
            print(f"Stock '{symbol}' added successfully.")
    elif choice == '2':
        symbol = input("Enter stock symbol to remove: ").upper()
        removed = tracker.remove(symbol)
        if removed:
            print(f"Stock '{symbol}' removed successfully.")
    elif choice == '3':
        tracker.display()
    elif choice == '4':
        symbol = input("Enter stock symbol to view graph (from tracked stocks): ").upper()
        tracker.view(symbol)
    elif choice == '5':
        print("Exiting Stock Tracker.")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 5.")
