#!/usr/bin/env python3

import unittest

def cut(nums, a, b):
    for i in range(len(nums)):
        if nums[i] < a:
            nums[i] = a
        elif nums[i] > b:
            nums[i] = b
    return nums


##input = list(map(int, input().split()))
##a = int(input())
##b = int(input())
##print(cut(input, a, b))

class MyTestCase(unittest.TestCase):
    def test_1(self):
        data = [1, 2, 3, 4, 4, 4, 5, 7, 8]
        self.assertEqual(cut(data, 2, 5), [2, 2, 3, 4, 4, 4, 5, 5, 5])

    def test_2(self):
        data = ['a', 'd', 'f', 'f']
        with self.assertRaises(TypeError):
            cut(data, 1, 2)

    def test_3(self):
        data = [1.152, 7, 56, 3, 6.99, 8, 200.01, 14, 15, 14.5]
        self.assertEqual(cut(data, 7, 14), [7, 7, 14, 7, 7, 8, 14, 14, 14, 14])


if __name__ == '__main__':
    unittest.main()
    
