class Stock:
    def __init__(self, _company_name, _ticker_symbol):
        self.name = _company_name
        self.ticker = _ticker_symbol
        self.current_price = 0.00
        self.day_change = 0.00
        self.history = []

    def view_stock(self):
        """Displays the details of a stock
        """

        print("\n\n--------------------------------")
        print("--------------------------------")
        print("{}").format(self.name)
        print("{}").format(self.ticker)
        print("${:.2f}").format(self.current_price)
        print("${:.2f}").format(self.day_change)
        print("--------------------------------")
        print("--------------------------------")
        print("         Stock History          ")
        print("--------------------------------")
        for stock in self.history:
            print("{}").format(stock.date)
            print("Close Price:     ${:.2f}").format(stock.price)
            print("Day Change:      ${:.2f}").format(stock.day_change)
        print("--------------------------------")
