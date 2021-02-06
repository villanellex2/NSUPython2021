import re

if __name__ == '__main__':
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
        sorted_dictionary = {k: dictionary[k] for k in sorted(dictionary)}
        for k in sorted_dictionary:
            print(k + " - " + str(dictionary[k]))
