#!/usr/bin/env python3

num = int(input())
print(
    [
        (x, y, int((x*x + y*y) ** (1/2)))
        for x in range(num)
        for y in range(1, x)
        if ((x*x + y*y) ** (1/2)) % 1 == 0
    ]
)