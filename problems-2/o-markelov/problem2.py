#!/usr/bin/env python3

with open(input('Enter the filename:\n')) as file:
    dictionary = {}

    for line in file:
        word, translations = line.rstrip().split(' - ')
        for translation in translations.split(', '):
            if translation not in dictionary:
                dictionary[translation] = [word]
            else:
                dictionary[translation].append(word)

    for translation, word in sorted(dictionary.items()):
        print(f'{translation} - {", ".join(sorted(word))}')
