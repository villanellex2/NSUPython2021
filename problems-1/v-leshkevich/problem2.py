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
