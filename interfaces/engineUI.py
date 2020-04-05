# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'engine.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_engine(object):
    def setupUi(self, engine):
        engine.setObjectName("engine")
        engine.resize(360, 95)
        engine.setMinimumSize(QtCore.QSize(360, 95))
        engine.setMaximumSize(QtCore.QSize(360, 95))
        self.verticalLayout = QtWidgets.QVBoxLayout(engine)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.central = QtWidgets.QWidget(engine)
        self.central.setMinimumSize(QtCore.QSize(360, 95))
        self.central.setMaximumSize(QtCore.QSize(360, 95))
        self.central.setStyleSheet("QWidget#central {\n"
"    background-color: qlineargradient(spread:pad, x1:0.216, y1:1, x2:1, y2:0, stop:0 rgba(211, 183, 49, 255), stop:0.494318 rgba(234, 210, 98, 255), stop:0.568182 rgba(242, 239, 224, 255), stop:0.784091 rgba(242, 203, 19, 255), stop:1 rgba(242, 218, 100, 255));\n"
"\n"
"    border-style: outset;\n"
"    border-radius: 10px;\n"
"    border-width: 3px;\n"
"    border-color: rgb(223, 186, 17);\n"
"}")
        self.central.setObjectName("central")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.central)
        self.verticalLayout_2.setContentsMargins(10, 10, 10, 10)
        self.verticalLayout_2.setSpacing(8)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.widget = QtWidgets.QWidget(self.central)
        self.widget.setStyleSheet("QWidget#widget {\n"
"    border-radius: 10px;\n"
"    background-color: rgb(112, 112, 112);\n"
"}")
        self.widget.setObjectName("widget")
        self.gridLayout = QtWidgets.QGridLayout(self.widget)
        self.gridLayout.setContentsMargins(8, 8, 8, 8)
        self.gridLayout.setHorizontalSpacing(10)
        self.gridLayout.setObjectName("gridLayout")
        self.label_15 = QtWidgets.QLabel(self.widget)
        self.label_15.setMinimumSize(QtCore.QSize(134, 0))
        self.label_15.setMaximumSize(QtCore.QSize(134, 16777215))
        self.label_15.setStyleSheet("    font: 75 14pt \"MS Shell Dlg 2\";\n"
"    color: rgb(240, 240, 240);")
        self.label_15.setObjectName("label_15")
        self.gridLayout.addWidget(self.label_15, 0, 0, 1, 1)
        self.down_btn_1 = QtWidgets.QPushButton(self.widget)
        self.down_btn_1.setMinimumSize(QtCore.QSize(23, 23))
        self.down_btn_1.setMaximumSize(QtCore.QSize(23, 23))
        self.down_btn_1.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.down_btn_1.setStyleSheet("QPushButton {\n"
"    border-radius: 8px;\n"
"    background-color: rgb(0, 0, 0);\n"
"    font: 75 12pt \"MS Shell Dlg 2\";\n"
"    color: rgb(255, 0, 0)\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(50, 50, 50);\n"
"}")
        self.down_btn_1.setObjectName("down_btn_1")
        self.gridLayout.addWidget(self.down_btn_1, 0, 1, 1, 1)
        self.lbl_speed_1 = QtWidgets.QLabel(self.widget)
        self.lbl_speed_1.setMinimumSize(QtCore.QSize(90, 0))
        self.lbl_speed_1.setMaximumSize(QtCore.QSize(90, 16777215))
        self.lbl_speed_1.setStyleSheet("QLabel {\n"
"    border-radius: 8px;\n"
"    background-color: rgb(0, 0, 0);\n"
"    font: 75 12pt \"MS Shell Dlg 2\";\n"
"    color: rgb(255, 0, 0)\n"
"}")
        self.lbl_speed_1.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_speed_1.setObjectName("lbl_speed_1")
        self.gridLayout.addWidget(self.lbl_speed_1, 0, 2, 1, 1)
        self.up_btn_1 = QtWidgets.QPushButton(self.widget)
        self.up_btn_1.setMinimumSize(QtCore.QSize(23, 23))
        self.up_btn_1.setMaximumSize(QtCore.QSize(23, 23))
        self.up_btn_1.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.up_btn_1.setStyleSheet("QPushButton {\n"
"    border-radius: 8px;\n"
"    background-color: rgb(0, 0, 0);\n"
"    font: 75 12pt \"MS Shell Dlg 2\";\n"
"    color: rgb(255, 0, 0)\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(50, 50, 50);\n"
"}")
        self.up_btn_1.setObjectName("up_btn_1")
        self.gridLayout.addWidget(self.up_btn_1, 0, 3, 1, 1)
        self.label_16 = QtWidgets.QLabel(self.widget)
        self.label_16.setMinimumSize(QtCore.QSize(134, 0))
        self.label_16.setMaximumSize(QtCore.QSize(134, 16777215))
        self.label_16.setStyleSheet("    font: 75 14pt \"MS Shell Dlg 2\";\n"
"    color: rgb(240, 240, 240);")
        self.label_16.setObjectName("label_16")
        self.gridLayout.addWidget(self.label_16, 1, 0, 1, 1)
        self.down_btn_2 = QtWidgets.QPushButton(self.widget)
        self.down_btn_2.setMinimumSize(QtCore.QSize(23, 23))
        self.down_btn_2.setMaximumSize(QtCore.QSize(23, 23))
        self.down_btn_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.down_btn_2.setStyleSheet("QPushButton {\n"
"    border-radius: 8px;\n"
"    background-color: rgb(0, 0, 0);\n"
"    font: 75 12pt \"MS Shell Dlg 2\";\n"
"    color: rgb(255, 0, 0)\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(50, 50, 50);\n"
"}")
        self.down_btn_2.setObjectName("down_btn_2")
        self.gridLayout.addWidget(self.down_btn_2, 1, 1, 1, 1)
        self.lbl_speed_2 = QtWidgets.QLabel(self.widget)
        self.lbl_speed_2.setMinimumSize(QtCore.QSize(90, 0))
        self.lbl_speed_2.setMaximumSize(QtCore.QSize(90, 16777215))
        self.lbl_speed_2.setStyleSheet("QLabel {\n"
"    border-radius: 8px;\n"
"    background-color: rgb(0, 0, 0);\n"
"    font: 75 12pt \"MS Shell Dlg 2\";\n"
"    color: rgb(255, 0, 0)\n"
"}")
        self.lbl_speed_2.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_speed_2.setObjectName("lbl_speed_2")
        self.gridLayout.addWidget(self.lbl_speed_2, 1, 2, 1, 1)
        self.up_btn_2 = QtWidgets.QPushButton(self.widget)
        self.up_btn_2.setMinimumSize(QtCore.QSize(23, 23))
        self.up_btn_2.setMaximumSize(QtCore.QSize(23, 23))
        self.up_btn_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.up_btn_2.setStyleSheet("QPushButton {\n"
"    border-radius: 8px;\n"
"    background-color: rgb(0, 0, 0);\n"
"    font: 75 12pt \"MS Shell Dlg 2\";\n"
"    color: rgb(255, 0, 0)\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(50, 50, 50);\n"
"}")
        self.up_btn_2.setObjectName("up_btn_2")
        self.gridLayout.addWidget(self.up_btn_2, 1, 3, 1, 1)
        self.verticalLayout_2.addWidget(self.widget)
        self.verticalLayout.addWidget(self.central)

        self.retranslateUi(engine)
        QtCore.QMetaObject.connectSlotsByName(engine)

    def retranslateUi(self, engine):
        _translate = QtCore.QCoreApplication.translate
        engine.setWindowTitle(_translate("engine", "Form"))
        self.label_15.setText(_translate("engine", "скорость 1 (%)"))
        self.down_btn_1.setText(_translate("engine", "-"))
        self.lbl_speed_1.setText(_translate("engine", "80"))
        self.up_btn_1.setText(_translate("engine", "+"))
        self.label_16.setText(_translate("engine", "скорость 2 (%)"))
        self.down_btn_2.setText(_translate("engine", "-"))
        self.lbl_speed_2.setText(_translate("engine", "40"))
        self.up_btn_2.setText(_translate("engine", "+"))
