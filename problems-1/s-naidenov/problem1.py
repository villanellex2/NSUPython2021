import unittest


def cum_sum(l):
    res = []
    cur_sum = 0
    res.append(cur_sum)
    for i in l:
        cur_sum += i
        res.append(cur_sum)
    return res


class TestCumSum(unittest.TestCase):
    def test_0(self):
        l = [1, 2, 3]
        self.assertEqual(cum_sum(l), [0, 1, 3, 6])

    def test_1(self):
        l = [1, 2, 3, 4]
        self.assertEqual(cum_sum(l), [0, 1, 3, 6, 10])

    def test_2(self):
        l = [3, 4, 3, 10, 7, 56, 56, 55, 56, 56, 56, 13, 16, 56]
        self.assertEqual(cum_sum(l), [0, 3, 7, 10, 20, 27, 83, 139, 194, 250, 306, 362, 375, 391, 447])


if __name__ == '__main__':
    unittest.main()
