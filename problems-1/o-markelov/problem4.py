nums = ['no', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten']

for i in range(10, 0, -1):
    line_1_2 = f'{nums[i].capitalize()} green bottle{"s" if i != 1 else ""} hanging on the wall,'
    for _ in range(2):
        print(line_1_2)
    print(f'{"And if" if i > 1 else "If that"} one green bottle should accidentally fall,')
    print(f'There’ll be {nums[i-1]} green bottle{"s" if i != 2 else ""} hanging on the wall.')
