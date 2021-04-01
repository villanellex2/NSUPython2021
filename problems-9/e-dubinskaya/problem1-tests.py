import problem1 as p1
import unittest


def test_func():
    with p1.Timer():
        raise Exception


class TestCalculator(unittest.TestCase):
    def test_1(self):
        self.assertRaises(Exception, test_func)


if __name__ == "__main__":
    unittest.main()