#!/usr/bin/env python3


while True:
    print('Please, enter the number > 1!')
    s = input()
    if s.isnumeric():
        n = int(s)
        if n > 1:
            break

print([(i, j, sqrs.index(sqrs[i] + sqrs[j])) 
        for i in range(2, n + 1) 
        for j in range(i, n + 1) 
        for sqrs in [[m*m for m in range(n + 1)]]
        if sqrs[i] + sqrs[j] in sqrs])
