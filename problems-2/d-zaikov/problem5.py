#!/usr/bin/env python3
import math
import sys
def primes_list_list_expression(n):
    return [i for i in range(2, n + 1) 
            if all(i % d != 0 
            for d in range(2, int(math.sqrt(i)) + 1))]
            
def primes_list_sieve(n):
    if n < 2:
        return []
    s = [True] * n
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if s[i]:
            s[i * i::2 * i] = [False] * ((n - i * i - 1) // (2 * i) + 1)
    return [2] + [i for i in range(3, n, 2) if s[i]]
            
            
if __name__ == '__main__':
    try:
        n = int(input('Write upper bound for primes list (an integer).'))
    except ValueError as e:
        print('Error: the entered string is not an integer.\n', file=sys.stderr)
        print('--------More info--------', file=sys.stderr)
        print(e, file=sys.stderr)
        exit(1)
    except Exception as e:
        print(e, file=sys.stderr)
        exit(1)
     
    print(primes_list_sieve(n))