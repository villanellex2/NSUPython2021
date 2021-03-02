#!/usr/bin/env python3
from sys import stderr

try:
	num = int(input())
	print([
		i for i in range(2, num + 1) if all(i % delim != 0 for delim in range(2, int(i ** 0.5) + 1))
	]) 

except ValueError:
	print("Write an integer", file = stderr)