from time import time


class Timer:
    def __init__(self):
        self.exec_time = -1

    def __enter__(self):
        self.__time = time()

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.exec_time = int(round(time() - self.__time)) * 1000
        print("'with' block execution time: {time} ms".format(time=self.exec_time))
