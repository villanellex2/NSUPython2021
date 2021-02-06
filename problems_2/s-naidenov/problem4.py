def count_substrings_in_text(p):
    file_path = input("File path ")
    count = 0

    with open(file_path, 'r', encoding='utf-8') as source:
        seq = input("sequence to find ")
        pos_in_text = 0
        for line in source:
            str_len = len(line) - 1
            i = -1
            while True:
                i = line.find(seq, i + 1)
                if i == -1:
                    break
                count += 1
                p.append(i + pos_in_text)
            pos_in_text += str_len
    return count


if __name__ == '__main__':
    positions = []
    res = count_substrings_in_text(positions)
    print("Found " + str(res))
    print("Positions " + str(positions[:5]))
