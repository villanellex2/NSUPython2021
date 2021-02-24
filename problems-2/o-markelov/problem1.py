#!/usr/bin/env python3

i_num = int(input('Enter some number:\n'))

print([
    (a, b, c)
    for a in range(1, i_num)
    for b in range(a + 1, i_num)
    for c in range(b + 1, i_num)
    if a * a + b * b == c * c
])
