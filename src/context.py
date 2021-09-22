from status import Status
from state_control import InitState, RunningState, SuspendedState
from time_keeper import TimeKeeper


class Context(object):
    def __init__(self, gui):
        self.__st = InitState(gui)
        self.__time_keeper = TimeKeeper()
        self.__gui = gui
        self.__need_display_update = False

    def on_click_start_stop_button(self, event):
        self.__st.start_stop(self, time_keeper=self.__time_keeper)

    def on_click_reset_button(self, event):
        self.__st.reset(self, time_keeper=self.__time_keeper)

    def transition(self, next_status):
        if next_status == Status.INIT:
            self.__st = InitState(self.__gui)
            self.__need_display_update = False
        elif next_status == Status.RUNNING:
            self.__st = RunningState(self.__gui)
            self.__need_display_update = True
        elif next_status == Status.SUSPENDED:
            self.__st = SuspendedState(self.__gui)
            self.__need_display_update = False
        self.__gui.update_time()

    def get_elapsed_time(self):
        return self.__time_keeper.elapsed_time()

    def need_display_update(self):
        return self.__need_display_update
