#!/usr/bin/env python3

try:
	n = int(input())
	square = {i: i*i for i in range(1, n+1)}

	print ([
			(x, y, int((square[x] + square[y])**(1/2)) ) 
			for x in square.keys()
			for y in square.keys()
			if y < x and square[x] + square[y] in square.values()
		]
	)

except ValueError:
	print('You did not enter an integer')


