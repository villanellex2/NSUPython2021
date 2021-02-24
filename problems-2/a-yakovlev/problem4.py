#!/usr/bin/env python3

seq = input('Enter seq: ')

cnt = 0
first_five = []


with open('pi.txt', 'r') as pi:
    str_pi = ''.join(pi.read()[2:].split())

cur_pos = str_pi.find(seq)
while cur_pos != -1:
    if cnt < 5:
        first_five.append(str(cur_pos))
    cnt += 1
    cur_pos = str_pi.find(seq, cur_pos+1)

print(f'Found {cnt} results.\nPositions: {" ".join(first_five)} ...')
