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

except NotADirectoryError as e:
	print('You specified not a directory', file=stderr)
	print(e, file=stderr)
except FileNotFoundError as e:
	print("Can't find the specified file" , file=stderr)
	print(e, file=stderr)
except PermissionError as e:
	print("You have no Permission to use the specified path", file=stderr)
	print(e, file=stderr)
except Exception as e:
	print("Here's some error while listing specified directory", file=stderr)
	print(e, file=stderr)

