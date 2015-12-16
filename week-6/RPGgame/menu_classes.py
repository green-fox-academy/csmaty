from pregame_operations import *
import os


class MenuItem():
    def __init__(self, number, name, action, itemarg = None):
        self.number = number
        self.name = name
        self.action = action
        self.itemarg = itemarg

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
                    if item.itemarg == None:
                        return item.action()
                    return item.action(item.itemarg)
        else:
            print('\n>>>>INCORRECT INPUT!!!<<<<\n')
            return 'INCORRECT INPUT'
            self.user_chooses()

    def main(self):
        while True:
            self.displaymenu()
            self.user_chooses()
