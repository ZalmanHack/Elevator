from PyQt5.QtCore import QObject, pyqtSignal, pyqtSlot
from PyQt5.Qt import QTimer
from .Templates import Speed, Way


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
