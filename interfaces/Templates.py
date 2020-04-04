from dataclasses import dataclass


@dataclass(frozen=True)
class Speed:
    LOW = 60
    FAST = 20


@dataclass(frozen=True)
class Way:
    UP = -1
    STOP = 0
    DOWN = 1


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


@dataclass(frozen=True)
class TFloors:
    One: bytes = b'\x01'
    Two: bytes = b'\x02'
    Three: bytes = b'\x03'
    Four: bytes = b'\x04'
    Five: bytes = b'\x05'

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


@dataclass(frozen=True)
class TStates:
    pre_init: bytes = b'\xF0'
    init: bytes = b'\xF1'
    normal: bytes = b'\xF2'
    crash: bytes = b'\xF3'
