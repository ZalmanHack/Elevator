import sys
from PyQt5.QtCore import QObject, pyqtSignal, pyqtSlot
from PyQt5.Qt import QMainWindow, QHBoxLayout, QVBoxLayout, QGridLayout, QPushButton, QSlider, Qt
from .engine import Engine
from .liftShaft import LiftShaft
from .sensors import Sensors
from .computer import Computer
from .digitalTable import DigitalTable
from interfaces.mainWindowUI import Ui_MainWindow


# import common.resources_rc

class MainWindow(QMainWindow, Ui_MainWindow):
    sig = pyqtSignal(int, bool)

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

    def setupUi(self, window):
        super().setupUi(window)

        self.engine = Engine(window)
        self.liftShaft = LiftShaft(window)
        self.sensors = Sensors(window)
        self.computer = Computer(window)
        self.digitTable = DigitalTable(window)

        self._init_connects_sensors()
        self._init_connects_liftShaft()
        self._init_connects_engine()
        self._init_connects_computer()
        self._init_connects_digitTable()

        #self.computer.init()



        # ПРОБНИКИ ----------------------------------------------------------

        self.gLayout = QGridLayout(self.main_widget)
        self.gLayout.setContentsMargins(8, 8, 8, 8)
        self.gLayout.setHorizontalSpacing(8)
        self.gLayout.setVerticalSpacing(8)
        self.gLayout.addWidget(self.liftShaft, 0, 0, 4, 1)
        self.gLayout.addWidget(self.sensors, 0, 1, 1, 3)
        self.gLayout.addWidget(self.digitTable, 1, 1, 1, 3)
        self.gLayout.addWidget(QPushButton("4"), 2, 1, 1, 1)
        self.gLayout.addWidget(QPushButton("5"), 2, 2, 1, 1)
        self.gLayout.addWidget(QPushButton("6"), 2, 3, 1, 1)
        self.gLayout.addWidget(QPushButton("7"), 3, 1, 1, 3)

    def _init_connects_sensors(self):
        self.sensors.checked_floor.connect(self.computer.checked_floor)
        self.sensors.checked_low_speed.connect(self.computer.checked_low_speed)
        # self.sensors.checked_weight
        self.sensors.checked_stoppers.connect(self.computer.checked_stoppers)
        self.sensors.checked_floor.connect(self.digitTable.set_floor)
        pass

    def _init_connects_liftShaft(self):
        self.liftShaft.updated_pos.connect(self.sensors.check_position)
        self.liftShaft.calling_lift.connect(self.computer.calling_floor)

    def _init_connects_engine(self):
        self.engine.added_len_cable.connect(self.liftShaft.add_len_cable)
        self.engine.updated_pointer.connect(self.digitTable.set_pointer)

    def _init_connects_computer(self):
        self.computer.engine_run.connect(self.engine.run)
        self.computer.engine_stop.connect(self.engine.stop)
        self.computer.set_light_state.connect(self.sensors.set_light_state)

    def _init_connects_digitTable(self):
        pass
