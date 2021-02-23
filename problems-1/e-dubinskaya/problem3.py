#!/usr/bin/env python3

def to_collatz_list(a: int) -> list:
    res = [a]
    while a > 1:
        if a % 2 == 0:
            a = a // 2
        else:
            a = a * 3 + 1
        res.append(a)
    return res


inp = int(input())
for i in to_collatz_list(inp):
    if i != 1:
        print(str(i), end='->')
    else:
        print(1)
