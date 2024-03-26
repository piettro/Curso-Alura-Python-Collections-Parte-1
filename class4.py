class accountSalary: 
    def __init__(self, code):
        self._code = code
        self._money = 0

    def deposita(self, money):
        self._money += money

    def __str__(self):
        return "[>>Code {} Saldo {}<<]".format(self._code, self._money)

    def __eq__(self, other):
        return self._code == other._code and self._money == other._money


account1 = accountSalary(37)
print(account1)

account2 = accountSalary(37)
print(account2)

accounts = [account1, account2]

print(account1 == account2)
print(account1 in accounts)
print(account2 in accounts) 
print(account1 != account2)
