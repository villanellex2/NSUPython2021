def prime_multipliers(num):
	first_num = num
	res = []
	for curr_del in range(2, int(num**(1/2)) + 1):
		power = 0
		while num % curr_del == 0:
			num //= curr_del
			power += 1
		if power > 0:
			res.append([curr_del, power])

	if num != 1: res.append([num, 1])
	return res 


print(prime_multipliers(int(input("Enter some number "))))