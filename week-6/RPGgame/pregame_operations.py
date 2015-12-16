import os
import random


class Character():
    def __init__(self, name, dexterity, health, luck):
        self.name = name
        self.dexterity = dexterity
        self.health = health
        self.luck = luck
        self.maxdexterity = 0
        self.maxhealth = 0
        self.maxluck = 0

    def enter_name(self):
        os.system('clear')
        self.name = input('\n>>Please enter a name for your hero: \n>>')
        print('\nYour hero will be called:')
        print('\n      ' + self.name + '\n\n')

    def roll_stats(self):
        os.system('clear')
        self.dexterity = random.randint(1, 6) + 6
        self.maxdexterity = self.dexterity
        self.health = random.randint(1, 6) + random.randint(1, 6) + 6
        self.maxhealth = self.health
        self.luck = random.randint(1, 6) + 6
        self.maxluck = self.luck

        print('\nSTATS rolled for ' + self.name + ':\n\n')
        print('   Dexterity: ' + str(self.dexterity))
        print('   Health:    ' + str(self.health))
        print('   Luck:      ' + str(self.luck))

    def potion_message(self):
        print('\nSelect one potion to take with youself: \n\n')

    def add_potion(self, potion):
        self.potion = potion
        print('\nYour selected potion:')
        print('\n      ' + self.potion + '\n\n')



character = Character('name', 0 , 0, 0)
