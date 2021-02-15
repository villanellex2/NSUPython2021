#!/usr/bin/env python3

def trim(lst, a, b):
  res = []
  for x in lst:
    if x < a:
      res.append(a)
    elif x > b:
      res.append(b)
    else:
      res.append(x)
  return res

lst = map(int, input('list: ').split())
a = int(input('a: '))
b = int(input('b: '))
print(trim(lst, a, b))

