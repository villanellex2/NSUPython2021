def trim(li, a, b):
    res = []
    for elem in li:
        if elem < a:
            res.append(a)
        elif elem > b:
            res.append(b)
        else:
            res.append(elem)
    return res

nums = map(int, input().split())
a, b = map(int, input().split())

print(trim(nums, a, b))