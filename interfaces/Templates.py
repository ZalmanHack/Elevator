from dataclasses import dataclass


@dataclass(frozen=False)
class Speed:
    LOW = 20 # 60
    FAST = 10 # 20


@dataclass(frozen=True)
class Way:
    UP = -1
    STOP = 0
    DOWN = 1


@dataclass(frozen=True)
class TDoor:
    OPEN: int = -1
    MIDDLE: int = 0
    CLOSE: int = 1


@dataclass(frozen=True)
class TSensors:
    One: bytes = b'\x10'
    Two: bytes = b'\x20'
    Three: bytes = b'\x30'
    Four: bytes = b'\x40'
    Five: bytes = b'\x50'
    LSpeed: bytes = b'\x60'
    Stopper: bytes = b'\x70'
    Weight: bytes = b'\x80'

    def get(self, value: int):
        if value == 1:
            return self.One
        elif value == 2:
            return self.Two
        elif value == 3:
            return self.Three
        elif value == 4:
            return self.Four
        elif value == 5:
            return self.Five

    def get_int(self, value: bytes):
        if value == self.One:
            return 1
        elif value == self.Two:
            return 2
        elif value == self.Three:
            return 3
        elif value == self.Four:
            return 4
        elif value == self.Five:
            return 5


@dataclass(frozen=True)
class TStates:
    pre_init: bytes = b'\xF0'
    init: bytes = b'\xF1'
    normal: bytes = b'\xF2'
    crash: bytes = b'\xF3'
