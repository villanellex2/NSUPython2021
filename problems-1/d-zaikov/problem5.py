def factor(n):
    if n <= 0:
        return []
    if n == 1:
        return [[2, 0]]
    ls = []
    d = 2
    k = 0
    while d * d <= n:
        if n % d == 0:
            k += 1
            n //= d
        else:
            if k > 0:
                ls.append([d, k])
            k = 0
            d += 1
    if k > 0:
        ls.append([d, k])
    if n > 1:
        if len(ls) > 0 and ls[-1][0] == n:
            ls[-1][1] += 1
        else:
            ls.append([n, 1])
    
    return ls
    
print(factor(int(input())))