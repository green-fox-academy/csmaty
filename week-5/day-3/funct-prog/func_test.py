import unittest
import func

class TestFunc(unittest.TestCase):

    def test_should_apply_a_func(self):
        array = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.assertEqual(func.adder(array), [2, 3, 4, 5, 6, 7, 8, 9, 10])

    def test_filter_array(self):
        array = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.assertEqual(func.filetr_array(array), [0, 3, 6, 9])

unittest.main()
