import time

class TimeKeeper(object):
    def __init__(self):
        self.start_time = None
        self.hold_time = None

    def start(self):
        # self.start_time = time.perf_counter()
        self.start_time = time.monotonic()

    def stop(self):
        if self.start_time is None:
            return
        if self.hold_time is None:
            # self.hold_time = time.perf_counter() - self.start_time
            self.hold_time = time.monotonic() - self.start_time
        else:
            # self.hold_time = self.hold_time + time.perf_counter() - self.start_time
            self.hold_time = self.hold_time + time.monotonic() - self.start_time
        self.start_time = None

    def elapsed_time(self):
        if self.start_time is None and self.hold_time is None:
            return 0
        if self.start_time is None:
            return self.hold_time
        if self.hold_time is None:
            # return time.perf_counter() - self.start_time
            return time.monotonic() - self.start_time
        else:
            return time.monotonic() - self.start_time + self.hold_time
            # return time.perf_counter() - self.start_time + self.hold_time

    def reset(self):
        self.start_time = None
        self.hold_time = None
