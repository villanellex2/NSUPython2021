#!/usr/bin/env python3

import unittest
from problem1 import Timer
from time import sleep


def do_some_long_stuff(seconds):
    sleep(seconds)


class TestTimerClass(unittest.TestCase):
    def test_time(self):
        timer = Timer()
        with timer:
            do_some_long_stuff(1)
        self.assertEqual(timer.exec_time, 1000)


if __name__ == '__main__':
    unittest.main()
