def to_primary_list(a: int) -> list:
    res = []
    curr_num = 2
    while a > 1:
        j = 0
        while a % curr_num == 0:
            a = a // curr_num
            j = j + 1
        if j != 0:
            res.append([curr_num, j])
        curr_num = curr_num + 1
    return res


inp = int(input())
print(to_primary_list(inp))
