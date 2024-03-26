class BankAccount:
    def __init__(self, code):
        self.code = code
        self.money = 0

    def deposit(self, value):
        self.money += value

    def __str__(self) -> str:
        return f"Code: {self.code}, Money:{self.money}"
    
account_gui = BankAccount(15)
account_gui.deposit(500)
print(account_gui)

account_dani = BankAccount(10)
account_dani.deposit(200)
print(account_dani)

accounts = (account_gui, account_dani)
print(accounts)

for account in accounts:
    print(account)

accounts[0].deposit(500)

print(accounts[0])
print(account_gui)

user_gui = ('Guilherme',37,1981)
user_dani = ('Daniela',24,1994)
user_paulo = ('Paulo',35,1983)

users = [user_gui, user_dani, user_paulo]

for user in users:
    print(user)