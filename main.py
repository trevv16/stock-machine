import importlib
import time
import datetime


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


class Portfolio:
    def __init__(self):
        self.name = None
        self.dobYear = None
        self.age = None
        self.cash_balance = 0.00
        self.total_equity = 0.00
        self.total_value = 0.00
        self.shares = []
        self.transfer_history = []
        self.transaction_history = []

    def setup(self, _name: "string", birthYear: "int"):
        self.name = _name
        self.dobYear = birthYear

        currYear = datetime.datetime.today().year
        self.age = currYear - birthYear
        self.cash_balance = 0.00
        self.total_equity = 0.00
        self.total_value = 0.00
        self.shares = []
        self.transfer_history = []
        self.transaction_history = []

    def record_transfer(self, transfer_type: "string", _amount: "float", _balance: "float"):
        """Records a transfer as a deposit or withdrawal and final balance.

        Args:
            transfer_type (string): Type of transfer "Deposit" or "Withdrawal"
            _amount (float): The amount of the transaction in dollars
            _balance (float): A dict with the details of the transaction including a timestamp

        Returns:
            (dict): The details of the transaction including a timestamp
        """

        transfer = dict()
        transfer['transfer_type'] = transfer_type
        transfer['amount'] = _amount
        transfer['balance'] = _balance
        transfer['timestamp'] = "11/12/2020"

        return transfer

    def get_cash_balance(self):
        """Returns the cash balance of the portfolio
        cash balance represents uninvested funds in the account

        Returns:
            (string): a string containing the cash balance as a fixed 2 digit decimal
        """
        return f"Cash Balance: ${self.cash_balance:.2f}"

    def make_transfer(self, is_deposit: "bool", amount: "float"):
        """Transfers between user's trading account and bank account,
        and records transaction details.

        Args:
            is_deposit (bool): Type of deposit "Deposit" True or "Withdrawal" False
            amount (float): The amount of the transaction in dollars
        """

        if (is_deposit):
            self.cash_balance += amount
            history = self.record_transfer(
                "Deposit", amount, self.cash_balance)
            self.transfer_history.append(history)
            print(f'Change: $+{amount:.2f}')
            print(f'New {self.get_cash_balance()}')
        else:
            amount *= -1.00
            self.cash_balance += amount
            history = self.record_transfer(
                "Withdrawal", amount, self.cash_balance)
            self.transfer_history.append(history)
            print(f'Change: $+{amount:.2f}')
            print(f'New {self.get_cash_balance()}')

    # TODO: Add stock details to view
    def view_portfolio(self):
        """Displays the details of the portfolio
        """

        print("\n\n--------------------------------")
        print(f"{self.name}'s Portfolio")
        print(f"Age: {self.age}")
        print("--------------------------------")
        print(f"Cash Balance:    ${self.cash_balance:.2f}")
        print(f"Total Equity:    ${self.total_equity:.2f}")
        print(f"Account Value:   ${self.total_value:.2f}")
        print("--------------------------------")
        print("         Stock History          ")
        print("--------------------------------")
        # for stock in self.shares:
        #     print("stock 1")
        #     print("stock 2")
        #     print("stock 3")

    def view_transfer_history(self):
        """Displays the transfer history of the portfolio
        """

        print("\n\n--------------------------------")
        print(f"{self.name}'s Portfolio")
        print("       Transaction History      ")
        print("--------------------------------")
        for transfer in self.transfer_history:
            print(f"{transfer.transfer_type}")
            print(f"Amount:  ${transfer.amount:.2f}")
            print(f"Balance: ${transfer.balance:.2f}")
            print("--------------------------------")

    def view_transaction_history(self):
        """Displays the transaction history of the portfolio
        """

        print("\n\n--------------------------------")
        print(f"    {self.name}'s Portfolio         ")
        print("         Transaction History      ")
        print("--------------------------------")
        for transaction in self.transaction_history:
            print(f"{transaction.stock_name}")
            print(f"{transaction.transaction_type}")
            print(f"${transaction.stock_price:.2f}")
            print(f"{transaction.num_of_shares} Shares")
            print(f"Total:                   ${transaction.total:.2f}")
            print(
                f"Total Stock Equity:      ${transaction.total_stock_equity:.2f}")
            print(f"Total Profit/(Loss):     ${transaction.num_of_shares:.2f}")
            print("--------------------------------")


# Start of main
# Saves portfolio instance in memory
main_portfolio = Portfolio()


def print_menu():
    # Dict to create the main menu
    main_menu = dict()
    main_menu["A"] = "View Portfolio"
    main_menu["B"] = "View Transfer History"
    main_menu["C"] = "View Transaction History"
    main_menu["D"] = "Make Transfer"
    main_menu["E"] = "Search Stock"
    main_menu["Q"] = "Quit"

    print("\n\n--------------------------------")
    print("       Stock Machine Menu      ")
    print("--------------------------------")
    for key in main_menu:
        print(key, main_menu[key])
    print("--------------------------------\n")

    eval_input()


def eval_input():
    user_input = input("Enter your choice: ")

    if (user_input.upper() == "A"):  # view portfolio
        main_portfolio.view_portfolio()
        print("\n\n--------------------------------")
        print(r"--------------------------------")
        time.sleep(3)
        print_menu()
    elif (user_input.upper() == "B"):  # view transfer history
        main_portfolio.view_transfer_history()
        print("\n\n--------------------------------")
        print(r"--------------------------------")
        time.sleep(3)
        print_menu()
    elif (user_input.upper() == "C"):  # view transaction history
        main_portfolio.view_transaction_history()
        print("\n\n--------------------------------")
        print(r"--------------------------------")
        time.sleep(3)
        print_menu()
    elif (user_input.upper() == "D"):  # make transfer
        transfer_type = input(
            "Enter deposit type: A. Deposit   B. Withdrawal ")
        transfer_amount = input("Enter transfer amount: $")
        transfer_amount = float(transfer_amount)

        if (transfer_type.upper() == "A"):
            main_portfolio.make_transfer(True, transfer_amount)
        else:
            main_portfolio.make_transfer(False, transfer_amount)

        print("\n\n--------------------------------")
        print(r"--------------------------------")
        time.sleep(3)
        print_menu()
    elif (user_input.upper() == "E"):  # search stock
        print("\n\n--------------------------------")
        print(r"--------------------------------")
        time.sleep(3)
        print_menu()
    elif (user_input.upper() == "Q"):  # quit
        pass
        print("\n\n--------------------------------")
        print(r"--------------------------------")
    else:
        print("There was an issue with your input try again.")
        print("\n\n--------------------------------")
        print(r"--------------------------------")
        time.sleep(1)
        print_menu()


def main():
    print("Welcome to the Stock Machine Command Line App.")
    print("Created by Trevor Njeru.")

    name = input("What is your name? ")
    dobYear = input("What year were you born? ")
    main_portfolio.setup(name, int(dobYear))

    print_menu()


if __name__ == "__main__":
    main()
