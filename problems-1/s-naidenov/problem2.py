def trim_sequence(seq, a, b):
    for i in range(0, len(seq)):
        if seq[i] < a:
            seq[i] = a
        elif seq[i] > b:
            seq[i] = b
    return seq


if __name__ == "__main__":
    s = input("seq = ").split(" ")
    a = int(input("min = "))
    b = int(input("max = "))
    seq = []
    for i in s:
        seq.append(int(i))
    print(str(trim_sequence(seq, a, b)))
