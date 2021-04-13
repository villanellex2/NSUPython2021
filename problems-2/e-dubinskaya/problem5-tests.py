import problem5 as p2
import unittest


def simple_generator(x: int) -> list:
    res = list()
    for i in range(2, x + 1):
        isPrime = True
        for j in range(2, i - 1):
            if i % j == 0:
                isPrime = False
                break
        if isPrime:
            res.append(i)
    return res


class TestCalculator(unittest.TestCase):
    def test_1(self):
        res = p2.get_primitives(100)
        actual = simple_generator(100)
        self.assertEqual(res, actual)

    def test_2(self):
        res = p2.get_primitives(1500)
        actual = simple_generator(1500)
        self.assertEqual(res, actual)


if __name__ == "__main__":
    unittest.main()
