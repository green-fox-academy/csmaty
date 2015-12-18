from characters import *
from menu_classes import *
import os

class GameScreen():
    def __init__(self, menu_to_display):
        self.menu_to_display = menu_to_display

    def change_menu_to_display(self, selectedmenu):
        self.menu_to_display = selectedmenu

gamescreen = GameScreen('mainmenu')

def newgamemenu():
    newgamemenu = Menu([
        MenuItem('1','Start New Game', enter_name),
        MenuItem('2', 'Back to Main Menu', gamescreen.change_menu_to_display, 'mainmenu')
        ])
    newgamemenu.main()

def loadmenu():
    loadmenu = Menu([
        MenuItem('1','Choose from Saved Games', gamescreen.change_menu_to_display, 'mainmenu'),
        MenuItem('2', 'Back to Main Menu', gamescreen.change_menu_to_display, 'mainmenu'),
        ])
    loadmenu.main()

def quitmenu():
    quitmenu = Menu([
        MenuItem('1','Quit Game', exit),
        MenuItem('2', 'Back to Main Menu', gamescreen.change_menu_to_display, 'mainmenu'),
        ])
    quitmenu.main()

def namemenu():
    namemenu = Menu([
        MenuItem('1', 'Continue to Hero Stats', rollstats),
        MenuItem('2','Reenter name', enter_name),
        MenuItem('3', 'Save Name', savename),
        MenuItem('4', 'Quit', gamescreen.change_menu_to_display, 'mainmenu')
        ])
    namemenu.main()

def enter_name():
    hero.enter_name()
    gamescreen.change_menu_to_display('namemenu')

def savename():
    hero.export_charspecs()
    print('The chosen name was saved.')

def statsmenu():
    statsmenu = Menu([
        MenuItem('1','Roll for new stats', rollstats),
        MenuItem('2', 'Continue', gamescreen.change_menu_to_display, 'potions'),
        MenuItem('3', 'Save Stats', savestats),
        MenuItem('4', 'Quit', gamescreen.change_menu_to_display, 'mainmenu')
        ])
    statsmenu.main()

def rollstats():
    hero.roll_stats()
    gamescreen.change_menu_to_display('statsmenu')

def savestats():
    hero.export_charspecs()
    print('The Stats were saved.')

def potions():
    print('\nSelect one potion to take with youself: \n\n')
    potions = Menu([
        MenuItem('1','Potion of Health', reconsider_potion, 'Potion of Health'),
        MenuItem('2', 'Potion of Dexterity', reconsider_potion, 'Potion of Dexterity'),
        MenuItem('3', 'Potion of Luck', reconsider_potion, 'Potion of Luck'),
        ])
    potions.main()

def potionmenu():
    potionmenu = Menu([
        MenuItem('1','Select another potion', gamescreen.change_menu_to_display, 'potions'),
        MenuItem('2', 'Continue', begin_game_screen),
        MenuItem('3', 'Quit', gamescreen.change_menu_to_display, 'mainmenu')
        ])
    potionmenu.main()

def reconsider_potion(potion):
    hero.add_potion(potion)
    gamescreen.change_menu_to_display('potionmenu')

def begingamemenu():
    begingamemenu = Menu([
        MenuItem('1','Begin Game',  round_one____fight),
        MenuItem('2', 'Save Hero', savehero),
        MenuItem('3', 'Quit', gamescreen.change_menu_to_display, 'mainmenu')
        ])
    begingamemenu.main()

def begin_game_screen():
    hero.display_character()
    gamescreen.change_menu_to_display('begingamemenu')

def savehero():
    hero.export_charspecs()
    print('Your hero\'s specifications were saved.')
    begin_game_screen()

def round_one____fight():
    print("Test your Sword in a test fight")
    hero.show_fight_stats()
    print('\n****')
    monster.show_enemy_fight_stats()
    gamescreen.change_menu_to_display('fightmenu')

def fightmenu():
    fightmenu = Menu([
        MenuItem('1','Strike',  fight_hit),
        MenuItem('2', 'Retreat', gamescreen.change_menu_to_display, 'mainmenu'),
        MenuItem('3', 'Quit', gamescreen.change_menu_to_display, 'mainmenu')
        ])
    fightmenu.main()

def strikemenu():
    strikemenu = Menu([
        MenuItem('1','Continue', next_strike),
        MenuItem('2', 'Try your Luck', roll_for_luck),
        MenuItem('3', 'Retreat', gamescreen.change_menu_to_display, 'mainmenu'),
        MenuItem('4', 'Quit', gamescreen.change_menu_to_display, 'mainmenu')
        ])
    strikemenu.main()

def fight_hit():
    testfight.decide_who_strikes()
    strikemenu()

def next_strike():
    testfight.loser_for_turn.suffer_damage(2)
    round_one____fight()

def roll_for_luck():
    testfight.player_tries_luck()
    round_one____fight()

mainmenu = Menu([
    MenuItem('1','New game', gamescreen.change_menu_to_display, 'newgamemenu'),
    MenuItem('2', 'Load Game', gamescreen.change_menu_to_display, 'loadmenu'),
    MenuItem('3', 'Exit', gamescreen.change_menu_to_display, 'quitmenu'),
    MenuItem('000', 'Exit without Save', exit)
    ])

function_dict = {
    'mainmenu': mainmenu.main,
    'newgamemenu': newgamemenu,
    'loadmenu': loadmenu,
    'quitmenu': quitmenu,
    'namemenu': namemenu,
    'statsmenu': statsmenu,
    'fightmenu': fightmenu,
    'strikemenu': strikemenu,
    'begingamemenu': begingamemenu,
    'potions': potions,
    'potionmenu': potionmenu,
    }

while True:
    function_dict[gamescreen.menu_to_display]()
