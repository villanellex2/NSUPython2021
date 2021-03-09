import unittest
from problem5 import primes_list

class TestStringMethods(unittest.TestCase):

    def test_neg12(self):
        self.assertEqual(primes_list(-12), [])

    def test_pos12(self):
        self.assertEqual(primes_list(12), [2,3,5,7,11])
    
    def test_pos11(self):
        self.assertEqual(primes_list(12), [2,3,5,7,11])

    def test_exception_type_error(self):
        self.assertRaises(TypeError, primes_list, '1111')


if __name__ == '__main__':
    unittest.main() 