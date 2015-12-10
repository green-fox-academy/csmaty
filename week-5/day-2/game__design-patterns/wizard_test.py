import unittest
from wizard import Wizard

class TestWizard(unittest.TestCase):
    def test_existence(self):
        wizard = Wizard('Merlin', 40, 10, 20)

    def test_inheritance(self):
        wizard = Wizard('Merlin', 40, 10, 20)
        self.assertEqual(wizard.hp, 40)

    def test_manna(self):
        wizard = Wizard('Merlin', 40, 10, 20)
        self.assertEqual(wizard.manna, 20)

    def test_strike_manna_over_5(self):
        wizard = Wizard('Merlin', 40, 10, 20)
        opponent = Wizard('NemMerlin', 120, 10, 20)
        wizard.strike(opponent)
        self.assertEqual(wizard.manna, 15)
        self.assertEqual(opponent.hp, 90)

    def test_strike_manna_under_5(self):
        wizard = Wizard('Merlin', 40, 10, 2)
        opponent = Wizard('NemMerlin', 120, 10, 20)
        wizard.strike(opponent)
        self.assertEqual(wizard.manna, 2)
        self.assertEqual(opponent.hp,  116.66666666666667)




unittest.main()
