def print_green_bottles_text():
    numbers = ['ten', 'nine', 'eight', 'seven', 'six',
               'five', 'four', 'three', 'two', 'one', 'no']
    hanging_text = " green bottles hanging on the wall"
    i = 0
    for number in numbers[:10]:
        i = i + 1
        print(number.title() + hanging_text, end=',\n')
        print(number.title() + hanging_text, end=',\n')
        print("{text} one green bottle should accidentally fall,\nThere'll be "
              .format(text="And if" if i < 10 else "If that") + numbers[i] + hanging_text, end='.\n')

print_green_bottles_text()