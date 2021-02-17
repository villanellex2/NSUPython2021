#!/usr/bin/env python3
from sys import stderr

def __is_prime(num):
	return all(num % delim != 0 for delim in range(2, int(num ** 0.5) + 1))

try:
	num = int(input())
	print([
		i for i in range(2, num + 1) if __is_prime(i)
	]) 

except ValueError:
	print("Write an integer", file = stderr)