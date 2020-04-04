# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'digitalTable.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_digital_table(object):
    def setupUi(self, digital_table):
        digital_table.setObjectName("digital_table")
        digital_table.resize(360, 118)
        digital_table.setMinimumSize(QtCore.QSize(360, 118))
        digital_table.setMaximumSize(QtCore.QSize(360, 118))
        self.verticalLayout = QtWidgets.QVBoxLayout(digital_table)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.central = QtWidgets.QWidget(digital_table)
        self.central.setMinimumSize(QtCore.QSize(360, 118))
        self.central.setMaximumSize(QtCore.QSize(360, 118))
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
        self.verticalLayout_2.setContentsMargins(10, 8, 10, 8)
        self.verticalLayout_2.setSpacing(8)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtWidgets.QLabel(self.central)
        self.label.setMinimumSize(QtCore.QSize(340, 36))
        self.label.setMaximumSize(QtCore.QSize(340, 36))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.digital = QtWidgets.QWidget(self.central)
        self.digital.setMinimumSize(QtCore.QSize(340, 0))
        self.digital.setMaximumSize(QtCore.QSize(340, 16777215))
        self.digital.setObjectName("digital")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.digital)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.down_lb = QtWidgets.QLabel(self.digital)
        self.down_lb.setMinimumSize(QtCore.QSize(30, 30))
        self.down_lb.setMaximumSize(QtCore.QSize(30, 30))
        self.down_lb.setStyleSheet("QLabel {\n"
                                   "border-image: url(:/pointers/down_off.png);\n"
                                   "}")
        self.down_lb.setText("")
        self.down_lb.setAlignment(QtCore.Qt.AlignCenter)
        self.down_lb.setObjectName("down_lb")
        self.horizontalLayout.addWidget(self.down_lb)
        self.floor_lb_1 = QtWidgets.QLabel(self.digital)
        self.floor_lb_1.setMinimumSize(QtCore.QSize(56, 30))
        self.floor_lb_1.setMaximumSize(QtCore.QSize(56, 30))
        self.floor_lb_1.setStyleSheet("QLabel {\n"
                                      "    background-color: rgb(83, 83, 83);\n"
                                      "    font: 75 15pt \"MS Shell Dlg 2\";\n"
                                      "    color: rgb(150, 150, 150);\n"
                                      "    border-style: outset;\n"
                                      "    border-width: 3px;\n"
                                      "    border-color: black;\n"
                                      "}")
        self.floor_lb_1.setAlignment(QtCore.Qt.AlignCenter)
        self.floor_lb_1.setObjectName("floor_lb_1")
        self.horizontalLayout.addWidget(self.floor_lb_1)
        self.floor_lb_2 = QtWidgets.QLabel(self.digital)
        self.floor_lb_2.setMinimumSize(QtCore.QSize(56, 30))
        self.floor_lb_2.setMaximumSize(QtCore.QSize(56, 30))
        self.floor_lb_2.setStyleSheet("QLabel {\n"
                                      "    background-color: rgb(83, 83, 83);\n"
                                      "    font: 75 15pt \"MS Shell Dlg 2\";\n"
                                      "    color: rgb(150, 150, 150);\n"
                                      "    border-style: outset;\n"
                                      "    border-width: 3px;\n"
                                      "    border-color: black;\n"
                                      "}")
        self.floor_lb_2.setAlignment(QtCore.Qt.AlignCenter)
        self.floor_lb_2.setObjectName("floor_lb_2")
        self.horizontalLayout.addWidget(self.floor_lb_2)
        self.floor_lb_3 = QtWidgets.QLabel(self.digital)
        self.floor_lb_3.setMinimumSize(QtCore.QSize(56, 30))
        self.floor_lb_3.setMaximumSize(QtCore.QSize(56, 30))
        self.floor_lb_3.setStyleSheet("QLabel {\n"
                                      "    background-color: rgb(83, 83, 83);\n"
                                      "    font: 75 15pt \"MS Shell Dlg 2\";\n"
                                      "    color: rgb(150, 150, 150);\n"
                                      "    border-style: outset;\n"
                                      "    border-width: 3px;\n"
                                      "    border-color: black;\n"
                                      "}")
        self.floor_lb_3.setAlignment(QtCore.Qt.AlignCenter)
        self.floor_lb_3.setObjectName("floor_lb_3")
        self.horizontalLayout.addWidget(self.floor_lb_3)
        self.floor_lb_4 = QtWidgets.QLabel(self.digital)
        self.floor_lb_4.setMinimumSize(QtCore.QSize(56, 30))
        self.floor_lb_4.setMaximumSize(QtCore.QSize(56, 30))
        self.floor_lb_4.setStyleSheet("QLabel {\n"
                                      "    background-color: rgb(83, 83, 83);\n"
                                      "    font: 75 15pt \"MS Shell Dlg 2\";\n"
                                      "    color: rgb(150, 150, 150);\n"
                                      "    border-style: outset;\n"
                                      "    border-width: 3px;\n"
                                      "    border-color: black;\n"
                                      "}")
        self.floor_lb_4.setAlignment(QtCore.Qt.AlignCenter)
        self.floor_lb_4.setObjectName("floor_lb_4")
        self.horizontalLayout.addWidget(self.floor_lb_4)
        self.floor_lb_5 = QtWidgets.QLabel(self.digital)
        self.floor_lb_5.setMinimumSize(QtCore.QSize(56, 30))
        self.floor_lb_5.setMaximumSize(QtCore.QSize(56, 30))
        self.floor_lb_5.setStyleSheet("QLabel {\n"
                                      "    background-color: rgb(83, 83, 83);\n"
                                      "    font: 75 15pt \"MS Shell Dlg 2\";\n"
                                      "    color: rgb(150, 150, 150);\n"
                                      "    border-style: outset;\n"
                                      "    border-width: 3px;\n"
                                      "    border-color: black;\n"
                                      "}")
        self.floor_lb_5.setAlignment(QtCore.Qt.AlignCenter)
        self.floor_lb_5.setObjectName("floor_lb_5")
        self.horizontalLayout.addWidget(self.floor_lb_5)
        self.up_lb = QtWidgets.QLabel(self.digital)
        self.up_lb.setMinimumSize(QtCore.QSize(30, 30))
        self.up_lb.setMaximumSize(QtCore.QSize(30, 30))
        self.up_lb.setStyleSheet("QLabel {\n"
                                 "border-image: url(:/pointers/up_off.png);\n"
                                 "}")
        self.up_lb.setText("")
        self.up_lb.setAlignment(QtCore.Qt.AlignCenter)
        self.up_lb.setObjectName("up_lb")
        self.horizontalLayout.addWidget(self.up_lb)
        self.verticalLayout_2.addWidget(self.digital)
        self.widget = QtWidgets.QWidget(self.central)
        self.widget.setObjectName("widget")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.floor_btn_1 = QtWidgets.QPushButton(self.widget)
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
        self.horizontalLayout_3.addWidget(self.floor_btn_1)
        self.floor_btn_2 = QtWidgets.QPushButton(self.widget)
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
        self.horizontalLayout_3.addWidget(self.floor_btn_2)
        self.floor_btn_3 = QtWidgets.QPushButton(self.widget)
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
        self.horizontalLayout_3.addWidget(self.floor_btn_3)
        self.floor_btn_4 = QtWidgets.QPushButton(self.widget)
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
        self.horizontalLayout_3.addWidget(self.floor_btn_4)
        self.floor_btn_5 = QtWidgets.QPushButton(self.widget)
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
        self.horizontalLayout_3.addWidget(self.floor_btn_5)
        self.verticalLayout_2.addWidget(self.widget)
        self.verticalLayout.addWidget(self.central)

        self.retranslateUi(digital_table)
        QtCore.QMetaObject.connectSlotsByName(digital_table)

    def retranslateUi(self, digital_table):
        _translate = QtCore.QCoreApplication.translate
        digital_table.setWindowTitle(_translate("digital_table", "Form"))
        self.label.setText(_translate("digital_table", "Кабина"))
        self.floor_lb_1.setText(_translate("digital_table", "1"))
        self.floor_lb_2.setText(_translate("digital_table", "2"))
        self.floor_lb_3.setText(_translate("digital_table", "3"))
        self.floor_lb_4.setText(_translate("digital_table", "4"))
        self.floor_lb_5.setText(_translate("digital_table", "5"))


import common.resources_rc
