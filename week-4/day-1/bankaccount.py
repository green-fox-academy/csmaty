class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def pay(self, amount):
        self.balance -= amount

    def recieve(self, amount):
        self.balance += amount

    def printbalance(self):
        print('Balance of: ')
        print(self.name)
        print('is: ')
        print(self.balance)

    def transfer(self, other, amount):
        self.pay(amount)
        other.recieve(amount)

customer1 = BankAccount('Robi', 12000)
customer2 = BankAccount('Codewars Kata', 90000)
feri = BankAccount('Feri', 7000000)




customer1.recieve(3000)
customer2.pay(2500)
customer2.printbalance()
customer1.printbalance()


customer1.transfer(customer2, 2300)
customer1.printbalance()
