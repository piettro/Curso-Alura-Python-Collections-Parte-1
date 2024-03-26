from operator import attrgetter
from functools import total_ordering

names = ["Guilherme", "Daniela", "Paulo"]
print(sorted(names))

@total_ordering
class SalaryAccount:
    def __init__(self, code):
        self._code = code
        self._money = 0
    
    def deposit(self, value):
        self._money += value
        
    def __str__(self):
        return "[Code {} Money {}]".format(self._code, self._money)
    
    def __eq__(self, other):
        if type(other) != SalaryAccount:
            return False
        return self._code == other._code and self._money == other._money

    def __lt__(self, other):
       if self._money != other._money:
            return self._money < other._money
       
       return self._code < other._code

account_guilherme = SalaryAccount(17)
account_guilherme.deposit(500)

account_daniela = SalaryAccount(3)
account_daniela.deposit(1000)

account_paulo = SalaryAccount(133)
account_paulo.deposit(510)

accounts = [account_guilherme, account_daniela, account_paulo]

for account in accounts:
    print(account)

for account in sorted(accounts, key=attrgetter("_money","_code")):
    print(account)

for account in sorted(accounts):
    print(account)