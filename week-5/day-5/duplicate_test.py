import unittest
from duplicate import DuplicateEncode

class TestDuplicateEncode(unittest.TestCase):
    def test_all_one_char(self):
        subject = DuplicateEncode('eeeeee')
        self.assertEqual(subject.duplicate_encode(), '))))))')
    def test_only_one_char(self):
        subject = DuplicateEncode('e')
        self.assertEqual(subject.duplicate_encode(), '(')
    def test_lower_case_string(self):
        subject = DuplicateEncode('recede')
        self.assertEqual(subject.duplicate_encode(), '()()()')



unittest.main()
