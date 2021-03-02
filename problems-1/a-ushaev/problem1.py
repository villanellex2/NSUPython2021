def cumsum(li):
    res = [0]
    total = 0
    for elem in li:
        total += elem
        res.append(total)
    return res

inp = list(map(int, input().split()))
print(cumsum(inp))