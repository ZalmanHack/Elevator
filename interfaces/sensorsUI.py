# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'sensors.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_sensors(object):
    def setupUi(self, sensors):
        sensors.setObjectName("sensors")
        sensors.resize(360, 242)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(sensors.sizePolicy().hasHeightForWidth())
        sensors.setSizePolicy(sizePolicy)
        sensors.setMinimumSize(QtCore.QSize(360, 242))
        sensors.setMaximumSize(QtCore.QSize(360, 242))
        self.verticalLayout = QtWidgets.QVBoxLayout(sensors)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.central = QtWidgets.QWidget(sensors)
        self.central.setMinimumSize(QtCore.QSize(360, 242))
        self.central.setMaximumSize(QtCore.QSize(360, 242))
        self.central.setStyleSheet("QWidget#central {\n"
"    background-color: qlineargradient(spread:pad, x1:0.216, y1:1, x2:1, y2:0, stop:0 rgba(211, 183, 49, 255), stop:0.494318 rgba(234, 210, 98, 255), stop:0.568182 rgba(242, 239, 224, 255), stop:0.784091 rgba(242, 203, 19, 255), stop:1 rgba(242, 218, 100, 255));\n"
"\n"
"    border-style: outset;\n"
"    border-radius: 10px;\n"
"    border-width: 3px;\n"
"    border-color: rgb(223, 186, 17);\n"
"}")
        self.central.setObjectName("central")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.central)
        self.verticalLayout_3.setContentsMargins(10, 8, 10, 8)
        self.verticalLayout_3.setSpacing(8)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label = QtWidgets.QLabel(self.central)
        self.label.setMinimumSize(QtCore.QSize(340, 36))
        self.label.setMaximumSize(QtCore.QSize(340, 36))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout_3.addWidget(self.label)
        self.widget = QtWidgets.QWidget(self.central)
        self.widget.setStyleSheet("QWidget#widget {\n"
"    border-radius: 10px;\n"
"    background-color: rgb(112, 112, 112);\n"
"}")
        self.widget.setObjectName("widget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_2.setContentsMargins(8, 8, 8, 8)
        self.verticalLayout_2.setSpacing(10)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setSpacing(10)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_14 = QtWidgets.QLabel(self.widget)
        self.label_14.setStyleSheet("    font: 75 14pt \"MS Shell Dlg 2\";\n"
"    color: rgb(240, 240, 240);")
        self.label_14.setObjectName("label_14")
        self.horizontalLayout_3.addWidget(self.label_14)
        self.light_stp = QtWidgets.QLabel(self.widget)
        self.light_stp.setMinimumSize(QtCore.QSize(16, 16))
        self.light_stp.setMaximumSize(QtCore.QSize(16, 16))
        self.light_stp.setStyleSheet("QLabel {\n"
"    border-style: outset;\n"
"    border-radius: 8px;\n"
"    border-width: 2px;\n"
"    border-color: rgb(0, 0, 0);\n"
"    background-color: rgb(255, 0, 0)\n"
"}")
        self.light_stp.setText("")
        self.light_stp.setObjectName("light_stp")
        self.horizontalLayout_3.addWidget(self.light_stp)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setSpacing(10)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_12 = QtWidgets.QLabel(self.widget)
        self.label_12.setStyleSheet("    font: 75 14pt \"MS Shell Dlg 2\";\n"
"    color: rgb(240, 240, 240);")
        self.label_12.setObjectName("label_12")
        self.horizontalLayout_2.addWidget(self.label_12)
        self.light_ls = QtWidgets.QLabel(self.widget)
        self.light_ls.setMinimumSize(QtCore.QSize(16, 16))
        self.light_ls.setMaximumSize(QtCore.QSize(16, 16))
        self.light_ls.setStyleSheet("QLabel {\n"
"    border-style: outset;\n"
"    border-radius: 8px;\n"
"    border-width: 2px;\n"
"    border-color: rgb(0, 0, 0);\n"
"    background-color: rgb(255, 0, 0)\n"
"}")
        self.light_ls.setText("")
        self.light_ls.setObjectName("light_ls")
        self.horizontalLayout_2.addWidget(self.light_ls)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSpacing(10)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_13 = QtWidgets.QLabel(self.widget)
        self.label_13.setStyleSheet("    font: 75 14pt \"MS Shell Dlg 2\";\n"
"    color: rgb(240, 240, 240);")
        self.label_13.setObjectName("label_13")
        self.horizontalLayout.addWidget(self.label_13)
        self.light_fl_1 = QtWidgets.QLabel(self.widget)
        self.light_fl_1.setMinimumSize(QtCore.QSize(16, 16))
        self.light_fl_1.setMaximumSize(QtCore.QSize(16, 16))
        self.light_fl_1.setStyleSheet("QLabel {\n"
"    border-style: outset;\n"
"    border-radius: 8px;\n"
"    border-width: 2px;\n"
"    border-color: rgb(0, 0, 0);\n"
"    background-color: rgb(255, 0, 0)\n"
"}")
        self.light_fl_1.setText("")
        self.light_fl_1.setObjectName("light_fl_1")
        self.horizontalLayout.addWidget(self.light_fl_1)
        self.light_fl_2 = QtWidgets.QLabel(self.widget)
        self.light_fl_2.setMinimumSize(QtCore.QSize(16, 16))
        self.light_fl_2.setMaximumSize(QtCore.QSize(16, 16))
        self.light_fl_2.setStyleSheet("QLabel {\n"
"    border-style: outset;\n"
"    border-radius: 8px;\n"
"    border-width: 2px;\n"
"    border-color: rgb(0, 0, 0);\n"
"    background-color: rgb(255, 0, 0)\n"
"}")
        self.light_fl_2.setText("")
        self.light_fl_2.setObjectName("light_fl_2")
        self.horizontalLayout.addWidget(self.light_fl_2)
        self.light_fl_3 = QtWidgets.QLabel(self.widget)
        self.light_fl_3.setMinimumSize(QtCore.QSize(16, 16))
        self.light_fl_3.setMaximumSize(QtCore.QSize(16, 16))
        self.light_fl_3.setStyleSheet("QLabel {\n"
"    border-style: outset;\n"
"    border-radius: 8px;\n"
"    border-width: 2px;\n"
"    border-color: rgb(0, 0, 0);\n"
"    background-color: rgb(255, 0, 0)\n"
"}")
        self.light_fl_3.setText("")
        self.light_fl_3.setObjectName("light_fl_3")
        self.horizontalLayout.addWidget(self.light_fl_3)
        self.light_fl_4 = QtWidgets.QLabel(self.widget)
        self.light_fl_4.setMinimumSize(QtCore.QSize(16, 16))
        self.light_fl_4.setMaximumSize(QtCore.QSize(16, 16))
        self.light_fl_4.setStyleSheet("QLabel {\n"
"    border-style: outset;\n"
"    border-radius: 8px;\n"
"    border-width: 2px;\n"
"    border-color: rgb(0, 0, 0);\n"
"    background-color: rgb(255, 0, 0)\n"
"}")
        self.light_fl_4.setText("")
        self.light_fl_4.setObjectName("light_fl_4")
        self.horizontalLayout.addWidget(self.light_fl_4)
        self.light_fl_5 = QtWidgets.QLabel(self.widget)
        self.light_fl_5.setMinimumSize(QtCore.QSize(16, 16))
        self.light_fl_5.setMaximumSize(QtCore.QSize(16, 16))
        self.light_fl_5.setStyleSheet("QLabel {\n"
"    border-style: outset;\n"
"    border-radius: 8px;\n"
"    border-width: 2px;\n"
"    border-color: rgb(0, 0, 0);\n"
"    background-color: rgb(255, 0, 0)\n"
"}")
        self.light_fl_5.setText("")
        self.light_fl_5.setObjectName("light_fl_5")
        self.horizontalLayout.addWidget(self.light_fl_5)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setSpacing(10)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_15 = QtWidgets.QLabel(self.widget)
        self.label_15.setStyleSheet("    font: 75 14pt \"MS Shell Dlg 2\";\n"
"    color: rgb(240, 240, 240);")
        self.label_15.setObjectName("label_15")
        self.horizontalLayout_4.addWidget(self.label_15)
        self.weight_down_btn = QtWidgets.QPushButton(self.widget)
        self.weight_down_btn.setMinimumSize(QtCore.QSize(23, 0))
        self.weight_down_btn.setMaximumSize(QtCore.QSize(23, 16777215))
        self.weight_down_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.weight_down_btn.setStyleSheet("QPushButton {\n"
"    border-radius: 8px;\n"
"    background-color: rgb(0, 0, 0);\n"
"    font: 75 14pt \"MS Shell Dlg 2\";\n"
"    color: rgb(255, 0, 0);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(50, 50, 50);\n"
"}")
        self.weight_down_btn.setObjectName("weight_down_btn")
        self.horizontalLayout_4.addWidget(self.weight_down_btn)
        self.cab_weight = QtWidgets.QLabel(self.widget)
        self.cab_weight.setMinimumSize(QtCore.QSize(0, 0))
        self.cab_weight.setMaximumSize(QtCore.QSize(90, 16777215))
        self.cab_weight.setStyleSheet("QLabel {\n"
"    border-radius: 8px;\n"
"    background-color: rgb(0, 0, 0);\n"
"    font: 75 14pt \"MS Shell Dlg 2\";\n"
"    color: rgb(255, 0, 0);\n"
"}")
        self.cab_weight.setAlignment(QtCore.Qt.AlignCenter)
        self.cab_weight.setObjectName("cab_weight")
        self.horizontalLayout_4.addWidget(self.cab_weight)
        self.weight_up_btn = QtWidgets.QPushButton(self.widget)
        self.weight_up_btn.setMinimumSize(QtCore.QSize(23, 0))
        self.weight_up_btn.setMaximumSize(QtCore.QSize(23, 16777215))
        self.weight_up_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.weight_up_btn.setStyleSheet("QPushButton {\n"
"    border-radius: 8px;\n"
"    background-color: rgb(0, 0, 0);\n"
"    font: 75 14pt \"MS Shell Dlg 2\";\n"
"    color: rgb(255, 0, 0);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(50, 50, 50);\n"
"}")
        self.weight_up_btn.setObjectName("weight_up_btn")
        self.horizontalLayout_4.addWidget(self.weight_up_btn)
        self.light_cw = QtWidgets.QLabel(self.widget)
        self.light_cw.setMinimumSize(QtCore.QSize(16, 16))
        self.light_cw.setMaximumSize(QtCore.QSize(16, 16))
        self.light_cw.setStyleSheet("QLabel {\n"
"    border-style: outset;\n"
"    border-radius: 8px;\n"
"    border-width: 2px;\n"
"    border-color: rgb(0, 0, 0);\n"
"    background-color: rgb(255, 0, 0)\n"
"}")
        self.light_cw.setText("")
        self.light_cw.setObjectName("light_cw")
        self.horizontalLayout_4.addWidget(self.light_cw)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setSpacing(10)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_16 = QtWidgets.QLabel(self.widget)
        self.label_16.setStyleSheet("    font: 75 14pt \"MS Shell Dlg 2\";\n"
"    color: rgb(240, 240, 240);")
        self.label_16.setObjectName("label_16")
        self.horizontalLayout_5.addWidget(self.label_16)
        self.label_17 = QtWidgets.QLabel(self.widget)
        self.label_17.setStyleSheet("    font: 75 14pt \"MS Shell Dlg 2\";\n"
"    color: rgb(240, 240, 240);")
        self.label_17.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_17.setObjectName("label_17")
        self.horizontalLayout_5.addWidget(self.label_17)
        self.light_door_op = QtWidgets.QLabel(self.widget)
        self.light_door_op.setMinimumSize(QtCore.QSize(16, 16))
        self.light_door_op.setMaximumSize(QtCore.QSize(16, 16))
        self.light_door_op.setStyleSheet("QLabel {\n"
"    border-style: outset;\n"
"    border-radius: 8px;\n"
"    border-width: 2px;\n"
"    border-color: rgb(0, 0, 0);\n"
"    background-color: rgb(255, 0, 0)\n"
"}")
        self.light_door_op.setText("")
        self.light_door_op.setObjectName("light_door_op")
        self.horizontalLayout_5.addWidget(self.light_door_op)
        self.label_18 = QtWidgets.QLabel(self.widget)
        self.label_18.setStyleSheet("    font: 75 14pt \"MS Shell Dlg 2\";\n"
"    color: rgb(240, 240, 240);")
        self.label_18.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_18.setObjectName("label_18")
        self.horizontalLayout_5.addWidget(self.label_18)
        self.light_door_md = QtWidgets.QLabel(self.widget)
        self.light_door_md.setMinimumSize(QtCore.QSize(16, 16))
        self.light_door_md.setMaximumSize(QtCore.QSize(16, 16))
        self.light_door_md.setStyleSheet("QLabel {\n"
"    border-style: outset;\n"
"    border-radius: 8px;\n"
"    border-width: 2px;\n"
"    border-color: rgb(0, 0, 0);\n"
"    background-color: rgb(255, 0, 0)\n"
"}")
        self.light_door_md.setText("")
        self.light_door_md.setObjectName("light_door_md")
        self.horizontalLayout_5.addWidget(self.light_door_md)
        self.label_19 = QtWidgets.QLabel(self.widget)
        self.label_19.setStyleSheet("    font: 75 14pt \"MS Shell Dlg 2\";\n"
"    color: rgb(240, 240, 240);")
        self.label_19.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_19.setObjectName("label_19")
        self.horizontalLayout_5.addWidget(self.label_19)
        self.light_door_cl = QtWidgets.QLabel(self.widget)
        self.light_door_cl.setMinimumSize(QtCore.QSize(16, 16))
        self.light_door_cl.setMaximumSize(QtCore.QSize(16, 16))
        self.light_door_cl.setStyleSheet("QLabel {\n"
"    border-style: outset;\n"
"    border-radius: 8px;\n"
"    border-width: 2px;\n"
"    border-color: rgb(0, 0, 0);\n"
"    background-color: rgb(255, 0, 0)\n"
"}")
        self.light_door_cl.setText("")
        self.light_door_cl.setObjectName("light_door_cl")
        self.horizontalLayout_5.addWidget(self.light_door_cl)
        self.verticalLayout_2.addLayout(self.horizontalLayout_5)
        self.verticalLayout_3.addWidget(self.widget)
        self.verticalLayout.addWidget(self.central)

        self.retranslateUi(sensors)
        QtCore.QMetaObject.connectSlotsByName(sensors)

    def retranslateUi(self, sensors):
        _translate = QtCore.QCoreApplication.translate
        sensors.setWindowTitle(_translate("sensors", "Form"))
        self.label.setText(_translate("sensors", "Датчики"))
        self.label_14.setText(_translate("sensors", "стопоры"))
        self.label_12.setText(_translate("sensors", "предварительное торможение"))
        self.label_13.setText(_translate("sensors", "точная остановка"))
        self.label_15.setText(_translate("sensors", "Вес кабины"))
        self.weight_down_btn.setText(_translate("sensors", "-"))
        self.cab_weight.setText(_translate("sensors", "450"))
        self.weight_up_btn.setText(_translate("sensors", "+"))
        self.label_16.setText(_translate("sensors", "Двери"))
        self.label_17.setText(_translate("sensors", "<||>"))
        self.label_18.setText(_translate("sensors", "|.|"))
        self.label_19.setText(_translate("sensors", ">||<"))
