import unittest
class TestMenu(unittest.TestCase):
    def test_choose(self):
        def test_func():
            return True
        menu = Menu([
                MenuItem(1, 'Test', test_func)
                ])
        self.assertEqual(menu.choose(1), True)

unittest.man()
