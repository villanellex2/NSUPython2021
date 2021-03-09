#!/usr/bin/env python3
import unittest
from problem5 import primes_list_list_expression
from problem5 import primes_list_sieve

class TestStringMethods(unittest.TestCase):

    def test_neg12_list_expression(self):
        self.assertEqual(primes_list_list_expression(-12), [])

    def test_pos12_list_expression(self):
        self.assertEqual(primes_list_list_expression(12), [2,3,5,7,11])
    
    def test_pos11_list_expression(self):
        self.assertEqual(primes_list_list_expression(12), [2,3,5,7,11])

    def test_exception_type_error_list_expression(self):
        self.assertRaises(TypeError, primes_list_list_expression, '1111')
        
    def test_neg12_sieve(self):
        self.assertEqual(primes_list_sieve(-12), [])

    def test_pos12_sieve(self):
        self.assertEqual(primes_list_sieve(12), [2,3,5,7,11])
    
    def test_pos11_sieve(self):
        self.assertEqual(primes_list_sieve(12), [2,3,5,7,11])

    def test_exception_type_error_sieve(self):
        self.assertRaises(TypeError, primes_list_sieve, '1111')


if __name__ == '__main__':
    unittest.main() 