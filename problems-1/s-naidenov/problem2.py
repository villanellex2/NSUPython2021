def trim_sequence(seq, a, b):
    for i in range(0, len(seq)):
        if seq[i] < a:
            seq[i] = a
        elif seq[i] > b:
            seq[i] = b
    return seq




