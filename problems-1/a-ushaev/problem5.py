def primes(num):
    res = []
    k = 0
    while num % 2 == 0:
        num //= 2
        k += 1

    if k != 0:
        res.append([2, k])

    for p in range(3, int(num ** (1/2)) + 1, 2):
        k = 0
        while num % p == 0:
            num //= p
            k += 1
        if k != 0:
            res.append([p, k])

    if num > 2:
        res.append([num, 1])

    return res


print(primes(int(input())))