from PyQt5.QtCore import pyqtSignal, pyqtSlot
from PyQt5.Qt import QTimer, QWidget
from .Templates import Speed, Way
from .engineUI import Ui_engine

class Engine(QWidget, Ui_engine):
    added_len_cable = pyqtSignal(int)
    updated_pointer = pyqtSignal(int)

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
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

    @pyqtSlot()
    def on_down_btn_1_clicked(self):
        value = int(self.lbl_speed_1.text())
        if value >= 1:
            value -= 1
        self.lbl_speed_1.setText(str(value))
        Speed.FAST = 100 - value

    @pyqtSlot()
    def on_down_btn_2_clicked(self):
        value = int(self.lbl_speed_2.text())
        if value >= 1:
            value -= 1
        self.lbl_speed_2.setText(str(value))
        Speed.LOW = 100 - value

    @pyqtSlot()
    def on_up_btn_1_clicked(self):
        value = int(self.lbl_speed_1.text())
        if value <= 99:
            value += 1
        self.lbl_speed_1.setText(str(value))
        Speed.FAST = 100 - value

    @pyqtSlot()
    def on_up_btn_2_clicked(self):
        value = int(self.lbl_speed_2.text())
        if value <= 99:
            value += 1
        self.lbl_speed_2.setText(str(value))
        Speed.LOW = 100 - value