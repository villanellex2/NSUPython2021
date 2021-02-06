import os
import sys
from operator import itemgetter


def find_files(path):
    names = os.listdir(path)
    res = []
    for n in names:
        full_path = os.path.join(path, n)
        if os.path.isfile(full_path):
            size = os.path.getsize(full_path)
            res.append([n, size])
    return res


if __name__ == "__main__":
    if len(sys.argv) < 2 or not os.path.exists(sys.argv[1]):
        print("Directory name was not found", file=sys.stderr)
        sys.exit(-1)
    res = find_files(sys.argv[1])
    res = sorted(res, key=itemgetter(1, 0), reverse=True)
    for f in res:
        print(f[0] + " " + str(f[1]))
