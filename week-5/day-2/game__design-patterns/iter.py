class Fibonacci:
    def __init__(self, count):
        self.count = count
        self.a = 0
        self.b = 1
        self.i = 0

    def __next__(self):
        if self.i >= self.count:
            raise StopIteration()

        self.i += 1
        self.a, self.b = self.a + self.b, self.a
        return self.b

    def __iter__(self):
        return self

for n in Fibonacci(5):
  print(n)

class Inventory:
    def __init__(self):
        self.items = []

    def add(self, item):
        self.items.append(item)

    def __iter__(self):
        return iter(self.items)

class Weapon:
        def strikewithweapon(self):
            self.strike()

class Sword(Weapon):
    def strike(self, opponent):
        opponent.hp -= self.damage

class Coin:
    def __init__(self):
        return "Coin: {}", format(self.value)


Inventory = Inventory()
inventory.add(Coin(5))
inventory.add(Coin(2))
inventory.add(Coin(1))
inventory.add(Sword())
