from math import sqrt

import unittest


def is_prime(n):
    if n < 2:
        return False
    max_factor = int(sqrt(n))
    return all(n % i for i in range(2, max_factor + 1))


def generate_primes(n):
    return [i for i in range(2, n + 1) if is_prime(i)]


class TestPrimeGenerator(unittest.TestCase):
    def test_0(self):
        self.assertEqual(generate_primes(15), [2, 3, 5, 7, 11, 13])

    def test_1(self):
        self.assertEqual(generate_primes(9), [2, 3, 5, 7])

    def test_2(self):
        self.assertEqual(generate_primes(200),
                          [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89,
                           97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191,
                           193, 197, 199])

if __name__ == "__main__":
    unittest.main()
