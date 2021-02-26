#!/usr/bin/env python3

from os import listdir, stat
from os.path import isfile, join
from sys import argv

dir_path = argv[1] if len(argv) > 1 else '.'

try:
    files_info = []

    for filename in listdir(dir_path):
        full_filename = join(dir_path, filename)
        if isfile(full_filename):
            files_info.append((filename, stat(full_filename).st_size))

    if not files_info:
        print('No files')
        exit()

    for file_info in sorted(files_info, key=lambda info: (-info[1], info[0])):
        print(file_info[0], ' - ', file_info[1], 'bytes')

except OSError as e:
    print(f'Cannot open "{dir_path}" ({e.strerror})')
