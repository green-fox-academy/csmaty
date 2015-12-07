class Character():
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage
        pass

    def drink_potion(self):
        self.hp += 10

    def strike(self, other):
        other.hp -= 10

    def get_status(self):
        life_status = 'DEAD'
        if self.hp > 0:
            life_status = 'HP: ' + str(self.hp)
        return self.name + '\n' + life_status

    def print_status(self):
        print(self.get_status())
