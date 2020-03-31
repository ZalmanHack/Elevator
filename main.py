import sys
from PyQt5.Qt import QApplication
from interfaces.mainWindow import MainWindow


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    app.exit(app.exec())