# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'checkinmodify.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(409, 428)
        Dialog.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.gridLayoutWidget = QtWidgets.QWidget(Dialog)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(40, 30, 341, 331))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label_2 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 3, 0, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.gridLayout.addWidget(self.label_9, 5, 0, 1, 1)
        self.label_13 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        self.gridLayout.addWidget(self.label_13, 6, 0, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.gridLayout.addWidget(self.label_10, 4, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 0, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 2, 0, 1, 1)
        self.lineEdit_name = QtWidgets.QLineEdit(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(10)
        self.lineEdit_name.setFont(font)
        self.lineEdit_name.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_name.setObjectName("lineEdit_name")
        self.gridLayout.addWidget(self.lineEdit_name, 0, 1, 1, 1)
        self.lineEdit_sno = QtWidgets.QLineEdit(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(10)
        self.lineEdit_sno.setFont(font)
        self.lineEdit_sno.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_sno.setObjectName("lineEdit_sno")
        self.gridLayout.addWidget(self.lineEdit_sno, 1, 1, 1, 1)
        self.lineEdit_course = QtWidgets.QLineEdit(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(10)
        self.lineEdit_course.setFont(font)
        self.lineEdit_course.setText("")
        self.lineEdit_course.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_course.setObjectName("lineEdit_course")
        self.gridLayout.addWidget(self.lineEdit_course, 2, 1, 1, 1)
        self.timeEdit_start = QtWidgets.QTimeEdit(self.gridLayoutWidget)
        self.timeEdit_start.setMinimumSize(QtCore.QSize(25, 25))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        self.timeEdit_start.setFont(font)
        self.timeEdit_start.setObjectName("timeEdit_start")
        self.gridLayout.addWidget(self.timeEdit_start, 4, 1, 1, 1)
        self.lineEdit_classroom = QtWidgets.QLineEdit(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(10)
        self.lineEdit_classroom.setFont(font)
        self.lineEdit_classroom.setText("")
        self.lineEdit_classroom.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_classroom.setObjectName("lineEdit_classroom")
        self.gridLayout.addWidget(self.lineEdit_classroom, 3, 1, 1, 1)
        self.timeEdit_end = QtWidgets.QTimeEdit(self.gridLayoutWidget)
        self.timeEdit_end.setMinimumSize(QtCore.QSize(0, 25))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        self.timeEdit_end.setFont(font)
        self.timeEdit_end.setObjectName("timeEdit_end")
        self.gridLayout.addWidget(self.timeEdit_end, 5, 1, 1, 1)
        self.label_14 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_14.setFont(font)
        self.label_14.setObjectName("label_14")
        self.gridLayout.addWidget(self.label_14, 7, 0, 1, 1)
        self.radioButton_late = QtWidgets.QRadioButton(self.gridLayoutWidget)
        self.radioButton_late.setObjectName("radioButton_late")
        self.gridLayout.addWidget(self.radioButton_late, 7, 1, 1, 1)
        self.timeEdit_checkin = QtWidgets.QTimeEdit(self.gridLayoutWidget)
        self.timeEdit_checkin.setMinimumSize(QtCore.QSize(0, 25))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        self.timeEdit_checkin.setFont(font)
        self.timeEdit_checkin.setObjectName("timeEdit_checkin")
        self.gridLayout.addWidget(self.timeEdit_checkin, 6, 1, 1, 1)
        self.pushButton_add = QtWidgets.QPushButton(Dialog)
        self.pushButton_add.setGeometry(QtCore.QRect(150, 380, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_add.setFont(font)
        self.pushButton_add.setStyleSheet("QPushButton{\n"
"    \n"
"    color: rgb(255, 255, 255);\n"
"    border-width: 1px;\n"
"    border-radius: 6px;\n"
"    border-bottom-color: rgb(150,150,150);\n"
"    border-right-color: rgb(165,165,165);\n"
"    border-left-color: rgb(165,165,165);\n"
"    border-top-color: rgb(180,180,180);\n"
"    border-style: solid;\n"
"    padding: 4px;\n"
"    background-color: rgb(69, 90, 100);\n"
"}\n"
"QPushButton:hover{\n"
"    color: rgb(255, 255, 255);\n"
"    border-width: 1px;\n"
"    border-radius:6px;\n"
"    border-top-color: rgb(255,150,60);\n"
"    border-right-color: qlineargradient(spread:pad, x1:0, y1:1, x2:1, y2:0, stop:0 rgba(200, 70, 20, 255), stop:1 rgba(255,150,60, 255));\n"
"    border-left-color:  qlineargradient(spread:pad, x1:1, y1:0, x2:0, y2:0, stop:0 rgba(200, 70, 20, 255), stop:1 rgba(255,150,60, 255));\n"
"    border-bottom-color: rgb(200,70,20);\n"
"    border-style: solid;\n"
"    padding: 2px;\n"
"    background-color: rgb(69, 90, 100);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"    color: rgb(255, 255, 255);\n"
"    border-width: 1px;\n"
"    border-radius: 6px;\n"
"    border-width: 1px;\n"
"    border-top-color: rgba(255,150,60,200);\n"
"    border-right-color: qlineargradient(spread:pad, x1:0, y1:1, x2:1, y2:0, stop:0 rgba(200, 70, 20, 255), stop:1 rgba(255,150,60, 200));\n"
"    border-left-color:  qlineargradient(spread:pad, x1:1, y1:0, x2:0, y2:0, stop:0 rgba(200, 70, 20, 255), stop:1 rgba(255,150,60, 200));\n"
"    border-bottom-color: rgba(200,70,20,200);\n"
"    border-style: solid;\n"
"    padding: 2px;\n"
"    \n"
"    background-color: rgb(129, 156, 169);\n"
"    \n"
"}")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icon/pic/add.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_add.setIcon(icon)
        self.pushButton_add.setObjectName("pushButton_add")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Check-in Record Modify"))
        self.label_2.setText(_translate("Dialog", "学生ID:"))
        self.label_7.setText(_translate("Dialog", "班级:"))
        self.label_9.setText(_translate("Dialog", "结束时间:"))
        self.label_13.setText(_translate("Dialog", "签到时间:"))
        self.label_10.setText(_translate("Dialog", "开始时间:"))
        self.label_3.setText(_translate("Dialog", "姓名:"))
        self.label_4.setText(_translate("Dialog", "课程:"))
        self.label_14.setText(_translate("Dialog", "迟到:"))
        self.radioButton_late.setText(_translate("Dialog", "是"))
        self.pushButton_add.setText(_translate("Dialog", " 保存"))
import resource_rc
