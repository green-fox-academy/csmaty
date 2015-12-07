import unittest
from counter import count_letters

class LetterCounterTest(unittest.TestCase):
    def test_simple_letter(self):
        self.assertEqual(count_letters('a'), {'a': 1})
        self.assertEqual(count_letters('aa'), {'a': 2})

    def test_different_letters(self):
        self.assertEqual(count_letters('b'), {'b': 1})

    def test_distinct_letters(self):
        self.assertEqual(count_letters('ab'), {'a': 1 , 'b': 1})
        self.assertEqual(count_letters('baba'), {'a': 2 , 'b': 2})



unittest.main()