import unittest
from characters import *

class TestPreGameOperations(unittest.TestCase):

    def test_character_has_properties(self):
        character = Character('Lajos', 3 , 11, 9)
        self.assertEqual(character.name, 'Lajos')
        self.assertEqual(character.dexterity, 3)
        self.assertEqual(character.health, 11)
        self.assertEqual(character.luck, 9)

unittest.main()
