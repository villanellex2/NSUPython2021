#!/usr/bin/env python3

def seive(arr: list, num: int):
    size = len(arr)
    i = 0
    while i < size:
        if arr[i] != num and arr[i] % num == 0:
            arr.remove(arr[i])
            size -= 1
        else:
            #print(str(arr[i]) + "%" + str(num) + "==" + str(arr[i]%num))
            i = i + 1


def main_cycle(arr: list) -> list:
    size = len(arr)
    i = 0
    while i < size:
        seive(arr, arr[i])
        i = i + 1
        size = len(arr)
    return arr


print("Enter number: ", end="")
inp = input()
while not inp.isdigit():
    print("incorrect input, enter integer value", end=": ")
    inp = input()
inp = int(inp)

print(main_cycle(list(range(2, inp + 1))))
#print(len(main_cycle(list(range(2, inp + 1)))))