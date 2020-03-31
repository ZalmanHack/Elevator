from PyQt5.QtCore import QObject, pyqtSignal, pyqtSlot
from PyQt5.Qt import QWidget
from .digitalTableUI import Ui_digital_table
from .engine import Way

class DigitalTable(QWidget, Ui_digital_table):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.pointer = None
        self.array = []
        self.array.append(self.floor_lb_1)
        self.array.append(self.floor_lb_2)
        self.array.append(self.floor_lb_3)
        self.array.append(self.floor_lb_4)
        self.array.append(self.floor_lb_5)

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

    @pyqtSlot(int)
    def set_floor(self, value: int):
        for i in range(len(self.array)):
            if value - 1 == i:
                self.array[i].setStyleSheet("QLabel {"
                                            "	background-color: rgb(255, 255, 255);"
                                            "	font: 75 15pt 'MS Shell Dlg 2';"
                                            "	color: rgb(0, 0, 0);"
                                            "	border-style: outset;"
                                            "	border-width: 3px;"
                                            "	border-color: black;"
                                            "}")
            else:
                self.array[i].setStyleSheet("QLabel {"
                                            "	background-color: rgb(83, 83, 83);"
                                            "	font: 75 15pt 'MS Shell Dlg 2';"
                                            "	color: rgb(150, 150, 150);"
                                            "	border-style: outset;"
                                            "	border-width: 3px;"
                                            "	border-color: black;"
                                            "}")
