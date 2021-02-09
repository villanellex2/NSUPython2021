def crop(_list, a, b):
    result = []
    for num in _list:
        if num < a:
            result.append(a)
        elif num > b:
            result.append(b)
        else:
            result.append(num)
    return result

a, b = map(int, input().split())
print(crop(list(map(int, input().split())), a, b))