from account import Account

class SavingsAccount(Account):
	def __init__(self, balance, withdrawal_limit=500000):
		Account.__init__(self, balance)
		self.withdrawal_limit = withdrawal_limit
	
	def deposit(self, amount):
		if amount > 0:
			self.balance += amount
	
	def withdraw(self, amount):
		if 0 < amount <= self.withdrawal_limit and amount <= self.balance:
			self.balance -= amount
			return True
		return False
