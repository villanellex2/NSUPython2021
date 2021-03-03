#!/usr/bin/env python3
import re


def find_all_link(inp: str):
    res = []
    while True:
        min_link = re.search(r'\b(?:http://|https://|www\.)[a-zA-Z0-9\.\/_~:?#\[\]@!$&\'\(\)*+,;=]+\b', inp)
        if min_link is not None:
            link = inp[min_link.start():min_link.end()]
            if min_link.start() == 0 or re.search(r'\s', inp[min_link.start() - 1]) is not None:
                # проверяем на то, не обрезали ли мы этой ссылкой что-то некорректное
                if len(inp) <= min_link.end() + 1 or \
                        (len(inp) > min_link.end() + 1 and
                         re.search(r'\s', inp[min_link.end()]) is not None):
                    res.append(link)
            inp = inp[min_link.end():]
        else:
            return res


if __name__ == "__main__":
    print("Input text.")
    inp = input()
    print(find_all_link(inp))
