#!/usr/bin/env python3

bottles = ['Ten', 'Nine', 'Eight', 'Seven', 'Six', 'Five', 'Four', 'Three', 'Two', 'One', 'No']
line = ' green bottle{s} sitting on the wall'

def add_S_Or_Not(i):
    if (i + 1) != 9:
        return 's'
    else:
        return ''


for i in range(10):
    print(bottles[i] + line.format(s='s' if i != 9 else '') + ',')
    print(bottles[i] + line.format(s='s' if i != 9 else '') + ',')
    print('And if one green bottle should accidentally fall')
    print('There would be ' + bottles[i + 1].lower() + line.format(s=add_S_Or_Not(i)), end='.\n\n')

