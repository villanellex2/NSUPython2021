from math import sqrt


def get_primes(num):
    primes = []

    for p in range(2, int(sqrt(num)) + 1):
        k = 0
        while num % p == 0:
            num //= p
            k += 1

        if k > 0:
            primes.append([p, k])

    return primes if len(primes) > 0 else [[num, 1]]


i_num = int(input('Enter some number > 1:\n'))
print(get_primes(i_num) if i_num > 1 else 'The number must be > 1')
