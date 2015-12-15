from pregame_operations import *
import os


class MenuItem():
    def __init__(self, number, name, action):
        self.number = number
        self.name = name
        self.action = action

    def display_menu_item(self):
        return self.number + ': ' + self.name

class Menu():
    def __init__(self, itemlist):
        self.itemlist = itemlist

    def displaymenu(self):
        os.system('clear')
        print('\n')
        for item in self.itemlist:
            print(item.display_menu_item())

    def user_chooses(self):
        chosen_option = input('\n>>Please enter the number of the chosen option: \n>>')
        self.select_and_call_action(chosen_option)

    def select_and_call_action(self, chosen_option):
        numberlist = list(map(lambda item: item.number, self.itemlist))
        if chosen_option in numberlist:
            for item in self.itemlist:
                if item.number == chosen_option:
                    return item.action()
        else:
            print('\n>>>>INCORRECT INPUT!!!<<<<\n')
            return 'INCORRECT INPUT'
            self.user_chooses()

    def main(self):
        while True:
            self.displaymenu()
            self.user_chooses()

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
        MenuItem('2', 'Save Stats and Continue', mainmenu.main),
        MenuItem('3', 'Save Stats', mainmenu.main),
        MenuItem('4', 'Quit', mainmenu.main)
        ]
    statsmenu = Menu(statsmenu_itemlist)
    statsmenu.main()

mainmenu_itemlist = [
    MenuItem('1','New game', newgamemenu),
    MenuItem('2', 'Load Game', loadmenu),
    MenuItem('3', 'Exit', exit),
    MenuItem('000', 'Exit without Saving', exit)
    ]
mainmenu = Menu(mainmenu_itemlist)
