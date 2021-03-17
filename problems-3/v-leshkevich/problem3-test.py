#!/usr/bin/env python3

import unittest
from problem3 import Vector


class TestVectorClass(unittest.TestCase):
    def test_add(self):
        a = Vector([1, 2, 3])
        b = Vector((4, 5, 6))
        self.assertEqual(a + b, Vector(5, 7, 9))

    def test_sub(self):
        a = Vector([1, 2, 3])
        b = Vector(4, 5, 6)
        self.assertEqual(a - b, Vector(-3, -3, -3))

    def test_mult(self):
        a = Vector([1, 2, 3])
        self.assertEqual(a * 5, Vector(5, 10, 15))

    def test_dot_mult(self):
        a = Vector([1, 2, 3])
        b = Vector(4, 5, 6)
        self.assertEqual(a * b, 32)

    def test_getitem(self):
        a = Vector(1, 2, 3)
        self.assertEqual(a[1], 2)

    def test_len(self):
        self.assertEqual(len(Vector(1, 2, 3, 4, 6)), 5)

    def test_repr(self):
        a = Vector(1, 2, 3)
        self.assertEqual(repr(a), 'Vector((1, 2, 3))')


if __name__ == '__main__':
    unittest.main()
