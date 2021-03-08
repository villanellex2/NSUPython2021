#!/usr/bin/env python3

bottles = ['Ten', 'Nine', 'Eight', 'Seven', 'Six', 'Five', 'Four', 'Three', 'Two', 'One', 'No']
line = ' green bottle{s} sitting on the wall'

def add_S_Or_Not(i):
    if (i) != 9:
        return 's'
    else:
        return ''

if __name__ == '__main__':
    for i in range(10):
        print(bottles[i] + line.format(s=add_S_Or_Not(i)) + ',')
        print(bottles[i] + line.format(s=add_S_Or_Not(i)) + ',')
        print('And if one green bottle should accidentally fall')
        print('There would be ' + bottles[i + 1].lower() + line.format(s=add_S_Or_Not(i+1)), end='.\n\n')

