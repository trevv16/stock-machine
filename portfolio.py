import datetime


class Portfolio:
    def __init__(self, _name, birthYear):
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

    def record_transfer(self, transfer_type, _amount, _balance):
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

    def transfer_funds(self, is_deposit, amount):
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
            print('Change: $+', amount)
            print('New Cash Balance: $', self.cash_balance)
        else:
            amount *= -1
            self.cash_balance += amount
            history = self.record_transfer(
                "Withdrawal", amount, self.cash_balance)
            self.transfer_history.append(history)
            print('Change: $-', amount)
            print('New Cash Balance: $', self.cash_balance)

    # TODO: Add stock details to view
    def view_portfolio(self):
        """Displays the details of the portfolio
        """

        print("\n\n--------------------------------\n")
        print("{}'s Portfolio\n").format(self.name)
        print("Age: {}\n").format(self.age)
        print("--------------------------------\n")
        print("Cash Balance: {}\n").format(self.cash_balance)
        print("Total Equity: {}\n").format(self.total_equity)
        print("Account Value: {}\n").format(self.total_value)
        print("--------------------------------\n")
        print("         Stock History          \n")
        print("--------------------------------\n")
        # for stock in self.shares:
        #     print("stock 1")
        #     print("stock 2")
        #     print("stock 3")

    def view_transfer_history(self):
        """Displays the transfer history of the portfolio
        """

        print("\n\n--------------------------------\n")
        print("{}'s Portfolio\n").format(self.name)
        print("       Transaction History      \n")
        print("--------------------------------\n")
        for transfer in self.transfer_history:
            print("{}").format(transfer.transfer_type)
            print("Amount:  ${}").format(transfer.amount)
            print("Balance: ${}").format(transfer.balance)
            print("--------------------------------\n")

    def view_transaction_history(self):
        """Displays the transaction history of the portfolio
        """

        print("\n\n--------------------------------\n")
        print("{}'s Portfolio\n").format(self.name)
        print("       Transaction History      \n")
        print("--------------------------------\n")
        for transaction in self.transaction_history:
            print("{}").format(transaction.stock_name)
            print("{}").format(transaction.transaction_type)
            print("${}").format(transaction.stock_price)
            print("{} Shares").format(transaction.num_of_shares)
            print("Total:                   ${}").format(transaction.total)
            print("Total Stock Equity:      ${}").format(
                transaction.total_stock_equity)
            print("Total Profit/(Loss):     ${}").format(transaction.num_of_shares)
            print("--------------------------------\n")
