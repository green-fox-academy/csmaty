class GameCharacter:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage

    def print_status(self):
        if self.hp <= 0:
            print(self.name + ' is DEAD')
        else:
            print(self.name + '\'s HP is: ' + str(self.hp) + '.  His damage is: ' + str(self.damage))

    def drink_potion(self):
        self.hp += 10

    def strike(self, other):
        other.hp -= self.damage

class Cleric(Player):
    def heal (self, ally):
        ally.hp += 10

robot_robi = GameCharacter('Robot Robi', 120, 25)
fogonosz = GameCharacter('Nagy Rohadek', 100000000000000, 9000)
melkor = Cleric('Melkor', 1000, 80)

robot_robi.print_status()
fogonosz.strike(robot_robi)
robot_robi.print_status()

for i in range (3):
    robot_robi.strike(fogonosz)
    melkor.heal(fogonosz)
fogonosz.print_status()
