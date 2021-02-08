nums = ['ten', 'nine', 'eight', 'seven', 'six', 
	'five', 'four', 'three', 'two', 'one', 'no']

line_one = ' green bottles hanging on the wall,\n'
line_two = 'And if one green bottle should accidentally fall,\n'
line_three_1= "There'll be "
line_three_2 = ' green bottles hanging on the wall.'

for i in range(0, len(nums)-1):
	same_str = nums[i].capitalize() + line_one
	print(same_str + same_str + line_two + line_three_1 + nums[i + 1] + line_three_2)