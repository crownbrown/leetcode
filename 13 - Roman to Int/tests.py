from main import romanToInt
import unittest


class TestCase(unittest.TestCase):
    def test1a(self):
        self.assertEqual(romanToInt('I'), 1)

    def test1b(self):
        self.assertEqual(romanToInt('II'), 2)
