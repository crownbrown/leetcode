from main import isMatch
import unittest


class TestCase(unittest.TestCase):
    def test1a(self):
        self.assertEqual(isMatch('aa', 'a'), False)
