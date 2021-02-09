from math import sqrt


def is_prime(n):
    if n < 2:
        return False
    max_factor = int(sqrt(n))
    return all(n % i for i in range(2, max_factor + 1))


def generate_primes(n):
    return [i for i in range(2, n + 1) if is_prime(i)]


if __name__ == "__main__":
    n = int(input("n = "))
    print(str(generate_primes(n)))
