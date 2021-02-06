from math import sqrt, ceil
import unittest


def expand_number(n):
    max_factor = ceil(sqrt(n))
    factors = []
    cur_factor = 2
    while cur_factor <= max_factor:
        counter = 0
        while n % cur_factor == 0:
            counter += 1
            n //= cur_factor

        if counter > 0:
            factors.append([cur_factor, counter])
        cur_factor += 1
    if n > 1:
        factors.append([n, 1])
    return factors


class TestNumberExpansion(unittest.TestCase):
    def test_0(self):
        self.assertEqual(expand_number(13), [[13, 1]])

    def test_1(self):
        self.assertEqual(expand_number(3 ** 4 * 2 ** 6 * 5 ** 5), [[2, 6], [3, 4], [5, 5]])

    def test_2(self):
        self.assertEqual(expand_number(1), [])

    def test_3(self):
        self.assertEqual(expand_number(199), [[199, 1]])

    def test_4(self):
        self.assertEqual(expand_number(13 * 17), [[13, 1], [17, 1]])

    def test_5(self):
        self.assertEqual(expand_number(14 * 19 * 15), [[2, 1], [3, 1], [5, 1], [7, 1], [19, 1]])

    def test_6(self):
        self.assertEqual(expand_number(10), [[2, 1], [5, 1]])


if __name__ == "__main__":
    unittest.main()
