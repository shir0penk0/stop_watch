from status import Status
from state_control import InitState, RunningState, SuspendedState
from time_keeper import TimeKeeper


class Context(object):
    def __init__(self, gui):
        self.st = InitState(gui)
        self.time_keeper = TimeKeeper()
        self.gui = gui

    def on_click_start_stop_button(self, event):
        self.st.start_stop(self, time_keeper=self.time_keeper)

    def on_click_reset_button(self, event):
        self.st.reset(self, time_keeper=self.time_keeper)

    def transition(self, next_status):
        if next_status == Status.INIT:
            self.st = InitState(self.gui)
        elif next_status == Status.RUNNING:
            self.st = RunningState(self.gui)
        elif next_status == Status.SUSPENDED:
            self.st = SuspendedState(self.gui)

    def get_elapsed_time(self):
        return self.time_keeper.elapsed_time()
