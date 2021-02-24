#!/usr/bin/env python3

nums = ["no", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten"]

for i in range(10, 0, -1):
  for j in range(2):
    print(nums[i].capitalize() + " green bottle" + ("" if i == 1 else "s") + " hanging on the wall,")
  print(("If that" if i == 1 else "And if") + " one green bottle should accidentally fall,")
  print("There'll be " + nums[i - 1] +  " green bottle" + ("" if i == 2 else "s") + " hanging on the wall.")
