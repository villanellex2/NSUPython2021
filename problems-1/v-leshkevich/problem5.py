def factorization(number):
    if number == 1:
        return [number, 1]
    result = []
    p = 2
    while p * p <= number:
        k = 0
        while number % p == 0:
            k += 1
            number //= p
        if k > 0:
            result.append([p, k])
        p += 1
    if number > 1:
        result.append([number, 1])
    return result

print(factorization(int(input())))