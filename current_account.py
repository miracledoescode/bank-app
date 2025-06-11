from account import Account

class CurrentAccount(Account):
    def __init__(self, balance):
        Account.__init__(self, balance)

currentAccount = CurrentAccount(1000)
currentAccount.deposit(300)
print(currentAccount.balance)  # Output: 1300
