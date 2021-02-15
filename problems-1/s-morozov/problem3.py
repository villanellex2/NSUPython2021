#!/usr/bin/env python3

def collatz(n):
  chain = [n]
  while chain[-1] != 1:
    chain.append(chain[-1] // 2 if chain[-1] % 2 == 0 else 3 * chain[-1] + 1)
  return chain

n = int(input())
print(collatz(n))
