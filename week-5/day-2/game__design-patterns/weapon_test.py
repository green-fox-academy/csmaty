import unittest
from weapon import Holy, Sword

class TestWeapon(unittest.TestCase):
    def test_holy_effect(self):
        weapon = Holy(Testweapon())
        self.assertEqual(13, weapon.damage())
        self.assertEqual(13, Holy(Sword()).damage())



class Testweapon:
    def damage(self):
        return 10

if __name__ == '__main__':
    unittest.main()
