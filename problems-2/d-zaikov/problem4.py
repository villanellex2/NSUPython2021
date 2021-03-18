#!/usr/bin/env python3
import sys
import os
from optparse import OptionParser

def find_seq(seq, path):
    cnt = 0
    pos_list = []
    
    #Оставил, так как open выдает PermissionError при чтении директории
    #(на windows)
    if os.path.isdir(path):
        raise IsADirectoryError('The entered path is not a file')
        return cnt, pos_list
    
    with open(path, 'r') as file:
        file.read(2)
        pi = file.read().replace('\n', '')
    
    
   
    pos = pi.find(seq, 0)
    while pos != -1:
        if cnt < 5:
            pos_list.append(pos)
        cnt += 1
        pos += 1
        pos = pi.find(seq, pos)
    
    return cnt, pos_list

if __name__ == '__main__':
    parser = OptionParser()
    parser.add_option("-p", "--path", dest="path",
                        help="Path to pi.txt.")
                        
    (options, args) = parser.parse_args()
    path = options.path
    if path is None:
        path = "pi.txt"
        
    print('Enter sequence to search for.')
    seq = input()
    if not seq.isdigit():
        print("Incorrect input, please use only digits.",
               file=sys.stderr)
        exit(1)
    try:
        cnt, posl = find_seq(seq, path)
    except Exception as e:
        print('Error while trying to call "open()"', file=sys.stderr)
        print(e, file=sys.stderr)
        exit(1)
    
    print(f'Found {cnt} results.')
    print(f'Positions: ', end='')
    for p in posl:
        print(p, end=', ')
    print('...')
    