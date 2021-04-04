#!/usr/bin/env python3.8

import random
import re
import sys


def shuffle_chars(word: str) -> str:
    if len(word) > 3:
        positions = list(range(1, len(word) - 1))
        random.shuffle(positions)
        return word[0] + ''.join(map(lambda x: word[x], positions)) + word[len(word) - 1]
    return word


def sort_chars(word: str) -> str:
    if len(word) > 3:
        positions = list(range(1, len(word) - 1))
        list.sort(positions, key=lambda x: word[x])
        return word[0] + ''.join(map(lambda x: word[x], positions)) + word[len(word) - 1]
    return word


if __name__ == '__main__':
    filename = 'example.txt'
    processing_function = shuffle_chars
    if len(sys.argv) > 3:
        raise ValueError("Too many arguments")
    if len(sys.argv) > 1:
        if sys.argv[1] == '--sorted':
            processing_function = sort_chars
            if len(sys.argv) == 3:
                filename = sys.argv[2]
        else:
            if len(sys.argv) != 2:
                print(sys.argv)
                raise ValueError("Too many arguments")
            filename = sys.argv[1]

    fp = open(filename, 'r')
    line = fp.readline()
    while line:
        words = re.split(r'[`\-=~!@#$%^&*()_+\[\]{};\'\\:"|<,./<>? \t\n\r]', line)
        print(' '.join(map(processing_function, words)))
        line = fp.readline()
