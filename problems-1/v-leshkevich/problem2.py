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

numbers = map(int, input().split())
a, b = map(int, input().split())
print(crop(list(numbers), a, b))
