from PyQt5.QtCore import QObject, pyqtSignal, pyqtSlot, QThread
from .Templates import TStates, TFloors, TSensors
from .engine import Speed, Way


class Computer(QObject):
    engine_run = pyqtSignal(int, int)
    engine_stop = pyqtSignal()
    set_light_state = pyqtSignal(bytes, bool)

    def __init__(self, parent=None):
        super().__init__(parent)
        self.stack_init = []
        self.t_stack_init = [TSensors.Five, TSensors.LSpeed, TSensors.Four, TSensors.LSpeed, TSensors.Three,
                           TSensors.LSpeed, TSensors.Two, TSensors.LSpeed, TSensors.One]
        self.stack_normal = []
        self.stack_error = []
        self.state = None

    def init(self):
        self.state = TStates.pre_init
        self.stack_init.clear()
        self.engine_run.emit(Speed.FAST, Way.UP)

    def check_init(self, value: bytes):
        self.stack_init.append(value)
        if value == self.t_stack_init[len(self.stack_init) - 1]:
            if len(self.t_stack_init) == len(self.stack_init):
                self.engine_stop.emit()
                self.state = TStates.normal
            elif len(self.stack_init) == len(self.t_stack_init) - 1:
                self.engine_run.emit(Speed.LOW, Way.DOWN)
            else:
                self.engine_run.emit(Speed.FAST, Way.DOWN)
            # self.set_light_state.emit(value, True)
        else:
            print('АВАРИЯ')
            self.engine_stop.emit()
            self.set_light_state.emit(value, False)


    @pyqtSlot(int)
    def checked_floor(self, value: int):
        result = TSensors().get(value)
        if self.state == TStates.init:
            if result is not None:
                self.check_init(result)
                self.set_light_state.emit(result, True)

    @pyqtSlot()
    def checked_low_speed(self):
        if self.state == TStates.init:
            self.check_init(TSensors.LSpeed)
            self.set_light_state.emit(TSensors.LSpeed, True)

    @pyqtSlot()
    def checked_stoppers(self):
        if self.state == TStates.pre_init:
                self.state = TStates.init
                self.engine_stop.emit()
        self.set_light_state.emit(TSensors.Stopper, True)

    @pyqtSlot(int)
    def calling_floor(self, value: int):
        self.init()