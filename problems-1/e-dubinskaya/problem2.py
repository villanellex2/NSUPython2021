def cut(nums, a, b):
    for i in range(len(nums)):
        if nums[i] < a:
            nums[i] = a
        elif nums[i] > b:
            nums[i] = b
    return nums


inp = list(map(int, input().split()))
bound = list(map(int, input().split()))
print(cut(inp, bound[0], bound[1]))
