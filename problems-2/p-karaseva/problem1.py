#!/usr/bin/env python3

num = int(input())
print([
    (2*m*n, m**2 - n**2, m**2 + n**2)
    for m in range(1, num)
    for n in range(1, m)
    if m**2 + n**2 <= num
])