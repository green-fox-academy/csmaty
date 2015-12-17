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
        self.weapon = 'Sword'
        self.armor = 'Leather Armor'
        self.potion = None

    def save_char_specs(self):
        specs = {'name': self.name, 'dexterity': self.dexterity,'health': self.health, 'luck': self.luck, 'weapon': self.weapon, 'armor': self.armor, 'potion': self.potion, 'maxdexterity': self.maxdexterity, 'maxhealth': self.maxhealth, 'maxluck': self.maxluck}
        return specs

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

    def add_potion(self, potion):
        os.system('clear')
        self.potion = potion
        print('\nYour selected potion is:')
        print('\n      ' + self.potion + '\n\n')

    def display_character(self):
        print('\n   Your Player: ' + self.name + '\n\n')
        print('   Dexterity: ' + str(self.dexterity))
        print('   Health:    ' + str(self.health))
        print('   Luck:      ' + str(self.luck))
        print('   Inventory: ' + str(self.weapon) + ', ' + str(self.armor) + ', ' +  str(self.potion))

    def show_fight_stats(self):
        print('\n   >' + str(self.name) + '<\n')
        print('   Health (MAX): ' + str(self.health) + ' (' + str(self.maxhealth) + ')')
        print('     Dexterity : ' + str(self.dexterity))
        print('     Luck (MAX): ' + str(self.luck) + ' (' + str(self.maxluck) + ')')

    def show_enemy_fight_stats(self):
        print('\n   >' + str(self.name) + '<\n')
        print('   Health (MAX): ' + str(self.health) + ' (' + str(self.maxhealth) + ')')
        print('     Dexterity : ' + str(self.dexterity))

    def roll_for_strike_dexterity(self):
        return self.dexterity + random.randint(1, 6)

    def suffer_damage(self, damagepoint):
        self.health -= damagepoint
    def reduce_luck(self):
        self.luck -= 1

# class Opponent(Character):
#     pass

class FightTurn():
    def __init__(self, player, opponent, loser_for_turn):
        self.loser_for_turn = loser_for_turn
        self.player = player
        self.opponent = opponent


    def decide_who_strikes(self):
        if self.player.dexterity + random.randint(1, 6) > self.opponent.dexterity + random.randint(1, 6):
            print('\n\n  You Strike!')
            self.loser_for_turn = self.opponent
        else:
            print('\n\n  Unfortunately the opponent strikes')
            self.loser_for_turn = self.player

    def player_tries_luck(self):
        if random.randint(1, 6) + random.randint(1, 6) > self.player.luck:
            if self.loser_for_turn == self.player:
                self.player.suffer_damage(3)
            else:
                self.player.suffer_damage(1)
        else:
            if self.loser_for_turn == self.player:
                self.player.suffer_damage(1)
                self.player.reduce_luck()
            else:
                self.player.suffer_damage(1)
                self.player.reduce_luck()


hero = Character(None, 0, 0, 0)
monster = Character('Enemy Monster', 4, 12, 4)
monster.maxhealth = 12
testfight = FightTurn(hero, monster, None)
