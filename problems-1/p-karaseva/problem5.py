#!/usr/bin/env python3

def prime_factors(n):
    factors = []
    f = 2
    while f*f <= n:
        pow = 0
        while n % f == 0:
            n //= f
            pow += 1

        if pow > 0:
            factors.append([f, pow])

        f += 1

    if n != 1:
        factors.append([n, 1])
    return factors


if __name__ == '__main__':
    n = int(input())
    print(prime_factors(n))

