#!/usr/bin/env python3

import argparse
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

text_parts = []
part_len = 0
previous_alpha = text[0].isalpha()
i = 1
while i < len(text):
    if previous_alpha == text[i].isalpha():
        part_len += 1
    else:
        text_parts.append(text[i - 1 - part_len: i])
        part_len = 0
        previous_alpha = not previous_alpha
    i += 1
text_parts.append(text[i - 1 - part_len: i])


def rearrange(letters):
    return sorted(letters) if args.sort else sample(letters, len(letters))


for part in text_parts:
    if len(part) > 3 and part[0].isalpha():
        print(part[0], ''.join(rearrange(part[1:-1])), part[-1], sep='', end='')
    else:
        print(part, end='')
