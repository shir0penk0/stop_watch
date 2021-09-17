import tkinter as tk
from enum import Enum, auto


class Status(Enum):
    INIT = auto()
    RUNNING = auto()
    SUSPENDED = auto()


class Context(object):
    def __init__(self):
        self.st = InitState()

    def on_click_start_stop_button(self, event):
        self.st.start_stop(self)

    def on_click_reset_button(self, event):
        self.st.reset(self)

    def transition(self, next_status):
        if next_status == Status.INIT:
            self.st = InitState()
        elif next_status == Status.RUNNING:
            self.st = RunningState()
        elif next_status == Status.SUSPENDED:
            self.st = SuspendedState()


class IState(object):
    def __init__(self):
        pass

    def start_stop(self, context):
        print('start stop button is clicked')

    def reset(self, context):
        pass


class InitState(IState):
    def __init__(self):
        super().__init__()
        pass

    def start_stop(self, context):
        print('[InitState] On start_stop button click')
        print('[InitState] Change status to RUNNING')
        context.transition(next_status=Status.RUNNING)

    def reset(self, context):
        print('[InitState] On reset button click')


class RunningState(IState):
    def __init__(self):
        super().__init__()
        pass

    def start_stop(self, context):
        print('[RunningState] On start_stop button click')
        print('[RunningState] Change status to SUSPENDED')
        context.transition(next_status=Status.SUSPENDED)

    def reset(self, context):
        print('[RunningState] On reset button click')


class SuspendedState(IState):
    def __init__(self):
        super().__init__()
        pass

    def start_stop(self, context):
        print('[SuspendedState] On start_stop button click')
        print('[SuspendedState] Change status to RUNNING')
        context.transition(next_status=Status.RUNNING)

    def reset(self, context):
        print('[SuspendedState] On reset button click')
        print('[SuspendedState] Change status to INIT')
        context.transition(next_status=Status.INIT)


if __name__ == '__main__':
    window = tk.Tk()
    window.geometry('600x600')
    elapsed_time = tk.Label(text=u'00:00:00')
    elapsed_time.pack()
    start_stop_button = tk.Button(text=u'Start', width=5)
    ctx = Context()
    start_stop_button.bind('<Button-1>', ctx.on_click_start_stop_button)
    start_stop_button.pack()
    reset_button = tk.Button(text=u'Reset', width=5)
    reset_button.bind('<Button-1>', ctx.on_click_reset_button)
    reset_button.pack()

    window.title(u'Stop watch')
    window.mainloop()
