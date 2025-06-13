from account import Account

class CurrentAccount(Account):
    def __init__(self, balance,):
        Account.__init__(self, balance)

    def deposit(self, amount):

       if amount >= 0:
           self.balance += amount

