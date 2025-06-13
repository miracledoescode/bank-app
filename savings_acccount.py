from account import Account


class SavingsAccount(Account):
    def __init__(self, balance, limit):
        Account.__init__(self, balance)
        self.limit = limit

    def withdraw(self, amount):
        if amount < self.limit:
            super().withdraw(amount)