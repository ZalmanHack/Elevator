import sys
from PyQt5.QtCore import QObject, pyqtSignal, pyqtSlot
from PyQt5.Qt import QWidget
from interfaces.liftShaftUI import Ui_LiftShaft
from .Templates import TSensors

# import common.resources_rc

class LiftShaft(QWidget, Ui_LiftShaft):
    updated_pos = pyqtSignal(int)
    out_of_rail = pyqtSignal()
    calling_lift = pyqtSignal(bytes)  # сигнал о нажатии кнопки с определенного этажа

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.maximum = 400
        self.minimum = 0

    @pyqtSlot(int)
    def add_len_cable(self, value: int):
        try:
            assert value == 1 or value == -1, 'value have to be 1 or -1'
            value = self.cab_cable.minimumHeight() + value
            if value < self.minimum:
                value = self.minimum
            elif value > self.maximum:
                value = self.maximum
            assert self.maximum >= value >= self.minimum, (
                'OUT OF RAIL!\n    {} >= {} >= {}'.format(self.maximum, value, self.minimum))
            self.cab_cable.setMinimumHeight(value)
            self.cab_cable.setMaximumHeight(value)
            self.counterweight_cable.setMinimumHeight(self.maximum - value)
            self.counterweight_cable.setMaximumHeight(self.maximum - value)
            self.updated_pos.emit(value)
        except Exception as e:
            self.out_of_rail.emit()
            print(e)

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