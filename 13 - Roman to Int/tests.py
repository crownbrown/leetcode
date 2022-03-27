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
