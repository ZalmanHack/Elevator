from PyQt5.QtCore import QObject, pyqtSignal, pyqtSlot
from PyQt5.Qt import QWidget, QTimer
from .digitalTableUI import Ui_digital_table
from .Templates import TSensors, Way


class DigitalTable(QWidget, Ui_digital_table):
    calling_lift = pyqtSignal(bytes)  # сигнал о нажатии кнопки из кабины

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.pointer = None
        self.info_table_state = False
        self.timerInfo = QTimer()
        self.timerInfo.timeout.connect(self.timeoutInfo)
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

    @pyqtSlot(bytes, bool)
    def set_state_btn(self, floor: bytes, state: bool = False):
        if state:
            color = [255, 0, 0]
            hover_color = [200, 0, 0]
        else:
            color = [100, 100, 100]
            hover_color = [0, 0, 0]
        styleSheet = "QPushButton {\n" \
                     "    background-color: rgb(" + str(color[0]) + "," + str(color[1]) + "," + str(color[2]) + ");\n" \
                     "    border-style: outset;\n" \
                     "    border-radius: 10px;\n" \
                     "    border-width: 3px;\n" \
                     "    border-color: rgb(223, 186, 17);\n" \
                     "}\n" \
                     "\n" \
                     "QPushButton:hover {\n" \
                     "background-color: " \
                     "rgb(" + str(hover_color[0]) + "," + str(hover_color[1]) + "," + str(hover_color[2]) + ");\n" \
                     " }\n" \
                     "\n" \
                     "QPushButton:pressed {\n" \
                     "     border-width: 4px;\n" \
                     " }"
        if floor == TSensors.One:
            self.floor_btn_1.setStyleSheet(styleSheet)
        elif floor == TSensors.Two:
            self.floor_btn_2.setStyleSheet(styleSheet)
        elif floor == TSensors.Three:
            self.floor_btn_3.setStyleSheet(styleSheet)
        elif floor == TSensors.Four:
            self.floor_btn_4.setStyleSheet(styleSheet)
        elif floor == TSensors.Five:
            self.floor_btn_5.setStyleSheet(styleSheet)

    @pyqtSlot(str)
    def set_table_info(self, text: str):
        self.label_info_table.setText(text)
        if len(text) == 0 and self.timerInfo.isActive():
            self.timerInfo.stop()
            self.label_info_table.setStyleSheet("QLabel {"
                                                "	background-color: rgb(83, 83, 83);"
                                                "	font: 75 15pt 'MS Shell Dlg 2';"
                                                "	color: rgb(150, 150, 150);"
                                                "	border-style: outset;"
                                                "	border-width: 3px;"
                                                "	border-color: black;"
                                                "}")
        elif len(text) != 0:
            if not self.timerInfo.isActive():
                self.timerInfo.start(500)


    @pyqtSlot()
    def timeoutInfo(self):
        if self.info_table_state:
            self.info_table_state = not self.info_table_state
            self.label_info_table.setStyleSheet("QLabel {"
                                                "	background-color: rgb(83, 83, 83);"
                                                "	font: 75 15pt 'MS Shell Dlg 2';"
                                                "	color: rgb(150, 150, 150);"
                                                "	border-style: outset;"
                                                "	border-width: 3px;"
                                                "	border-color: black;"
                                                "}")
        else:
            self.info_table_state = not self.info_table_state
            self.label_info_table.setStyleSheet("QLabel {"
                                                "	background-color: rgb(255, 255, 255);"
                                                "	font: 75 15pt 'MS Shell Dlg 2';"
                                                "	color: rgb(0, 0, 0);"
                                                "	border-style: outset;"
                                                "	border-width: 3px;"
                                                "	border-color: black;"
                                                "}")