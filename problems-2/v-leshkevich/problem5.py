#!/usr/bin/env python3

from math import sqrt

try:
    print([a for a in range(2, int(input()) + 1)
           if not any(a % b == 0 for b in range(2, int(sqrt(a)) + 1))])
except ValueError:
    print('Please enter integer.')
