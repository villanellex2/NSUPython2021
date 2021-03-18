#!/usr/bin/env python3

import sys
import os
from argparse import ArgumentParser

parser = ArgumentParser()
parser.add_argument("-p", "--path", dest="dirpath",
                    help="Scan directory by path.")
                    
options = parser.parse_args()

if options.dirpath is None:
    print("Error: Directory for scan not specified, use -p to write path.",
           file=sys.stderr)
    exit(1)


try:
    dir_l = os.listdir(options.dirpath)
except Exception as e:
    print('Error while calling "os.listdir" for directory', file=sys.stderr)
    print(e, file=sys.stderr)
    exit(1)
try:
    ls = sorted([y for y in [os.path.join(options.dirpath, x) 
                       for x in dir_l]
                   if os.path.isfile(y)], 
                       key=(lambda x: (-os.stat(x).st_size, x)))
                       
    print([os.path.split(x)[-1] for x in ls])
except Exception as e:
    print('Error while calling "os.stat" for a file in the directory:', file=sys.stderr)
    print(e, file=sys.stderr)
    exit(1)
