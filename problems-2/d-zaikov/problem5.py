#!/usr/bin/env python3
import math
import sys
def primes_list(n):
    return [i for i in range(2, n + 1) 
            if all(i % d != 0 
            for d in range(2, int(math.sqrt(i)) + 1))]
            
            
if __name__ == '__main__':
    try:
        n = int(input())
    except ValueError:
        print('Please, write an integer.', file=sys.stderr)
        exit(1)
    except Exception as e:
        print(e, file=sys.stderr)
        exit(1)
     
    print(primes_list(n))