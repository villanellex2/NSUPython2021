#!/usr/bin/env python3

di = {}

file_path = input()

try:
	with open(file_path, 'r') as eng_to_lat:	
		for line in eng_to_lat.readlines():
			eng, lat = line.strip().split(' - ')
			for words in lat.split(', '):
				if words in di:
					di[words].append(eng)
				else:
					di[words] = [eng]

	for lat in sorted(di.keys()):
		print(lat, ', '.join(di[lat]), sep=' - ')

except FileNotFoundError:
	print("File not found")