def primes(num):
    res = []
    for p in range(2, int(num ** (1/2)) + 1):
        k = 0
        while num % p == 0:
            num //= p
            k += 1
        if k != 0:
            res.append([p, k])

    if num > 2:
        res.append([num, 1])

    return res if len(res) > 0 else [[num, 1]]

print(primes(int(input())))