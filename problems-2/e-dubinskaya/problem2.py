#!/usr/bin/env python3
# путь до словаря из примера: res/en_dictionary.txt
from sys import stderr


def add_to_latin_dict(latin_dict: dict, read_str: str):
    read_str = read_str.replace(" ", "")
    read_str = read_str.replace("\n", "")
    word_meaning = read_str.split("-", 2)
    word = word_meaning[0]
    meaning = word_meaning[1].split(",")
    for i in range(len(meaning)):
        if latin_dict.get(meaning[i]) is not None:
            latin_dict[meaning[i]].append(word)
        else:
            latin_dict[meaning[i]] = [word]


print("Enter path to dictionary file: ", end="")
fileName = input()
latin = {}
try:
    f = open(fileName, 'r')
    for line in f:
        add_to_latin_dict(latin, line)
    for key in sorted(latin):
        print(key, end=' - ')
        values = latin.get(key)
        size = len(values)
        for i in range(size):
            if i == size - 1:
                print(values[i])
            else:
                print(values[i], end=', ')
except OSError as e:
    print(e, file=stderr)
