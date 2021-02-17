#!/usr/bin/env python3

from os import listdir, stat
from os.path import isfile, join, exists
from sys import argv, exit, stderr

from operator import itemgetter

try:
	if len(argv) != 2:
		print("Should be the dir path as the only argument", file=stderr)
	else:
		files = []
		for name in listdir(argv[1]):
			full_path = join(argv[1], name)
			if isfile(full_path): 
				files.append((name, stat(full_path).st_size))

		for name, size in sorted(files, key=itemgetter(1, 0), reverse=True):
			print(name, size)

except (NotADirectoryError, FileNotFoundError):
	print('You must specify dir path', file=stderr)
