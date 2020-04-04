from PyQt5.QtCore import QObject, pyqtSignal, pyqtSlot, QTimer
from PyQt5.Qt import QWidget
from .sensorsUI import Ui_sensors
from .Templates import TSensors, TStates


class Sensors(QWidget, Ui_sensors):
    checked_floor = pyqtSignal(bytes)
    checked_weight = pyqtSignal(int)
    checked_stoppers = pyqtSignal()
    checked_low_speed = pyqtSignal()
    reset_init = pyqtSignal()

    def __init__(self, parent=None, floor_height=100, max_weight=400):
        super().__init__(parent)
        self.setupUi(self)
        self.floor_height = floor_height
        self.max_weight = max_weight
        self.weight = 0
        self.states = {
            TStates.pre_init: self.light_init,
            TStates.init: self.light_init,
            TStates.normal: self.light_normal,
            TStates.crash: self.light_crash
        }
        self.widgets = {TSensors.One: self.light_fl_1,
                        TSensors.Two: self.light_fl_2,
                        TSensors.Three: self.light_fl_3,
                        TSensors.Four: self.light_fl_4,
                        TSensors.Five: self.light_fl_5,
                        TSensors.LSpeed: self.light_ls,
                        TSensors.Stopper: self.light_stp,
                        TSensors.Weight: self.light_cw}
        self.styleSheet = 'QLabel {border-style: outset;border-radius: 8px;border-width: 2px;' \
                          'border-color: rgb(0, 0, 0);background-color: rgb'
        self.red = '(255, 0, 0);}'
        self.green = '(25, 255, 0);}'
        self.blue = '(0, 155, 255);}'
        self.timerLight = QTimer()
        self.timerWeight = QTimer()
        self.timerLight.timeout.connect(self.timeoutLight)
        self.timerWeight.timeout.connect(self.timeoutWeight)
        self.timerWeight.start(2000)

    # метод окрашивает все зеленые фонарики в синие (по таймеру)
    @pyqtSlot()
    def timeoutLight(self):
        for key, obj in self.widgets.items():
            if obj.styleSheet() == self.styleSheet + self.green:
                obj.setStyleSheet(self.styleSheet + self.blue)
        self.timerLight.stop()

    # метод проверяет вес кабины (по таймеру)
    @pyqtSlot()
    def timeoutWeight(self):
        if self.weight - self.max_weight > 0:
            self.set_light_state(TSensors.Weight, True)
        else:
            self.set_light_state(TSensors.Weight, True)


    # сигнал на этот слот поступает при изменении веса кабинв
    @pyqtSlot(int)
    def check_weight(self, weight: int = 0):
        # сли <= 0 то вес в норме, если > 0 то превышение
        self.checked_weight.emit(weight - self.max_weight)

    # проверка вхождения в зону аерхнего или нижнего стопора (метод для компьютера)
    @pyqtSlot()
    def check_stoppers(self):
        self.checked_stoppers.emit(True)

    # сигнал на этот слот поступает при изменении расстояния от кабины до земли
    @pyqtSlot(int)
    def check_position(self, len_cable: int = 0):
        self._check_stoppers(len_cable)
        self._check_floor(len_cable)
        self._check_low_speed(len_cable)

    # проверка вхождения в зону аерхнего или нижнего стопора
    def _check_stoppers(self, len_cable: int = 0):
        if len_cable >= self.floor_height * 4 or len_cable <= 0:
            self.checked_stoppers.emit()

    # проверка вхождения в зону конкретного этажа
    def _check_floor(self, len_cable: int = 0):
        if len_cable % self.floor_height == 0:
            value = TSensors().get(int(5 - (len_cable / self.floor_height)))
            self.checked_floor.emit(value)

    # проверка вхождения в зону точной остановки
    def _check_low_speed(self, len_cable: int = 0):
        result = len_cable - self.floor_height / 2
        if result % self.floor_height == 0:
            self.checked_low_speed.emit()

    # изменение цвета фонарика
    @pyqtSlot(bytes, bool)
    def set_light_state(self, value: bytes, state: bool):
        self.styleSheet = 'QLabel {border-style: outset;border-radius: 8px;border-width: 2px;' \
                     'border-color: rgb(0, 0, 0);background-color: rgb'
        color = self.green
        if not state:
            color = self.red

        if value in self.widgets:
            self.widgets[value].setStyleSheet(self.styleSheet + color)
            if self.timerLight.isActive():
                self.timerLight.stop()
            self.timerLight.start(1000)

        elif value in self.states:
            for state in self.states.keys():
                self.states[state].setStyleSheet(self.styleSheet + self.red)
            self.states[value].setStyleSheet(self.styleSheet + color)

    @pyqtSlot()
    def on_reset_btn_clicked(self):
        self.reset_init.emit()
