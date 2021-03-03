#!/usr/bin/env python3


def string_finder(string: str, value: str, res: list) -> int:
    num = 0
    while True:
        curr_occ = string.find(value)
        if curr_occ == -1:
            break
        if len(res) < 5:
            res.append(curr_occ)
        num += 1
        string = string[curr_occ+1:]
    return num


print("Enter sequence to search for: ", end="")
inp = input()
while not inp.isdigit():
    print("Incorrect input, enter integer value", end=": ")
    inp = input()
size = len(inp)

try:
    f = open("res/pi.txt", 'r')

    string = f.read(size * 10)
    out = 0
    res = []
    while True:
        out += string_finder(string, inp, res)
        if len(string) < size - 1:
            break
        string = string[-size+1:] + f.read(size * 10)
        if len(string) == size-1:
            break
    print(out)
except OSError as e:
    from sys import stderr
    print(e, file=stderr)
