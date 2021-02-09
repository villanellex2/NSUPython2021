nums = ['ten', 'nine', 'eight', 'seven', 'six', 
        'five', 'four', 'three', 'two', 'one', 'no']
line1 = ' green bottle'
line1_1 = ' hanging on the wall,'
line2 = 'And if one green bottle should accidentally fall,'
line3 = "There'll be "
line3_1 = ' green bottle'
line3_2 = ' hanging on the wall.'
for i in range(0,10):
    s = 's' if i != 9 else ''
    print(nums[i].title() + line1 + s + line1_1)
    print(nums[i].title() + line1 + s + line1_1)
    print(line2)
    print(line3 + nums[i + 1] + line3_1 + ('s' if i + 1 != 9 else '') + line3_2)
    
    