#!/usr/bin/env python3

import unittest
from problem1 import Timer
from time import sleep


def do_some_long_stuff(seconds):
    sleep(seconds)


class TestTimer(unittest.TestCase):
    def test_time(self):
        timer = Timer()
        seconds = 1
        with timer.timer():
            do_some_long_stuff(seconds)
        self.assertEqual(timer.exec_time, seconds * 1000)


if __name__ == '__main__':
    unittest.main()
