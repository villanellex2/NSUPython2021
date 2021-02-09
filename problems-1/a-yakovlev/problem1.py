def sums(seq=[]):

	out = [0]

	for i in seq:
		out.append(out[-1] + int(i))

	return out


print(sums(input().split()))
