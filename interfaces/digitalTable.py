from PyQt5.QtCore import QObject, pyqtSignal, pyqtSlot
from PyQt5.Qt import QWidget
from .digitalTableUI import Ui_digital_table
from .Templates import TSensors, Way


class DigitalTable(QWidget, Ui_digital_table):
    calling_lift = pyqtSignal(bytes)  # сигнал о нажатии кнопки из кабины

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.pointer = None
        self.array = {
            TSensors.One: self.floor_lb_1,
            TSensors.Two: self.floor_lb_2,
            TSensors.Three: self.floor_lb_3,
            TSensors.Four: self.floor_lb_4,
            TSensors.Five: self.floor_lb_5
        }

    def setupUi(self, window):
        super().setupUi(window)

    @pyqtSlot(int)
    def set_pointer(self, value: int):
        if self.pointer != value:
            self.pointer = value
            if value == Way.UP:
                self.up_lb.setStyleSheet("QLabel {\nborder-image: url(:/pointers/up_on.png);\n}")
                self.down_lb.setStyleSheet("QLabel {\nborder-image: url(:/pointers/down_off.png);\n}")
            elif value == Way.DOWN:
                self.up_lb.setStyleSheet("QLabel {\nborder-image: url(:/pointers/up_off.png);\n}")
                self.down_lb.setStyleSheet("QLabel {\nborder-image: url(:/pointers/down_on.png);\n}")
            elif value == Way.STOP:
                self.up_lb.setStyleSheet("QLabel {\nborder-image: url(:/pointers/up_off.png);\n}")
                self.down_lb.setStyleSheet("QLabel {\nborder-image: url(:/pointers/down_off.png);\n}")

    @pyqtSlot()
    def on_floor_btn_1_clicked(self):
        self.calling_lift.emit(TSensors.One)

    @pyqtSlot()
    def on_floor_btn_2_clicked(self):
        self.calling_lift.emit(TSensors.Two)

    @pyqtSlot()
    def on_floor_btn_3_clicked(self):
        self.calling_lift.emit(TSensors.Three)

    @pyqtSlot()
    def on_floor_btn_4_clicked(self):
        self.calling_lift.emit(TSensors.Four)

    @pyqtSlot()
    def on_floor_btn_5_clicked(self):
        self.calling_lift.emit(TSensors.Five)

    @pyqtSlot(bytes)
    def set_floor(self, value: bytes):
        for val in self.array.values():
            val.setStyleSheet("QLabel {"
                              "	background-color: rgb(83, 83, 83);"
                              "	font: 75 15pt 'MS Shell Dlg 2';"
                              "	color: rgb(150, 150, 150);"
                              "	border-style: outset;"
                              "	border-width: 3px;"
                              "	border-color: black;"
                              "}")
        if value in self.array:
            self.array[value].setStyleSheet("QLabel {"
                                            "	background-color: rgb(255, 255, 255);"
                                            "	font: 75 15pt 'MS Shell Dlg 2';"
                                            "	color: rgb(0, 0, 0);"
                                            "	border-style: outset;"
                                            "	border-width: 3px;"
                                            "	border-color: black;"
                                            "}")