#!/usr/bin/env python3

from os import listdir, stat
from os.path import isfile, join
from sys import argv

files_info = []

for filename in listdir(argv[1]):
    full_filename = join(argv[1], filename)
    if isfile(full_filename):
        files_info.append((filename, stat(full_filename).st_size))

for file_info in sorted(files_info, key=lambda info: (-info[1], info[0])):
    print(file_info[0], ' - ', file_info[1], 'bytes')
