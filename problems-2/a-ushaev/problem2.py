#!/usr/bin/env python3

with open('problem2.txt', 'r') as f:
    defs = {}
    for ln in f.readlines():
        eng, latin = ln.rstrip().split(' - ')
        for wds in latin.split(', '):
            if wds in defs:
                defs[wds].append(eng)
            else:
                defs[wds] = [eng]
                
    for latin, eng in sorted(defs.items()):
        print(f'{latin} - {", ".join(eng)}') 