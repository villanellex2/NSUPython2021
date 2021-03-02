nums = ['no', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten']

line_one = ' green bottle{} hanging on the wall,\n'
line_two = '{} one green bottle should accidentally fall{}\n'
line_three_1= "There'll be "
line_three_2 = ' green bottle{} hanging on the wall.'
   


for i in range(len(nums)-1, 0, -1):
	same_str = nums[i].capitalize() + line_one.format(
		's' if i != 1 else '')
	print(same_str 
		+ same_str 
		+ line_two.format('And if' if i != 1 else 'If that', ',' if i != 1 else '') 
		+ line_three_1 
		+ nums[i-1] 
		+ line_three_2.format('s' if i != 1 else ''))