#!/usr/bin/env python3
import unittest


def chain_of_numbers(n):
    s = str(n)
    while n != 1:
        if n % 2 == 0:
            n = n // 2
            s += ' -> ' + str(n)
        else:
            n = 3 * n + 1
            s += ' -> ' + str(n)
    return s


class MyTestCase(unittest.TestCase):
    def test_1(self):
        with self.assertRaises(TypeError):
            chain_of_numbers('a')

    def test_2(self):
        self.assertEqual(chain_of_numbers(1), '1')

    def test_3(self):
        self.assertEqual(chain_of_numbers(17), '17 -> 52 -> 26 -> 13 -> 40 -> 20 -> 10 -> 5 -> 16 -> 8 -> 4 -> 2 -> 1')

    def test_4(self):
        self.assertEqual(chain_of_numbers(5), '5 -> 16 -> 8 -> 4 -> 2 -> 1')


if __name__ == '__main__':
    unittest.main()
