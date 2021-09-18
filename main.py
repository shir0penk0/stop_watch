import tkinter as tk
import time
from enum import Enum, auto


class Status(Enum):
    INIT = auto()
    RUNNING = auto()
    SUSPENDED = auto()


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


class Context(object):
    def __init__(self):
        self.st = InitState()
        self.time_keeper = TimeKeeper()

    def on_click_start_stop_button(self, event):
        self.st.start_stop(self, time_keeper=self.time_keeper)

    def on_click_reset_button(self, event):
        self.st.reset(self, time_keeper=self.time_keeper)

    def transition(self, next_status):
        if next_status == Status.INIT:
            self.st = InitState()
        elif next_status == Status.RUNNING:
            self.st = RunningState()
        elif next_status == Status.SUSPENDED:
            self.st = SuspendedState()

    def get_elapsed_time(self):
        return self.time_keeper.elapsed_time()


class IState(object):
    def __init__(self):
        pass

    def start_stop(self, context, time_keeper):
        pass

    def reset(self, context, time_keeper):
        pass


class InitState(IState):
    def __init__(self):
        super().__init__()
        start_stop_button_text.set('Start')

    def start_stop(self, context, time_keeper):
        print('[InitState] On start_stop button click')
        print('[InitState] Change status to RUNNING')
        time_keeper.start()
        context.transition(next_status=Status.RUNNING)

    def reset(self, context, time_keeper):
        print('[InitState] On reset button click')


class RunningState(IState):
    def __init__(self):
        super().__init__()
        start_stop_button_text.set('Stop')

    def start_stop(self, context, time_keeper):
        print('[RunningState] On start_stop button click')
        print('[RunningState] Change status to SUSPENDED')
        time_keeper.stop()
        context.transition(next_status=Status.SUSPENDED)

    def reset(self, context, time_keeper):
        print('[RunningState] On reset button click')


class SuspendedState(IState):
    def __init__(self):
        super().__init__()
        start_stop_button_text.set('Restart')

    def start_stop(self, context, time_keeper):
        print('[SuspendedState] On start_stop button click')
        print('[SuspendedState] Change status to RUNNING')
        time_keeper.start()
        context.transition(next_status=Status.RUNNING)

    def reset(self, context, time_keeper):
        print('[SuspendedState] On reset button click')
        print('[SuspendedState] Change status to INIT')
        time_keeper.reset()
        context.transition(next_status=Status.INIT)


def update_time():
    t = ctx.get_elapsed_time()
    h = int(t / 3600)
    m = int((t / 60) % 60)
    s = int(t % 60)
    ms = int((t - int(t)) * 100)
    # print('{:02d}:{:02d}:{:02d}'.format(h, m, s))
    time_text.set('{:02d}:{:02d}:{:02d}.{:02d}'.format(h, m, s, ms))
    window.after(DISPLAY_INTERVAL, update_time)


if __name__ == '__main__':

    window = tk.Tk()
    window.title(u'Stop watch')
    window.geometry('500x200')
    window.resizable(width=False, height=False)

    frame_top = tk.Frame(window, borderwidth=10, relief='sunken')
    frame_top.pack(expand=True, fill=tk.BOTH)
    time_text = tk.StringVar()
    time_text.set('00:00:00')
    elapsed_time = tk.Label(frame_top, textvariable=time_text, font=("Osaka-Mono", "80", "bold"))
    elapsed_time.pack(expand=True, fill=tk.X)

    frame_bottom = tk.Frame(window, borderwidth=10, relief='sunken')
    frame_bottom.pack(expand=True, fill=tk.BOTH)
    start_stop_button_text = tk.StringVar()
    start_stop_button_text.set('Start')
    start_stop_button = tk.Button(frame_bottom, textvariable=start_stop_button_text, width=5, font=("", "40", "bold"))
    ctx = Context()
    start_stop_button.bind('<Button-1>', ctx.on_click_start_stop_button)
    start_stop_button.pack(side=tk.LEFT, expand=True, fill=tk.BOTH)
    reset_button = tk.Button(frame_bottom, text=u'Reset', width=5, font=("", "40", "bold"))
    reset_button.bind('<Button-1>', ctx.on_click_reset_button)
    reset_button.pack(side=tk.RIGHT, expand=True, fill=tk.BOTH)

    # Unit of interval is ms
    DISPLAY_INTERVAL = 10
    window.after(DISPLAY_INTERVAL, update_time)
    window.mainloop()
