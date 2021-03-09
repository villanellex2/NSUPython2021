#!/usr/bin/env python3

import sys
import os
from optparse import OptionParser

parser = OptionParser()
parser.add_option("-p", "--path", dest="dirpath",
                    help="Scan directory by path.")
                    
(options, args) = parser.parse_args()

if options.dirpath is None:
    print("Error: Directory for scan not specified, use -p to write path.",
           file=sys.stderr)
    exit(1)


try:
    ls = sorted([y for y in [os.path.join(options.dirpath, x) 
                       for x in os.listdir(options.dirpath)]
                   if os.path.isfile(y)], 
                       key=(lambda x: (-os.stat(x).st_size, x)))
    print([os.path.split(x)[-1] for x in ls])
    
except FileNotFoundError as e:
    print('Error: the entered directory for scan not found.\n', file=sys.stderr)
    print('--------More info--------', file=sys.stderr)
    print(e, file=sys.stderr)
    exit(1)
except NotADirectoryError as e:
    print('Error: the entered path for scan is not a directory.\n', file=sys.stderr)
    print('--------More info--------', file=sys.stderr)
    print(e, file=sys.stderr)
    exit(1)
except PermissionError as e:
    print('Error: you have not permission to scan the entered directory.\n', file=sys.stderr)
    print('--------More info--------', file=sys.stderr)
    print(e, file=sys.stderr)
    exit(1)
except Exception as e:
    print('Error: some error occurred while trying to scan the directory.\n', file=sys.stderr)
    print('--------More info--------', file=sys.stderr)
    print(e, file=sys.stderr)
    exit(1)
