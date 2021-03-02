bottles = ' green bottle{s} sitting on the wall{comma}'
numbers = ['Ten', 'Nine', 'Eight', 'Seven', 'Six',
           'Five', 'Four', 'Three', 'Two', 'One', 'No']

for i in range(10):
    print(numbers[i] + bottles.format(s='s' if i != 9 else '', comma=','))
    print(numbers[i] + bottles.format(s='s' if i != 9 else '', comma=','))
    print('And if one green bottle should accidentally fall')
    print('There would be ' + numbers[i+1].lower() + bottles.format(
        s='s' if (i+1) != 9 else '', comma=''), end='.\n\n')
