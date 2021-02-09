
def cumulative_sum(list):
    res = [0]
    curr_sum = 0
    for elem in list:
        curr_sum += elem
        res.append(curr_sum)
    return res


input = list(map(int, input().split()))
print(cumulative_sum(input))
