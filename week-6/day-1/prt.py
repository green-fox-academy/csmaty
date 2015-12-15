class Pirate():
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage
        self.rumcount = 0

    def drink_rum(self):
        self.rumcount += 1
    def hows_it_goin(self):
        response = 'Aargh' if (self.rumcount>=5) else 'Nothin\''
        print(response)

        # if self.rumcount >= 5:
        #     print('Aargh')
        # else:
        #     print('Nothin\'')


danny = Pirate('Danny', 100, 20)

danny.drink_rum()
danny.drink_rum()
danny.drink_rum()
danny.hows_it_goin()
danny.drink_rum()
danny.drink_rum()
danny.drink_rum()
danny.hows_it_goin()
