def cumsum(seq=[]):
    res = [0]
    cursum = 0
    for i in seq:
        cursum += i
        res.append(cursum)
    return res
    
test_seq = [int(x) for x in input().split()]
print(cumsum(test_seq))