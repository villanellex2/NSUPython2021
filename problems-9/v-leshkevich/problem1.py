from contextlib import contextmanager
from time import time


class Timer:

    def __init__(self):
        self.exec_time = -1

    @contextmanager
    def timer(self):
        start_time = time()
        try:
            yield
        except Exception as e:
            print('Caught exception: ' + str(e))
        finally:
            self.exec_time = int(round(time() - start_time)) * 1000
            print("'with' block execution time: {time} ms".format(time=self.exec_time))
