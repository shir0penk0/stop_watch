import time


class TimeKeeper(object):
    def __init__(self):
        self.__start_time = None
        self.__hold_time = None

    def start(self):
        self.__start_time = time.monotonic()

    def stop(self):
        if self.__start_time is None:
            return
        if self.__hold_time is None:
            self.__hold_time = time.monotonic() - self.__start_time
        else:
            self.__hold_time = self.__hold_time + time.monotonic() - self.__start_time
        self.__start_time = None

    def elapsed_time(self):
        if self.__start_time is None and self.__hold_time is None:
            return 0
        if self.__start_time is None:
            return self.__hold_time
        if self.__hold_time is None:
            return time.monotonic() - self.__start_time
        else:
            return time.monotonic() - self.__start_time + self.__hold_time

    def reset(self):
        self.__start_time = None
        self.__hold_time = None
