#!/usr/bin/env python3

from math import sqrt


def get_primitives(x: int) -> list:
    return [
        i for i in range(2, x+1)
        if all(i % j != 0
               for j in range(2, i-1))]


if __name__ == '__main__':
    print("Enter number: ", end="")
    inp = input()
    while not inp.isdigit():
        print("incorrect input, enter integer value", end=": ")
        inp = input()
    inp = int(inp)
    print(get_primitives(inp))

