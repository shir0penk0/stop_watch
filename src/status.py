from enum import Enum, auto


class Status(Enum):
    INIT = auto()
    RUNNING = auto()
    SUSPENDED = auto()
