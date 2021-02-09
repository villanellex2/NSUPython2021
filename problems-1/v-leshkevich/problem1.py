def cusum(_list):
    total_sum = 0
    result = [0]
    for num in _list:
        total_sum += num
        result.append(total_sum)
    return result

print(cusum(list(map(int, input().split()))))