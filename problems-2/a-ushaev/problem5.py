#!/usr/bin/env python3

num = int(input())

print([
    i for i in range(2, num + 1) if all(i % j != 0 for j in range(2, int(i ** 0.5) + 1))
])