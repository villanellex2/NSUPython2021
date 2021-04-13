#!/usr/bin/env python3

from os import listdir, stat
from os.path import isfile, join, exists
from sys import argv, exit, stderr

from operator import itemgetter


if len(argv) != 2:
	print("Error: Should be the dir path as the only argument", file=stderr)
	exit(1)


files = []
try:
	dir_l = listdir(argv[1])
except Exception as e:
	print("Error while calling os.listdir for directory", file=stderr)
	print(e, file=stderr)
	exit(1)
try:
	for name in dir_l:
		full_path = join(argv[1], name)
		if isfile(full_path): 
			files.append((name, stat(full_path).st_size))
except Exception as e:
	print("Error while calling os.stat for directory:", file=stderr)
	print(e, file=stderr)
	exit(1)

for name, size in sorted(files, key=itemgetter(1, 0), reverse=True):
	print(name, size)


