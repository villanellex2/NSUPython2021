def collatz(number):
    while number != 1:
        print(number, end=' -> ')
        if number % 2 == 0:
            number //= 2
        else:
            number = 3 * number + 1
    print(number)
