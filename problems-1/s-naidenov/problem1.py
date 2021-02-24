def cum_sum(l):
    res = []
    cur_sum = 0
    res.append(cur_sum)
    for i in l:
        cur_sum += i
        res.append(cur_sum)
    return res


if __name__ == '__main__':
    s = input().split(" ")
    l = []
    for i in s:
        l.append(int(i))
    print(str(cum_sum(l)))