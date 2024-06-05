import yfinance as yf
class StockPortfolio:
    def __init__(self):
        self.stocks = {}
    def add_stock(self, symbol, quantity):
        if symbol in self.stocks:
            self.stocks[symbol] += quantity
        else:
            self.stocks[symbol] = quantity
        print(f"Added {quantity} shares of {symbol} to the portfolio.")
    def remove_stock(self, symbol, quantity):
        if symbol in self.stocks:
            if self.stocks[symbol] > quantity:
                self.stocks[symbol] -= quantity
                print(f"Removed {quantity} shares of {symbol} from the portfolio.")
            elif self.stocks[symbol] == quantity:
                del self.stocks[symbol]
                print(f"Removed all shares of {symbol} from the portfolio.")
            else:
                print("Error: Not enough shares to remove.")
        else:
            print("Error: Stock not found in portfolio.")
    def get_portfolio(self):
        return self.stocks
    def track_performance(self):
        total_value = 0
        for symbol, quantity in self.stocks.items():
            stock = yf.Ticker(symbol)
            price = stock.history(period="1d")['Close'].iloc[-1]
            value = price * quantity
            total_value += value
            print(f"{symbol}: {quantity} shares @ ${price:.2f} = ${value:.2f}")
        print(f"Total portfolio value: ${total_value:.2f}")
def main():
    portfolio = StockPortfolio()
    while True:
        print("\nStock Portfolio Tracker")
        print("1. Add Stock")
        print("2. Remove Stock")
        print("3. View Portfolio")
        print("4. Track Performance")
        print("5. Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            symbol = input("Enter stock symbol: ").upper()
            quantity = int(input("Enter quantity: "))
            portfolio.add_stock(symbol, quantity)
        elif choice == '2':
            symbol = input("Enter stock symbol: ").upper()
            quantity = int(input("Enter quantity: "))
            portfolio.remove_stock(symbol, quantity)
        elif choice == '3':
            stocks = portfolio.get_portfolio()
            for symbol, quantity in stocks.items():
                print(f"{symbol}: {quantity} shares")
        elif choice == '4':
            portfolio.track_performance()
        elif choice == '5':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")
if __name__ == "__main__":
    main()
