#!/usr/bin/env python3

def prime_factor(num):
    factors = {}
    i = 2
    while i * i <= num:
        if num % i == 0:
            factors[i] = 0
        while num % i == 0:
            factors[i] += 1
            num = num // i
        i += 1
    if num != 1:
        factors[num] = 1
    return list(factors.items())


if __name__ == '__main__':
    print(prime_factor(int(input())))
