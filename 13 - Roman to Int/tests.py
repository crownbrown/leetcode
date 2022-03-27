from main import romanToInt
import unittest


class TestCase(unittest.TestCase):
    def test1a(self):
        self.assertEqual(romanToInt('I'), 1)

    def test1b(self):
        self.assertEqual(romanToInt('II'), 2)

    def test1c(self):
        self.assertEqual(romanToInt('III'), 3)

    def test1d(self):
        self.assertEqual(romanToInt('IV'), 4)

    def test2a(self):
        self.assertEqual(romanToInt('IX'), 9)

    def test2b(self):
        self.assertEqual(romanToInt('XL'), 40)

    def test2c(self):
        self.assertEqual(romanToInt('XC'), 90)

    def test2d(self):
        self.assertEqual(romanToInt('CD'), 400)

    def test2e(self):
        self.assertEqual(romanToInt('CM'), 900)

    def test3a(self):
        self.assertEqual(romanToInt('LVIII'), 58)

    def test3b(self):
        self.assertEqual(romanToInt('MCMXCIV'), 1994)