class Warrior:
    def __init__(self):
        self.companions = []
        self.hp = 100

    def join(self, companion):
        self.companions.append(companion)

    def strike(self, opponent):
        opponent.inflict_damage(10)
        for companion in self.companions:
            companion.notify("strike", self)

    def inflict_damage(self, damage):
        self.hp -= damage
        self._notify_all("damage")
        """for companion in self.companions:
            companion.notify("damage", self)"""

    def heal(self, hp):
        self.hp += hp

    def _notify_all(self, type):
        for companion in self.companions:
            companion.notify(type, self)


class Healer():
    def notify(self, type, Warrior):
        if type == "damage":
            warrior.heal(10)

class Aide():
    if notify(self, type, Warrior):
        if type == "strike":
            opponent.inflict_damage(2)

class Curse:
    def notify(self, type, warrior):
        if type == "damage":
            warrior.heal(-10)

class Cheer:
    def notify(self, type, warrior):
        if type == "curse":
        print ("Hurray")

class CombatLine():
    if notify(self, type, Warrior):
        if type == "damage":
            print ("%s has damaged ") (Warrior)
    def natural_disiter()


rabbit = Warrior()
wolf = Warrior()
shaman = Healer()
ninjaturtle = Aide()

rabbit.join(shaman)
wolf.join(Cheer())

wolf.curse(rabbit)
wolf.strike(rabbit)
