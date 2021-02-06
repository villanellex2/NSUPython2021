def cumsum(seq=[]):
    res = [0]
    cursum = 0
    for i in seq:
        cursum += i
        res += [cursum]
    return res