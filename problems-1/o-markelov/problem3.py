i_num = int(input('Enter some positive number:\n'))

if i_num < 1:
    print('The number must be positive')
else:
    while i_num != 1:
        print(i_num, '→', end=' ')
        i_num = (i_num // 2) if (i_num % 2 == 0) else (3 * i_num + 1)
    print(1)
