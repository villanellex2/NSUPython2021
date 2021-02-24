#!/usr/bin/env python3

def collatz(num):
    res = []
    while num != 1:
        res.append(num)
        num = num // 2 if num % 2 == 0 else num * 3 + 1
    res.append(num)
    return res


if __name__ == '__main__':
    print(collatz(int(input())))
