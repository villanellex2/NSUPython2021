from math import sqrt, ceil


def expand_number(n):
    max_factor = ceil(sqrt(n))
    factors = []
    cur_factor = 2
    while cur_factor <= max_factor:
        counter = 0
        while n % cur_factor == 0:
            counter += 1
            n //= cur_factor
        if counter > 0:
            factors.append([cur_factor, counter])
        cur_factor += 1
    if n > 1:
        factors.append([n, 1])
    return factors


if __name__ == "__main__":
    n = int(input("n = "))

    print(str(expand_number(n)))
