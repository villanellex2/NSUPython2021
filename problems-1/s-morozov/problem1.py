def cumulative_sum(numbers):
  ans = [0]
  for n in numbers:
    ans.append(n + ans[-1])
  return ans

numbers = map(int, input().split())
print(cumulative_sum(numbers))