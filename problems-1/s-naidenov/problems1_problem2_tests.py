import unittest
from problem2 import trim_sequence


class TestFunction(unittest.TestCase):

    def test_0(self):
        l_0 = [4, 4, 4, 9, 7, 121, 256, 44, 767, 66, 6]
        self.assertEqual(trim_sequence(l_0, 6, 100), [6, 6, 6, 9, 7, 100, 100, 44, 100, 66, 6])

    def test_1(self):
        l_1 = [4, 9, 4, 9, 7, 13, 25, 44, 7, 66, 6]
        self.assertEqual(trim_sequence(l_1, 5, 20), [5, 9, 5, 9, 7, 13, 20, 20, 7, 20, 6])

    def test_2(self):
        l_2 = [2, 4, 1, 10, 7, 56, 256, 55, 767, 66, 99, 13, 16, 75]
        self.assertEqual(trim_sequence(l_2, 3, 56), [3, 4, 3, 10, 7, 56, 56, 55, 56, 56, 56, 13, 16, 56])


if __name__ == '__main__':
    unittest.main()
