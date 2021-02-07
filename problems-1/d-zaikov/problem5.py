def factor(n):
    ls = []
    d = 2
    while d * d <= n:
        if n % d == 0:
            ls.append(d)
            n //= d
        else:
            d += 1
    if n > 1:
        ls.append(n)
    res = []
    for i in set(ls):
        res.append([i, ls.count(i)])
    
    return res