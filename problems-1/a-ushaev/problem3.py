def collatz(n):
    res = [n]
    num = n
    while num > 1:
        num = (num // 2) if num % 2 == 0 else (3 * num + 1)
        res.append(num) 
    return res

def chain_printer(li):
    print(' -> '.join(str(x) for x in li))

chain_printer(collatz(int(input())))
