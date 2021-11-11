# in the_bank.py
class Account(object):
	ID_COUNT = 1
	def __init__(self, name, **kwargs):
		self.id = self.ID_COUNT
		self.name = name
		self.__dict__.update(kwargs)
		if hasattr(self, 'value'):
			self.value = 0
		Account.ID_COUNT += 1

	def transfer(self, amount):
		self.value += amount


class Bank(object):
	"""The bank"""
	def __init__(self):
		self.account = []

	def add(self, account):
		self.account.append(account)

	def transfer(self, origin, dest, amount):
		"""
		@origin: int(id) or str(name) of the first account
		@dest: int(id) or str(name) of the destination account
		@amount: float(amount) amount to transfer
		"""


	def fix_account(self, account):
		"""
		fix the corrupted account
		@account: int(id) or str(name) of the account
		@return: True if success, False if an error occured
		"""
		diclass = account.__dict__
		if len(diclass) % 2 == 0:
			print("odd number")
		for d in diclass.keys():
			if d[0] == "b":
				print("Name starts with b")

		if not "zip" in diclass.keys():
			return 1
		if not "addr" in diclass.keys():
			return 1