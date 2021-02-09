def generate_triples(n):
    res = []
    max_n = int(n * (2 ** 0.5)) + 1
    squares = [x * x for x in range(max_n + 1)]
    squares_to_numbers = dict([(squares[i], i) for i in range(max_n + 1)])
    for x in range(1, n):
        sqr_x = squares[x]
        for y in range(x, n + 1):
            sqr_y = squares[y]
            z = squares_to_numbers.get(sqr_x + sqr_y)
            if z is not None:
                res.append([x, y, z])
    return res


if __name__ == '__main__':
    try:
        n = int(input("n = "))
        print([x for x in generate_triples(n)])
    except ValueError:
        print("Invalid value")
