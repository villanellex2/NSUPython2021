num = int(input())

while num != 1:
	print(num, end='->')
	if num % 2 == 0:
		num //= 2
	else:
		num = 3 * num + 1

print(num)
