from pregame_operations import *
from menu_classes import *
import os

def newgamemenu():
    newgamemenu_itemlist = [
        MenuItem('1','Start New Game', namemenu),
        MenuItem('2', 'Back to Main Menu', mainmenu.main)
        ]
    newgamemenu = Menu(newgamemenu_itemlist)
    newgamemenu.main()

def loadmenu():
    loadmenu_itemlist = [
        MenuItem('1','Choose from Saved Games', mainmenu.main),
        MenuItem('2', 'Back to Main Menu', mainmenu.main),
        ]
    loadmenu = Menu(loadmenu_itemlist)
    loadmenu.main()

def namemenu():
    character.enter_name()
    namemenu_itemlist = [
        MenuItem('1','I would like to use a different name', character.enter_name),
        MenuItem('2', 'Save Name and Continue', statsmenu),
        MenuItem('3', 'Save Name', mainmenu.main),
        MenuItem('4', 'Quit', mainmenu.main)
        ]
    namemenu = Menu(namemenu_itemlist)
    namemenu.main()

def statsmenu():
    character.roll_stats()
    statsmenu_itemlist = [
        MenuItem('1','I would like to roll for new stats', character.roll_stats),
        MenuItem('2', 'Save Stats and Continue', potion_select),
        MenuItem('3', 'Save Stats', mainmenu.main),
        MenuItem('4', 'Quit', mainmenu.main)
        ]
    statsmenu = Menu(statsmenu_itemlist)
    statsmenu.main()

def potion_select():
    character.potion_message()
    potionlist = [
        MenuItem('1','Potion of Health', character.add_potion, 'Potion of Health'),
        MenuItem('2', 'Potion of Dexterity', character.add_potion, 'Potion of Dexterity'),
        MenuItem('3', 'Potion of Luck', character.add_potion, 'Potion of Luck'),
        MenuItem('4', 'Quit', mainmenu.main)
        ]
    potions = Menu(potionlist)
    potions.main()
    potionmenu()



def potionmenu():
    # character.potion_message()
    potionmenu_itemlist = [
        MenuItem('1','Select another potion', potion_select),
        MenuItem('2', 'Continue', mainmenu.main),
        MenuItem('3', 'Quit', mainmenu.main)
        ]
    potionmenu = Menu(potionmenu_itemlist)
    potionmenu.main()





mainmenu_itemlist = [
    MenuItem('1','New game', newgamemenu),
    MenuItem('2', 'Load Game', loadmenu),
    MenuItem('3', 'Exit', exit),
    MenuItem('000', 'Exit without Saving', exit)
    ]
mainmenu = Menu(mainmenu_itemlist)
