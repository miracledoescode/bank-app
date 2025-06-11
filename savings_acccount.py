from account import Account


class SavingsAccount(Account):
    limit = 1000  # Example limit for withdrawals

    def __init__(self, balance):
        Account.__init__(self, balance)

    def withdraw(self, amount):
        if amount < 10000:
            super().withdraw(amount)