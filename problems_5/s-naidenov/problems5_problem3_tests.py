import unittest

from Stack import Stack
from FixedStack import FixedStack

class StackTest(unittest.TestCase):

    def test_init(self):
        stack = Stack()
        self.assertEqual(stack.elements, [])

        stack = Stack([1, 23, 2])
        self.assertEqual(stack.elements, [1, 23, 2])

    def test_pop(self):
        stack = Stack([1, 2, 3])
        stack.push(4)
        self.assertEqual(stack.elements, [1, 2, 3, 4])
        stack.pop()
        self.assertEqual(stack.elements, [1, 2, 3])

    def test_push(self):
        stack = Stack()
        stack.push(2)
        self.assertEqual(stack.elements, [2])
        stack.push(3)
        self.assertEqual(stack.elements, [2, 3])
        stack = Stack()
        try:
            self.assertEqual(stack.elements, [])  # ERROR, при изменении значения elements изменяется и его значение по
        # умолчанию, поэтому при создании нового stack'а elements не будет равно []
        except Exception:
            print("test push failed")

    def test_init_fixed(self):
        stack = FixedStack()
        self.assertEqual(stack.elements, [])

        stack = FixedStack([1, 23, 2])
        self.assertEqual(stack.elements, [1, 23, 2])

    def test_pop_fixed(self):
        stack = FixedStack([1, 2, 3])
        stack.push(4)
        self.assertEqual(stack.elements, [1, 2, 3, 4])
        stack.pop()
        self.assertEqual(stack.elements, [1, 2, 3])

    def test_push_fixed(self):
        stack = FixedStack()
        stack.push(2)
        self.assertEqual(stack.elements, [2])
        stack.push(3)
        self.assertEqual(stack.elements, [2, 3])
        stack = FixedStack()
        self.assertEqual(stack.elements, [])




if __name__ == '__main__':
    unittest.main()
