#!/usr/bin/env python3
import sys

if len(sys.argv) < 2:
    print('File name not found, please use it as argument')
    exit()
    
if sys.argv[1] == 'help':
    print('To open file, please use it as first argument')
    exit()

dictionary = {}
try:
    with open(sys.argv[1], "r", encoding='utf-8') as f:
        for line in f:
            l = [s.strip() for s in line.replace('-',',').split(',')]
            for word in l[1:]:
                if not (word in dictionary):
                    dictionary[word] = []
                dictionary[word].append(l[0])
except IOError as e:
    print(e)
    exit()
    
try:
    with open("dict-out.txt", "w", encoding='utf-8') as f:
        d = sorted(dictionary.items())
        for t in d:
            words = str(t[1]).strip("[]").replace("'","")
            f.write(f'{t[0]} - {words}\n')
except IOError as e:
    print(e)