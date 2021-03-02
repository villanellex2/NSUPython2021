numbers = ["no", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten"]
wall = " green bottles standing on a wall"
comma = ","
dot = "."

for i in range(10, 0, -1):
    print(numbers[i].title() + wall + comma)
    print(numbers[i].title() + wall + comma)
    print("And if " + numbers[1] + " green bottle should accidentally fall,")
    print("There’ll " + numbers[i-1] + wall + dot)
    print()
