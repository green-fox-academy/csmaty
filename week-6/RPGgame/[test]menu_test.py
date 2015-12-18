import unittest
from menu import *

class TestMenu(unittest.TestCase):

    def test_has_name_number_and_action(self):
        item = MenuItem('1', 'New Game', 'action')
        self.assertEqual(item.name, 'New Game')
        self.assertEqual(item.number, '1')
        self.assertEqual(item.action, 'action')

    def test_display_menu_item(self):
        item = MenuItem('1', 'New Game', 'action')
        result = item.display_menu_item()
        self.assertEqual(result, ' 1: New Game')

    def test_select_and_call_action_correct_input(self):
        def action2():
            return 'action2'
        itemlist = [
            MenuItem('2', 'Load Game', action2),
            ]
        testmenu = Menu(itemlist)
        chosen_option = '2'
        result = testmenu.select_and_call_action(chosen_option)
        self.assertEqual(result, 'action2')

    def test_select_and_call_action_incorrect_input(self):
        def action2():
            return 'action2'
        itemlist = [
            MenuItem('2', 'Load Game', action2),
            ]
        testmenu = Menu(itemlist)
        chosen_option = 'perec'
        result = testmenu.select_and_call_action(chosen_option)
        self.assertEqual(result, 'INCORRECT INPUT')


unittest.main()
