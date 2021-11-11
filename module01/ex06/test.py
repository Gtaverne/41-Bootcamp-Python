from the_bank import Account
from the_bank import Bank

acc = Account("acc", value=0, balancoire="")
bk = Bank()

bk.add(acc)

testacc= Account("acc", value=0, balancoire="")

print(acc.__dict__)

bk.fix_account(acc)
