from status import Status


class IState(object):
    def __init__(self):
        pass

    def start_stop(self, context, time_keeper):
        pass

    def reset(self, context, time_keeper):
        pass


class InitState(IState):
    def __init__(self, gui):
        super().__init__()
        gui.set_start_stop_button_text('Start')

    def start_stop(self, context, time_keeper):
        print('[InitState] On start_stop button click')
        print('[InitState] Change status to RUNNING')
        time_keeper.start()
        context.transition(next_status=Status.RUNNING)

    def reset(self, context, time_keeper):
        print('[InitState] On reset button click')


class RunningState(IState):
    def __init__(self, gui):
        super().__init__()
        gui.set_start_stop_button_text('Stop')

    def start_stop(self, context, time_keeper):
        print('[RunningState] On start_stop button click')
        print('[RunningState] Change status to SUSPENDED')
        time_keeper.stop()
        context.transition(next_status=Status.SUSPENDED)

    def reset(self, context, time_keeper):
        print('[RunningState] On reset button click')


class SuspendedState(IState):
    def __init__(self, gui):
        super().__init__()
        gui.set_start_stop_button_text('Restart')

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
