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


inp = input()
while not inp.isdigit():
    print("incorrect input, enter integer value", end=": ")
    inp = input()
inp = int(inp)

for i in to_collatz_list(inp):
    if i != 1:
        print(str(i), end='->')
    else:
        print(1)
