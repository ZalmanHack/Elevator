from PyQt5.QtCore import QObject, pyqtSignal, pyqtSlot


class Sensors(QObject):
    checked_floor = pyqtSignal(int)
    checked_weight = pyqtSignal(int)
    checked_stoppers = pyqtSignal(bool)
    checked_low_zone = pyqtSignal()

    def __init__(self, parent=None, floor_height=100, max_weight=400):
        super().__init__(parent)
        self.floor_height = floor_height
        self.max_weight = max_weight

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
    def _check_stoppers(self,  len_cable: int = 0):
        self.checked_stoppers.emit(len_cable == self.floor_height * 4 or len_cable == 0)

    # проверка вхождения в зону конкретного этажа
    def _check_floor(self, len_cable: int = 0):
        if len_cable % self.floor_height == 0:
            self.checked_floor.emit(int(5 - (len_cable / self.floor_height)))
            print('_check_floor ' + str(int(5 - (len_cable / self.floor_height))))

    # проверка вхождения в зону точной остановки
    def _check_low_speed(self, len_cable: int = 0):
        if (len_cable - self.floor_height / 2) % self.floor_height == 0:
            self.checked_low_zone.emit()
            print('_check_low_speed')
