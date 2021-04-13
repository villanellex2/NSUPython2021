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


def createDictionary(inp: str) -> str:
    latin = {}
    res = ""
    for line in inp.split("\n"):
        add_to_latin_dict(latin, line)
    for key in sorted(latin):
        values = latin.get(key)
        res += key + " - " + ", ".join(values) + "\n"
    return res


if __name__ == "__main__":
    print("Enter path to dictionary file: ", end="")
    fileName = input()
    try:
        f = open(fileName, 'r')
        print(createDictionary(f.read()))
    except OSError as e:
        print(e, file=stderr)
