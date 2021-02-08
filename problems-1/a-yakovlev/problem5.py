def prime_multipliers(num):
	res = []
	power = 0
	curr_del = 2
	while num != 1:
		while num % curr_del == 0:
			num //= curr_del
			power += 1
		if power > 0:
			res.append([curr_del, power])
			power = 0
		if curr_del == 2:
			curr_del += 1
		else:
			curr_del += 2

	return res