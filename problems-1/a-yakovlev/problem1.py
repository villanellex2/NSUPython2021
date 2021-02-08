def sums(seq=[]):

	out = [0]
	cursum = 0

	for i in seq:
		cursum += i
		out.append(cursum)

	return out