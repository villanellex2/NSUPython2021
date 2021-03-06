#!/usr/bin/env python3

import argparse
import re
import sys
from random import sample

parser = argparse.ArgumentParser(description='Shuffle the letters of the words of the input text')
parser.add_argument('-t', '--text', type=str, help='text to shuffle')
parser.add_argument('-f', '--file', type=str, help='file with text')
parser.add_argument('-s', '--sort', help='sort letters instead of shuffling', action='store_true')
args = parser.parse_args()

if args.file:
    try:
        with open(args.file, 'r', encoding='utf8') as f:
            data = f.read()
    except OSError as err:
        print(str(e), file=sys.stderr)
elif args.text:
    data = args.text
else:
    parser.print_help(sys.stderr)
    exit(0)

def garble(text: str) -> str:
    return ''.join(sorted(text) if args.sort else sample(text, len(text)))

tokens = re.findall(r"[^\d\W]+|[\d\W]", data)
for t in tokens:
    if len(t) > 3 and t.isalpha():
        print(f"{t[0]}{garble(t[1:-1])}{t[-1]}", end='')
    else:
        print(t, end='')