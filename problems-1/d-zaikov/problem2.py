def trim(seq, a, b):
    res = []
    for i in seq:
        t = i
        if i < a:
            t = a
        elif i > b:
            t = b
        res.append(t)
    return res
    
test_seq = [int(x) for x in input().split()]
a_test = int(input())
b_test = int(input())
print(trim(test_seq, a_test, b_test))   
   