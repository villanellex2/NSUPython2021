#!/usr/bin/env python3

from math import sqrt


def get_pythagorean_triplets(n: int) -> list:
    return [
        [i, j, int(sqrt(i * i + j * j))]
        for i in range(1, n)
        for j in range(i + 1, n)
        if sqrt(i * i + j * j) % 1 == 0 and sqrt(i * i + j * j) <= n
    ]


if __name__ == '__main__':
    print("Enter number: ", end="")
    inp = input()
    while not inp.isdigit():
        print("incorrect input, enter integer value", end=": ")
        inp = input()
    inp = int(inp)
    print(get_pythagorean_triplets(inp))
