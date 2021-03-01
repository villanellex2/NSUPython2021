#!/usr/bin/env python3

import re
from collections import defaultdict

path = input('Enter path to file.\n')
dictionary = defaultdict(list)

try:
    with open(path, 'r') as file:
        for line in file.readlines():
            result = re.split(" - |, ", line)
            result[-1] = result[-1].rstrip('\r\n')
            value = result.pop(0)
            for key in result:
                dictionary[key].append(value)

    for key, value in sorted(dictionary.items()):
        print(key + ' -', ', '.join(value))

except FileNotFoundError:
    print("Can not find file with given path.")
