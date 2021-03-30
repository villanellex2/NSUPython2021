#!/usr/bin/env python3


def string_finder(string: str, value: str, res: list) -> int:
    num = 0
    prev_len = 0
    while True:
        curr_occ = string.find(value)
        if curr_occ == -1:
            break
        if len(res) < 5:
            res.append(curr_occ + prev_len)
        num += 1
        string = string[curr_occ+1:]
        prev_len += curr_occ + 1
    return num


print("Enter sequence to search for: ", end="")
inp = input()
while not inp.isdigit():
    print("Incorrect input, enter integer value", end=": ")
    inp = input()
size = len(inp)

try:
    f = open("res/pi.txt", 'r')

    string = f.read()
    string = string[2:]
    res = []
    prev_len = 0
    out = string_finder(string, inp, res)
    print("Found " + str(out) + " results.")
    print("Positions: ", end=" ")
    for pos in res:
        print(pos, end=" ")
    if len(res) < out:
        print("...")

except OSError as e:
    from sys import stderr
    print(e, file=stderr)
