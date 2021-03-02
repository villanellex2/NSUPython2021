#!/usr/bin/env python3

import sys
import os
from optparse import OptionParser

parser = OptionParser()
parser.add_option("-p", "--path", dest="dirpath",
                    help="Scan directory by path.")
                    
(options, args) = parser.parse_args()

if options.dirpath is None:
    print("Directory not specified, use -p to write path.",
           file=sys.stderr)
    exit()
    
if not os.path.exists(options.dirpath):
    print('Directory not found', 
           file=sys.stderr)
    exit(1)
    
if not os.path.isdir(options.dirpath):
    print("Path is not a directory.",
           file=sys.stderr)
    exit(1)

if not os.access(options.dirpath, os.X_OK | os.R_OK):
    print("Permission denied.",
           file=sys.stderr)
    exit(1)


try:
    ls = sorted([y for y in [os.path.join(options.dirpath, x) 
                       for x in os.listdir(options.dirpath)]
                   if os.path.isfile(y)], 
                       key=(lambda x: (-os.stat(x).st_size, x)))
    print([os.path.split(x)[-1] for x in ls])
    
except OSError as e:
    print(e, file=sys.stderr)