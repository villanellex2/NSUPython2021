#!/usr/bin/env python3

from os import listdir, stat
from os.path import isfile, join
from sys import argv

if len(argv) < 2:
    print('You haven\'t passed the path argument')
    exit()

try:
    files_info = []

    for filename in listdir(argv[1]):
        full_filename = join(argv[1], filename)
        if isfile(full_filename):
            files_info.append((filename, stat(full_filename).st_size))

    if not files_info:
        print('No files')
        exit()

    for file_info in sorted(files_info, key=lambda info: (-info[1], info[0])):
        print(file_info[0], ' - ', file_info[1], 'bytes')

except OSError as e:
    print(f'Cannot open "{argv[1]}" ({e.strerror})')
