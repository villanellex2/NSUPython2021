def seq_in_range(seq, a, b):
	if b < a:
		b = a
	for i in range(0, len(seq)):
		if seq[i] < a:
			seq[i] = a
		if seq[i] > b:
			seq[i] = b

	return seq

seq = list(map(int, input().split()))

print(seq_in_range(seq, int(input()), int(input())))