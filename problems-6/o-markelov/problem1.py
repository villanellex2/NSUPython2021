#!/usr/bin/env python3

import argparse
import re
import sys
from random import sample

parser = argparse.ArgumentParser()
parser.add_argument('-t', '--text', help='text data')
parser.add_argument('-f', '--file', help='file with text data')
parser.add_argument('-s', '--sort', help='sort inner letters of the words instead of shuffling', action='store_true')
args = parser.parse_args()

if args.text:
    text = args.text
elif args.file:
    try:
        with open(args.file, 'r', encoding='utf8') as file:
            text = file.read()
    except OSError as e:
        sys.stderr.write(str(e))
        exit()
else:
    sys.stderr.write('You must provide either some text or some file')
    exit()


def rearrange(letters):
    return sorted(letters) if args.sort else sample(letters, len(letters))


for part in re.split('([^\\W\\d_]+)', text):
    if len(part) > 3 and part[0].isalpha():
        print(part[0], ''.join(rearrange(part[1:-1])), part[-1], sep='', end='')
    else:
        print(part, end='')
