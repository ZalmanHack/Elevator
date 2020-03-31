from PyQt5.QtCore import QObject, pyqtSignal, pyqtSlot
from PyQt5.Qt import QTimer


class Speed:
    LOW = 50
    FAST = 20


class Way:
    UP = -1
    STOP = 0
    DOWN = 1


class Engine(QObject):
    added_len_cable = pyqtSignal(int)
    updated_pointer = pyqtSignal(int)

    def __init__(self, parent=None):
        super().__init__(parent)
        self.timer = QTimer()
        self.timer.timeout.connect(self.timeout)
        self.way = None

    @pyqtSlot()
    def timeout(self):
        self.added_len_cable.emit(self.way)

    @pyqtSlot(int, int)
    def run(self, speed: Speed, way: Way):
        self.timer.start(speed)
        self.way = way
        self.updated_pointer.emit(way)

    def stop(self):
        self.timer.stop()
        self.updated_pointer.emit(Way.STOP)
