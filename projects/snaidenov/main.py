#!/usr/bin/env python3.7
import sys
from argparse import ArgumentParser

from modules.controller import Controller
from modules.model import Model
from modules.view import View


def main():
    parser = ArgumentParser()
    parser.add_argument('--cfg_path', nargs='?', help="Path to file with Life 1.06 config",
                        default=None)
    parser.add_argument('--color', nargs='?', help="Initial color",
                        default=None)
    options = parser.parse_args()
    rects = set()
    if options.cfg_path is not None:
        try:
            with open(options.cfg_path) as f:
                first_line = f.readline()
                for line in f:
                    line = line.strip()
                    res = list(map(int, line.split()))
                    rects.add((res[0] + 3, res[1] + 3))
        except FileNotFoundError as e:
            print("Error while opening config file.", file=sys.stderr)
            print(e, file=sys.stderr)
            sys.exit()
    model = Model(rects)
    view = View(model)
    if options.color is not None:
        view.cur_color = options.color
        view.switch_color = False
    model.view = view
    controller = Controller(model)
    controller.run()

if __name__ == "__main__":
    main()