#!/usr/bin/env python3

import itertools

try:
    n = int(input())

    print([
        (x, y, z)
        for x, y, z in itertools.product(range(1, n + 1), repeat=3)
        if x < y < z and x * x + y * y == z * z
    ])
except ValueError:
    print('Please enter integer.')
