from PyQt5.QtCore import QObject, pyqtSignal, pyqtSlot, QThread
from .Templates import TStates, TFloors, TSensors, Speed, Way


class Computer(QObject):
    engine_run = pyqtSignal(int, int)
    engine_stop = pyqtSignal()
    set_light_state = pyqtSignal(bytes, bool)
    set_btn_cab_state = pyqtSignal(bytes, bool)
    set_btn_floor_state = pyqtSignal(bytes, bool)

    def __init__(self, parent=None):
        super().__init__(parent)
        self._init()

    def _init(self):
        # массив из 5 этажей, в котором будем хранить вызовы
        # значения могут ыбыть:
        # Way.UP - вверх
        # Way.DOWN - вниз
        # None - нет вызова
        self.floor_calls = {TSensors.One: None, TSensors.Two: None, TSensors.Three: None,
                            TSensors.Four: None, TSensors.Five: None}
        self.t_stack_init = [TSensors.Five, TSensors.LSpeed, TSensors.Four, TSensors.LSpeed, TSensors.Three,
                             TSensors.LSpeed, TSensors.Two, TSensors.LSpeed, TSensors.One]
        self.stack_init = []
        self.stack_normal = []
        self.stack_error = []
        self.state = TStates.pre_init  # состояние компьютера (инициализация, норм, авария)
        self.state_eng = Way.STOP  # направление движения двигателя (stop, up, down)
        self.end_floor = None  # последний пройденый этаж
        self.count_calls = 0  # кол-во вызванных этажей
        self.next_floor_sensor = None  # ожидаемый сенсор (хранит либо этаж либо датчик медленного движения)


    def init(self):
        self._init()
        self.state = TStates.pre_init
        self.set_light_state.emit(self.state, True)
        self.stack_init.clear()
        self.engine_run.emit(Speed.FAST, Way.UP)
        self.state_eng = Way.UP

    def check_init(self, value: bytes):
        self.stack_init.append(value)
        if value == self.t_stack_init[len(self.stack_init) - 1]:
            if len(self.t_stack_init) == len(self.stack_init):
                self.engine_stop.emit()
                self.state_eng = Way.STOP
                self.state = TStates.normal
                self.set_light_state.emit(self.state, True)
            elif len(self.stack_init) == len(self.t_stack_init) - 1:
                self.engine_run.emit(Speed.LOW, Way.DOWN)
                self.state_eng = Way.DOWN
            else:
                self.engine_run.emit(Speed.FAST, Way.DOWN)
                self.state_eng = Way.DOWN
        else:
            print('АВАРИЯ')
            self.engine_stop.emit()
            self.state_eng = Way.STOP
            self.set_light_state.emit(value, False)

    def check_normal(self):
        #


        for key, val in self.floor_calls.items():
            print('{} : {}'.format(bytes.hex(key), val))
        print(self.count_calls)
        print('check_normal')

    @pyqtSlot(bytes)
    def checked_floor(self, value: bytes):
        self.end_floor = value
        if self.state == TStates.init:
            if value is not None:
                self.check_init(value)
                self.set_light_state.emit(value, True)
                # отключаем кнопку, если вдруг она была включена
                self.set_btn_cab_state.emit(value, False)
                self.set_btn_floor_state.emit(value, False)

    @pyqtSlot()
    def checked_low_speed(self):
        if self.state == TStates.init:
            self.check_init(TSensors.LSpeed)
            self.set_light_state.emit(TSensors.LSpeed, True)
        elif self.state == TStates.normal:
            self.check_normal(TSensors.LSpeed)
            self.set_light_state.emit(TSensors.LSpeed, True)

    @pyqtSlot()
    def checked_stoppers(self):
        self.engine_stop.emit()
        self.state_eng = Way.STOP
        self.set_light_state.emit(TSensors.Stopper, True)
        if self.state == TStates.pre_init:
            self.state = TStates.init
            self.set_light_state.emit(self.state, True)
            self.set_light_state.emit(TSensors.Stopper, True)
            self.engine_stop.emit()
            self.state_eng = Way.STOP
        elif self.state == TStates.init:
            pass


    @pyqtSlot(bytes)
    def calling_on_floor(self, value: bytes):
        if self.state == TStates.normal:
            assert value in self.floor_calls
            # если данный этаж еще небыл вызван то увеличиваем кол-во вызванных этажкй
            if self.floor_calls[value] is None:
                self.count_calls += 1
            # добавляем значение вызова
            self.floor_calls[value] = Way.DOWN
            # вызываем проверку нормальной работы лифта (обработка всех вызовов)
            self.check_normal()
            # отправляем сигнал о нажатой кнопке
            self.set_btn_floor_state.emit(value, True)

    @pyqtSlot(bytes)
    def calling_on_cab(self, value: bytes):
        if self.state == TStates.normal:
            assert value in self.floor_calls
            # если данный этаж еще небыл вызван то увеличиваем кол-во вызванных этажкй
            if self.floor_calls[value] is None:
                self.count_calls += 1
            # для добавления параметра в массив вызовов, проверяем положение кабины
            if value < self.end_floor:
                self.floor_calls[value] = Way.DOWN
            elif value > self.end_floor:
                self.floor_calls[value] = Way.UP
            self.check_normal()
            # отправляем сигнал о нажатой кнопке
            self.set_btn_cab_state.emit(value, True)

    @pyqtSlot()
    def restart(self):
        self.init()
