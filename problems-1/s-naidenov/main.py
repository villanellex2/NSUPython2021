from problem2 import trim_sequence
if __name__ == '__main__':
    s = input("seq = ").split(" ")
    a = int(input("min = "))
    b = int(input("max = "))
    seq = []
    for i in s:
        seq.append(int(i))
    print(str(trim_sequence(seq, a, b)))