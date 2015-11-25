class BankAccount:
    def __init__(self, account_name, balance = 0):
        self.balance = balance
        self.account_name = account_name

    def deposit(self, amount):
        self.balance += amount
        return self.balance

    def withdraw(self, amount):
        self.balance -= amount
        return self.balance
