def get_cum_sum(nums):
    cum_sum_nums = [0]

    for num in nums:
        cum_sum_nums.append(cum_sum_nums[-1] + num)

    return cum_sum_nums


print(get_cum_sum([int(x) for x in input('Enter the numbers (space separated):\n').split()]))
