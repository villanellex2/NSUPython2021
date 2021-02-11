#!/usr/bin/env python3

with open('pi.txt', 'r') as pi:
    print('Enter sequence to search for:')
    seq = input()

    digits = ''.join(pi.read()[2:].split('\n'))
    match = []
    match_cnt = 0
    cur_pos = digits.find(seq, 0)
    while cur_pos != -1:
        if match_cnt < 5:
            match.append(cur_pos)
        match_cnt += 1
        cur_pos += 1
        cur_pos = digits.find(seq, cur_pos)

    print(f'Found {match_cnt} results.')
    print(f'Positions: {" ".join(map(str, match))} ...')