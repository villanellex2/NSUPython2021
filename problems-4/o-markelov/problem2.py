#!/usr/bin/env python3

import argparse
import sys

parser = argparse.ArgumentParser()
parser.add_argument("file", help="file to translate")
parser.add_argument("old_symbols", help="symbols to be replaced with the new ones")
parser.add_argument("new_symbols", help="symbols to replace the old ones")
parser.add_argument("-d", "--delete", help="symbols to delete")
args = parser.parse_args()

if len(args.old_symbols) != len(args.new_symbols):
    sys.stderr.write('"old_symbols" and "new_symbols" have different lengths')
    exit()

if len(args.old_symbols) != len(set(args.old_symbols)):
    sys.stderr.write('"old_symbols" must not contain duplicate symbols')
    exit()

translate_table = dict(zip(args.old_symbols, args.new_symbols))
delete_set = set(args.delete) if args.delete else set()

try:
    with open(args.file, 'r', encoding='utf8') as file:
        while True:
            symbol = file.read(1)

            if not symbol:
                break

            if symbol in delete_set:
                continue

            if symbol in translate_table:
                symbol = translate_table[symbol]

            print(symbol, end='')
except OSError as e:
    sys.stderr.write(str(e))
