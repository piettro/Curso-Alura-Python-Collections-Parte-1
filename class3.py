import numpy as np
import array as arr
from abc import ABCMeta, abstractmethod

class BankAccount:
    def __init__(self, code):
        self._code = code
        self._money = 0

    def deposit(self, value):
        self._money += value

    def __str__(self) -> str:
        return f"Code: {self._code}, Money:{self._money}"
    
    @abstractmethod
    def pass_month(self):
        pass

class AccountCorrente(BankAccount):
    def pass_month(self):
        self._money -= 2

class AccountSaving(BankAccount):
    def pass_month(self):
        self._money *= 1.01
        self._money -= 3

class AccountInvestment(BankAccount):
    pass

try:
    account15 = AccountInvestment(15)
except:
    pass

account16 = AccountCorrente(16)
account16.deposit(1000)

account17 = AccountSaving(17)
account17.deposit(1000)

accounts = [account16, account17]

for account in accounts:
    account.pass_month()
    print(account)

float_array = arr.array('d', [1,3.5])
print(float_array)

float_array_np = np.array([1,3.5])
print(float_array_np)