import sudoku_checker
import unittest

class TestSudokuChecker(unittest.TestCase):
    def test_is_complete_empty(self):
        test_input = []
        expected = False
        actual = sudoku_checker.is_complete(test_input)
        self.assertEqual(expected, actual, "The row is empty.")

    def test_is_complete_too_short(self):
        test_input = [1, 2, 3, 4, 5, 6, 7, 8]
        expected = False
        actual = sudoku_checker.is_complete(test_input)
        self.assertEqual(expected, actual, "The row is too short.")

    def test_is_too_long(self):
        test_input = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        expected = False
        actual = sudoku_checker.is_too_long(test_input)
        self.assertEqual(expected, actual, "The row is too long.")

    def test_repeating_numbers(self):
        test_input = [1, 2, 2, 4, 5, 6, 9, 8, 7]
        expected = False
        actual = sudoku_checker.repeating_numbers(test_input)
        self.assertEqual(expected, actual, "There are repeating numbers in your list.")


    def not_1_through_9(self):
        test_input = [1, 22, 3, 4, 5, 97, 9, 8, 7]
        expected = False
        actual = sudoku_checker.not_1_through_9(test_input)
        self.assertEqual(expected, actual, "The given numbers are not 1 through 9.")

    def not_1_through_9(self):
        test_input = [1, 22, 3, 4, 5, 97, 9, 8, 7]
        expected = False
        actual = sudoku_checker.not_1_through_9(test_input)
        self.assertEqual(expected, actual, "The given numbers are not 1 through 9.")




unittest.main()
