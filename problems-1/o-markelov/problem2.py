def crop(nums, a, b):
    for i in range(len(nums)):
        if nums[i] < a:
            nums[i] = a
        elif nums[i] > b:
            nums[i] = b


i_nums = [int(x) for x in input('Enter the numbers (space separated):\n').split()]
i_bounds = [int(x) for x in input('Enter the bounds (space separated):\n').split()]

crop(i_nums, i_bounds[0], i_bounds[1])
print(i_nums)
