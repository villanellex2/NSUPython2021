nums = ['ten', 'nine', 'eight', 'seven', 'six', 
        'five', 'four', 'three', 'two', 'one', 'no']
line1 = ' green bottles hanging on the wall,'
line2 = 'And if one green bottle should accidentally fall,'
line3_1 = "There'll be "
line3_2 = ' green bottles hanging on the wall.'
for i in range(0,10):
    print(nums[i].title() + line1)
    print(nums[i].title() + line1)
    print(line2)
    print(line3_1 + nums[i + 1] + line3_2)
    
    