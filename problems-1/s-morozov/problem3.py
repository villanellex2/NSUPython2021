#!/usr/bin/env python3

def collatz(n):
  chain = [n]
  while chain[-1] != 1:
    if chain[-1] % 2 == 0:
      chain.append(chain[-1] // 2)
    else:
      chain.append(3 * chain[-1] + 1)
  return chain

n = int(input())
print(collatz(n))
