def cut(seq=[], a=0, b=0):
    if b < a:
        b = a
    res = []
    for i in seq:
        if i < a:
            res.append(a)
        elif i > b:
            res.append(b)
        else:
            res.append(i)
    return res