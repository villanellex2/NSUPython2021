#!/usr/bin/env python3

import sys
import os

if len(sys.argv) < 2:
    print('Directory path not found, please use it as argument')
    exit()

if sys.argv[1] == 'help':
    print('Please use directory path as first argument')
    exit()
try:
    ls = sorted([y for y in [os.path.join(sys.argv[1], x) 
                       for x in os.listdir(sys.argv[1])]
                   if os.path.isfile(y)], 
                       key=(lambda x: (-os.stat(x).st_size, x)))
    print([os.path.split(x)[-1] for x in ls])
except IOError as e:
    print(e)