def test_hypothesis(n):
    seq = []
    while n != 1:
        seq.append(n)
        if n % 2 == 0:
            n //= 2
        else:
            n = 3 * n + 1
    seq.append(n)
    return seq


try:
    n = int(input("n = "))
    print(str(test_hypothesis(n)))
except ValueError:
    print("n is not natural number")
