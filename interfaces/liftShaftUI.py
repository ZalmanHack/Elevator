# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'liftShaft.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_LiftShaft(object):
    def setupUi(self, LiftShaft):
        LiftShaft.setObjectName("LiftShaft")
        LiftShaft.resize(144, 590)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(LiftShaft.sizePolicy().hasHeightForWidth())
        LiftShaft.setSizePolicy(sizePolicy)
        LiftShaft.setMinimumSize(QtCore.QSize(144, 590))
        LiftShaft.setMaximumSize(QtCore.QSize(144, 590))
        LiftShaft.setStyleSheet("")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(LiftShaft)
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.central = QtWidgets.QWidget(LiftShaft)
        self.central.setStyleSheet("QWidget#central {\n"
"    background-color: qlineargradient(spread:pad, x1:0.216, y1:1, x2:1, y2:0, stop:0 rgba(211, 183, 49, 255), stop:0.494318 rgba(234, 210, 98, 255), stop:0.568182 rgba(242, 239, 224, 255), stop:0.784091 rgba(242, 203, 19, 255), stop:1 rgba(242, 218, 100, 255));\n"
"\n"
"    border-style: outset;\n"
"    border-radius: 10px;\n"
"    border-width: 3px;\n"
"    border-color: rgb(223, 186, 17);\n"
"}")
        self.central.setObjectName("central")
        self.gridLayout = QtWidgets.QGridLayout(self.central)
        self.gridLayout.setContentsMargins(8, 8, 8, 8)
        self.gridLayout.setHorizontalSpacing(8)
        self.gridLayout.setVerticalSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.floor_btn_1 = QtWidgets.QPushButton(self.central)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.floor_btn_1.sizePolicy().hasHeightForWidth())
        self.floor_btn_1.setSizePolicy(sizePolicy)
        self.floor_btn_1.setMinimumSize(QtCore.QSize(20, 20))
        self.floor_btn_1.setMaximumSize(QtCore.QSize(20, 20))
        self.floor_btn_1.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.floor_btn_1.setStyleSheet("QPushButton {\n"
"    background-color: rgb(255, 0, 0);\n"
"    border-style: outset;\n"
"    border-radius: 10px;\n"
"    border-width: 3px;\n"
"    border-color: rgb(223, 186, 17);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(200, 0, 0);\n"
" }\n"
"\n"
"QPushButton:pressed {\n"
"     border-width: 4px;\n"
" }")
        self.floor_btn_1.setText("")
        self.floor_btn_1.setObjectName("floor_btn_1")
        self.gridLayout.addWidget(self.floor_btn_1, 12, 1, 1, 1)
        self.floor_btn_3 = QtWidgets.QPushButton(self.central)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.floor_btn_3.sizePolicy().hasHeightForWidth())
        self.floor_btn_3.setSizePolicy(sizePolicy)
        self.floor_btn_3.setMinimumSize(QtCore.QSize(20, 20))
        self.floor_btn_3.setMaximumSize(QtCore.QSize(20, 20))
        self.floor_btn_3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.floor_btn_3.setStyleSheet("QPushButton {\n"
"    background-color: rgb(255, 0, 0);\n"
"    border-style: outset;\n"
"    border-radius: 10px;\n"
"    border-width: 3px;\n"
"    border-color: rgb(223, 186, 17);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(200, 0, 0);\n"
" }\n"
"\n"
"QPushButton:pressed {\n"
"     border-width: 4px;\n"
" }")
        self.floor_btn_3.setText("")
        self.floor_btn_3.setObjectName("floor_btn_3")
        self.gridLayout.addWidget(self.floor_btn_3, 6, 1, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 36, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout.addItem(spacerItem, 13, 1, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 80, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout.addItem(spacerItem1, 7, 1, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(20, 77, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout.addItem(spacerItem2, 10, 1, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(20, 80, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout.addItem(spacerItem3, 5, 1, 1, 1)
        self.shaft = QtWidgets.QWidget(self.central)
        self.shaft.setMinimumSize(QtCore.QSize(100, 500))
        self.shaft.setMaximumSize(QtCore.QSize(100, 500))
        self.shaft.setStyleSheet("QWidget#shaft {\n"
"background-color: rgb(255, 255, 255);\n"
"    background-image: url(:/shaft/floor.png);\n"
"}")
        self.shaft.setObjectName("shaft")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.shaft)
        self.horizontalLayout.setContentsMargins(8, 0, 8, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setContentsMargins(-1, -1, -1, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.counterweight_cable = QtWidgets.QWidget(self.shaft)
        self.counterweight_cable.setMinimumSize(QtCore.QSize(20, 200))
        self.counterweight_cable.setMaximumSize(QtCore.QSize(20, 200))
        self.counterweight_cable.setStyleSheet("border-image: url(:/shaft/counterweight_cable.png);")
        self.counterweight_cable.setObjectName("counterweight_cable")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.counterweight_cable)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.verticalLayout.addWidget(self.counterweight_cable)
        self.counterweight = QtWidgets.QWidget(self.shaft)
        self.counterweight.setMinimumSize(QtCore.QSize(20, 100))
        self.counterweight.setMaximumSize(QtCore.QSize(20, 100))
        self.counterweight.setStyleSheet("border-image: url(:/shaft/counterweight.png);")
        self.counterweight.setObjectName("counterweight")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.counterweight)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.verticalLayout.addWidget(self.counterweight)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem4)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.cabLayout = QtWidgets.QVBoxLayout()
        self.cabLayout.setContentsMargins(-1, -1, -1, 0)
        self.cabLayout.setSpacing(0)
        self.cabLayout.setObjectName("cabLayout")
        self.cab_cable = QtWidgets.QWidget(self.shaft)
        self.cab_cable.setMinimumSize(QtCore.QSize(59, 200))
        self.cab_cable.setMaximumSize(QtCore.QSize(59, 200))
        self.cab_cable.setStyleSheet("border-image: url(:/shaft/cab_cable.png);")
        self.cab_cable.setObjectName("cab_cable")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.cab_cable)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.cabLayout.addWidget(self.cab_cable)
        self.cab = QtWidgets.QWidget(self.shaft)
        self.cab.setMinimumSize(QtCore.QSize(59, 100))
        self.cab.setMaximumSize(QtCore.QSize(59, 100))
        self.cab.setStyleSheet("border-image: url(:/shaft/cab.png);")
        self.cab.setObjectName("cab")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.cab)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.cabLayout.addWidget(self.cab)
        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.cabLayout.addItem(spacerItem5)
        self.horizontalLayout.addLayout(self.cabLayout)
        self.gridLayout.addWidget(self.shaft, 1, 0, 13, 1)
        self.bottom_widget = QtWidgets.QWidget(self.central)
        self.bottom_widget.setMinimumSize(QtCore.QSize(100, 30))
        self.bottom_widget.setMaximumSize(QtCore.QSize(100, 30))
        self.bottom_widget.setStyleSheet("border-image: url(:/shaft/shaft_bottom.png);")
        self.bottom_widget.setObjectName("bottom_widget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.bottom_widget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.gridLayout.addWidget(self.bottom_widget, 14, 0, 1, 1)
        self.floor_btn_5 = QtWidgets.QPushButton(self.central)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.floor_btn_5.sizePolicy().hasHeightForWidth())
        self.floor_btn_5.setSizePolicy(sizePolicy)
        self.floor_btn_5.setMinimumSize(QtCore.QSize(20, 20))
        self.floor_btn_5.setMaximumSize(QtCore.QSize(20, 20))
        self.floor_btn_5.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.floor_btn_5.setStyleSheet("QPushButton {\n"
"    background-color: rgb(255, 0, 0);\n"
"    border-style: outset;\n"
"    border-radius: 10px;\n"
"    border-width: 3px;\n"
"    border-color: rgb(223, 186, 17);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(200, 0, 0);\n"
" }\n"
"\n"
"QPushButton:pressed {\n"
"     border-width: 4px;\n"
" }")
        self.floor_btn_5.setText("")
        self.floor_btn_5.setObjectName("floor_btn_5")
        self.gridLayout.addWidget(self.floor_btn_5, 2, 1, 1, 1)
        self.label = QtWidgets.QLabel(self.central)
        self.label.setMinimumSize(QtCore.QSize(0, 44))
        self.label.setMaximumSize(QtCore.QSize(16777215, 44))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        spacerItem6 = QtWidgets.QSpacerItem(20, 80, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout.addItem(spacerItem6, 3, 1, 1, 1)
        spacerItem7 = QtWidgets.QSpacerItem(20, 44, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout.addItem(spacerItem7, 1, 1, 1, 1)
        self.floor_btn_2 = QtWidgets.QPushButton(self.central)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.floor_btn_2.sizePolicy().hasHeightForWidth())
        self.floor_btn_2.setSizePolicy(sizePolicy)
        self.floor_btn_2.setMinimumSize(QtCore.QSize(20, 20))
        self.floor_btn_2.setMaximumSize(QtCore.QSize(20, 20))
        self.floor_btn_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.floor_btn_2.setStyleSheet("QPushButton {\n"
"    background-color: rgb(255, 0, 0);\n"
"    border-style: outset;\n"
"    border-radius: 10px;\n"
"    border-width: 3px;\n"
"    border-color: rgb(223, 186, 17);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(200, 0, 0);\n"
" }\n"
"\n"
"QPushButton:pressed {\n"
"     border-width: 4px;\n"
" }")
        self.floor_btn_2.setText("")
        self.floor_btn_2.setObjectName("floor_btn_2")
        self.gridLayout.addWidget(self.floor_btn_2, 9, 1, 1, 1)
        self.floor_btn_4 = QtWidgets.QPushButton(self.central)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.floor_btn_4.sizePolicy().hasHeightForWidth())
        self.floor_btn_4.setSizePolicy(sizePolicy)
        self.floor_btn_4.setMinimumSize(QtCore.QSize(20, 20))
        self.floor_btn_4.setMaximumSize(QtCore.QSize(20, 20))
        self.floor_btn_4.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.floor_btn_4.setStyleSheet("QPushButton {\n"
"    background-color: rgb(255, 0, 0);\n"
"    border-style: outset;\n"
"    border-radius: 10px;\n"
"    border-width: 3px;\n"
"    border-color: rgb(223, 186, 17);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(200, 0, 0);\n"
" }\n"
"\n"
"QPushButton:pressed {\n"
"     border-width: 4px;\n"
" }")
        self.floor_btn_4.setText("")
        self.floor_btn_4.setObjectName("floor_btn_4")
        self.gridLayout.addWidget(self.floor_btn_4, 4, 1, 1, 1)
        self.verticalLayout_7.addWidget(self.central)

        self.retranslateUi(LiftShaft)
        QtCore.QMetaObject.connectSlotsByName(LiftShaft)

    def retranslateUi(self, LiftShaft):
        _translate = QtCore.QCoreApplication.translate
        LiftShaft.setWindowTitle(_translate("LiftShaft", "Form"))
        self.label.setText(_translate("LiftShaft", "Шахта"))
import common.resources_rc
