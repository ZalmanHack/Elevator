from PyQt5.QtCore import QObject, pyqtSignal, pyqtSlot, QThread
from .engine import Speed, Way

class _MainProcess(QObject):
    finished = pyqtSignal()
    check_stoppers = pyqtSignal()
    engine_run = pyqtSignal(int, int)
    engine_stop = pyqtSignal()

    def __init__(self, parent=None):
        super().__init__(parent)
        self.try_count = 10
        # массив проверки состояния датчиков

        # property ---------------------------------
        self.m_stoppers = None
        self.m_floor = None
        self.m_floor_array = [False] * 5
        # ------------------------------------------

    def init(self):
        QThread.sleep(2)
        # проверка стопорных датчиков
        if self._init_stoppers():
            # поднимаем лифт до конца вверх
            self.engine_run.emit(Speed.FAST, Way.UP)
            self._wait_stoppers()
            self.engine_stop.emit()
            # опускам кабину до конца вниз, проверяя все датчики
            self.engine_run.emit(Speed.FAST, Way.DOWN)
            # ждем окончания спуска кабины
            self._wait_stoppers()
            # станавливаем ее
            self.engine_stop.emit()
            # проверяем все датчики
            if False in self.floor_array:
                print('Не найден один из датчиков')
            else:
                print('Все заебись')

    def _wait_stoppers(self):
        self.m_stoppers = None
        while self.m_stoppers is not True:
            QThread.usleep(100)

    def _whit_floor(self):
        pass

    def _init_stoppers(self):
        self.m_stoppers = None
        self.check_stoppers.emit()
        for i in range(self.try_count):
            QThread.usleep(100)
            print(self.m_stoppers)
            if self.m_stoppers is True:
                return True
        return False

    @pyqtSlot()
    def run(self):
        self.init()
        # self.finished.emit()

    @pyqtSlot(int)
    def checked_floor(self, value: int):
        self.floor_array[value - 1] = True
        print(self.floor_array, value)

    # property методы __________________________________________________________________________________________________
    # m_stoppers -------------------------------------------------------------------------------------------------------
    @property
    def stoppers(self):
        return self.m_stoppers

    @stoppers.setter
    def stoppers(self, value: bool):
        self.m_stoppers = value
    # m_floor ----------------------------------------------------------------------------------------------------------
    @property
    def floor(self):
        return self.m_floor

    @floor.setter
    def floor(self, value: int):
        self.m_floor = value
    # m_floor ----------------------------------------------------------------------------------------------------------
    @property
    def floor_array(self):
        return self.m_floor_array

    @floor_array.setter
    def floor_array(self, value: list):
        self.m_floor_array = value

class Computer(QObject):
    check_stoppers = pyqtSignal()
    engine_run = pyqtSignal(int, int)
    engine_stop = pyqtSignal()

    def __init__(self, parent=None):
        super().__init__(parent)
        self.main_thread = QThread(self)
        self._process = _MainProcess()
        self._process.moveToThread(self.main_thread)
        self._init_connects__process()
        self.main_thread.start()

    def _init_connects__process(self):
        self._process.finished.connect(self.main_thread.terminate)
        self.main_thread.started.connect(self._process.run)
        self._process.check_stoppers.connect(self.check_stoppers)
        self._process.engine_run.connect(self.engine_run)
        self._process.engine_stop.connect(self.engine_stop)

    @pyqtSlot(bool)
    def update_stoppers(self, value: bool):
        self._process.stoppers = value

    @pyqtSlot(int)
    def checked_floor(self, value: int):
        temp = self._process.floor_array
        temp[value - 1] = True
        self._process.floor_array = temp
        print(temp)

    @pyqtSlot(int)
    def add_floor(self, value: int):
        print('Добавлен новый этаж {}'.format(value))
