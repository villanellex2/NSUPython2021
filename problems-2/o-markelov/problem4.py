#!/usr/bin/env python3

from sys import argv

print_count = 5
pi_filename = argv[1] if len(argv) > 1 else 'pi.txt'

try:
    with open(pi_filename) as pi_file:
        pi_file.seek(2)
        pi_str = pi_file.read()

    pi_str = ''.join(pi_str.split())
    i_sequence = input('Enter sequence to search for.\n')

    positions_count = 0
    positions = []

    position = pi_str.find(i_sequence)
    while position != -1:
        positions_count += 1
        if positions_count <= print_count:
            positions.append(str(position))

        position = pi_str.find(i_sequence, position + 1)

    print(f'Found {positions_count} results.')
    if positions_count > 0:
        print(f'Positions: {" ".join(positions)}{" ..." if positions_count > print_count else "."}')

except OSError as e:
    print(str(e))
