#!/usr/bin/env python3

def cumsum(list):
    res = [0]
    curr_sum = 0
    for elem in list:
        curr_sum += elem
        res.append(curr_sum)
    return res



##input = list(map(int, input().split()))
##print(cumsum(input))


class MyTestCase(unittest.TestCase):
    def test_1(self):
        data = ['a', 'b', 'c']
        with self.assertRaises(TypeError):
            cumsum(['a', 'v', 'd'])

    def test_2(self):
        data = [1, 2, 3, 4, 5, 6]
        self.assertEqual(cumsum(data), [0, 1, 3, 6, 10, 15, 21])

    def test_3(self):
        data = [i for i in range(1, 100)]
        self.assertEqual(len(cumsum(data)), 100)

    def test_4(self):
        data = [1, 3, 4.15, 3.709, 5, 12.04]
        self.assertEqual(cumsum(data)[-1], 28.899)

if __name__ == '__main__':
    unittest.main()
    
