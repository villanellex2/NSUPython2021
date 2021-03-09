#!/usr/bin/env python3
import unittest
import sys
import os
from optparse import OptionParser

def find_seq(seq, path):
    cnt = 0
    pos_list = []
    
    #Оставил, так как open выдает PermissionError при чтении директории
    #(на windows)
    if os.path.isdir(path):
        raise IsADirectoryError
        return cnt, pos_list
    
    with open(path, 'r') as file:
        pi = file.read()[2:].replace('\n', '')
    
    
   
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
    except FileNotFoundError:
        print('File not found', 
               file=sys.stderr)
        exit(1)
    except IsADirectoryError:
        print('Path is not a file',
               file=sys.stderr)
        exit(1)
    except PermissionError:
        print("Permission denied.",
               file=sys.stderr)
        exit(1)
    except Exception as e:
        print(e, file=sys.stderr)
    print(f'Found {cnt} results.')
    print(f'Positions: ', end='')
    for p in posl:
        print(p, end=', ')
    print('...')
    