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
