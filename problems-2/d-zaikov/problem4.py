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
    except FileNotFoundError as e:
        print('Error: the entered path to the file with pi number not found.\n', file=sys.stderr)
        print('--------More info--------', file=sys.stderr)
        print(e, file=sys.stderr)
        exit(1)
    except IsADirectoryError as e:
        print('Error: the entered path to the file with pi number is not a file.\n', file=sys.stderr)
        print('--------More info--------', file=sys.stderr)
        print(e, file=sys.stderr)
        exit(1)
    except PermissionError as e:
        print('Error: you have not permission to read the file with pi number by the entered path.\n', file=sys.stderr)
        print('--------More info--------', file=sys.stderr)
        print(e, file=sys.stderr)
        exit(1)
    except Exception as e:
        print('Error: some error occurred while trying to read the file with pi number.\n', file=sys.stderr)
        print('--------More info--------', file=sys.stderr)
        print(e, file=sys.stderr)
        exit(1)
    print(f'Found {cnt} results.')
    print(f'Positions: ', end='')
    for p in posl:
        print(p, end=', ')
    print('...')
    