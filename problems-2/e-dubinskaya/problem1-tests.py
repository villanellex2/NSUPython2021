#!/usr/bin/env python3
import problem1 as p1
import unittest


class TestCalculator(unittest.TestCase):
    def test_1(self):
        correct = [[3, 4, 5]]
        actual = p1.get_pythagorean_triplets(5)
        self.assertEqual(correct, actual)

    def test_2(self):
        correct = [[3, 4, 5], [5, 12, 13], [6, 8, 10]]
        actual = p1.get_pythagorean_triplets(14)
        self.assertEqual(correct, actual)

    def test_3(self):
        res = p1.get_pythagorean_triplets(100)
        for triplet in res:
            self.assertEqual(triplet[2] ** 2, triplet[1] ** 2 + triplet[0] ** 2)
            self.assertTrue((triplet[1] ** 2 + triplet[0] ** 2) ** 0.5 <= 100)

if __name__ == "__main__":
    unittest.main()
