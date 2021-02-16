#!/usr/bin/env python3

def sing():
    nums = ["No", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten"]
    ending = " hanging on the wall"
    green_bottle = "green bottle"
    bottles = lambda n: nums[n] + " " + green_bottle + ("" if n == 1 else "s")
    first_line = lambda n: bottles(n) + ending + ","
    third_line = lambda n: ("And if" if n > 1 else "If that") + " one " + green_bottle + " should accidentally fall,"
    fourth_line = lambda n: "There'll be " + bottles(n - 1).lower() + ending + "."

    for i in range(10, 0, -1):
        print(first_line(i))
        print(first_line(i))
        print(third_line(i))
        print(fourth_line(i))


if __name__ == '__main__':
    sing()
