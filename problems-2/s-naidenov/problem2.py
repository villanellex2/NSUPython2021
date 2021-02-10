import re


dictionary = {}
file_path = input()
with open(file_path, 'r', encoding='utf-8') as source:
    for line in source:
        s = re.findall(r"[\w']+", line)
        for word in s[1:]:
            if not (word in dictionary.keys()):
                dictionary[word] = [s[0]]
            else:
                dictionary[word].append(s[0])
    keys = sorted(list(dictionary.keys()))
    for k in keys:
        print(k + " - " + str(dictionary[k]))
