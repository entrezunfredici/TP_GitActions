import unittest

class TestSimpleMath(unittest.TestCase):
    def test_add(self):
        self.assertEqual(2+3, 5)
    def test_rem(self):
        self.assertEqual(2-3, -1)
