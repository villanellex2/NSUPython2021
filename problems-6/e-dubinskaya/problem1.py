#!/usr/bin/env python3
import argparse
import re
import sys
import random


def sort_word(elem: str) -> str:
    if len(elem) == 1:
        red = re.match(r"[,.;:\"\'!)]", elem)
        if red is not None and red.pos >= 0:
            return elem
        else:
            return " " + elem
    else:
        return " " + "".join(sorted(elem))


def random_word(elem: str) -> str:
    if len(elem) <= 2:
        red = re.match(r"[^\w\s]", elem)
        if red is not None and red.pos >= 0:
            return elem
        else:
            return " " + elem
    else:
        arr = list(elem)
        return " " + elem[0] + "".join(random.sample(arr[1:-1], len(arr) - 2)) + elem[len(elem) - 1]


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-s', '--sort')
    parser.add_argument('-r', '--random')

    args = parser.parse_args()
    fun = sort_word
    file = ""

    if args.sort:
        fun = sort_word
        file = args.sort
    elif args.random:
        file = args.random
        fun = random_word
    else:
        print("No flag set, you should use -s or -r", file=sys.stderr)
        exit()

    try:
        f = open(file, 'r')
        line = f.readline()
        while line:
            words = re.findall(r"\w+|[^\w\s]", line)
            print(''.join(map(fun, words)), end="")
            line = f.readline()
            print()

    except OSError as e:
        print(e, file=sys.stderr)
