from math import sqrt


def generate_primes(n):
    return [i for i in range(2, n + 1) if all(i % d for d in range(2, int(sqrt(i)) + 1))]


if __name__ == "__main__":
    n = int(input("n = "))
    print(str(generate_primes(n)))
