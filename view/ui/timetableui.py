# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'timetableui.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(972, 465)
        Form.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_tablecard = QtWidgets.QLabel(Form)
        self.label_tablecard.setGeometry(QtCore.QRect(0, 10, 731, 441))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_tablecard.setFont(font)
        self.label_tablecard.setStyleSheet("border-image: url(:/icon/pic/table_card.png);\n"
"")
        self.label_tablecard.setText("")
        self.label_tablecard.setAlignment(QtCore.Qt.AlignCenter)
        self.label_tablecard.setObjectName("label_tablecard")
        self.pushButton_add = QtWidgets.QPushButton(Form)
        self.pushButton_add.setGeometry(QtCore.QRect(780, 330, 131, 41))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
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
"QPushButton:default{\n"
"    color: rgb(255, 255, 255);\n"
"    border-width: 1px;\n"
"    border-radius:6px;\n"
"    border-top-color: rgb(255,150,60);\n"
"    border-right-color: qlineargradient(spread:pad, x1:0, y1:1, x2:1, y2:0, stop:0 rgba(200, 70, 20, 255), stop:1 rgba(255,150,60, 255));\n"
"    border-left-color:  qlineargradient(spread:pad, x1:1, y1:0, x2:0, y2:0, stop:0 rgba(200, 70, 20, 255), stop:1 rgba(255,150,60, 255));\n"
"    border-bottom-color: rgb(200,70,20);\n"
"    border-style: solid;\n"
"    padding: 2px;\n"
"    background-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(220, 220, 220, 255), stop:1 rgba(255, 255, 255, 255));\n"
"}\n"
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
        self.gridLayoutWidget = QtWidgets.QWidget(Form)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(730, 10, 231, 311))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 4, 0, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 6, 0, 1, 1)
        self.lineEdit_course = QtWidgets.QLineEdit(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(10)
        self.lineEdit_course.setFont(font)
        self.lineEdit_course.setObjectName("lineEdit_course")
        self.gridLayout.addWidget(self.lineEdit_course, 3, 1, 1, 1)
        self.timeEdit_end = QtWidgets.QTimeEdit(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(10)
        self.timeEdit_end.setFont(font)
        self.timeEdit_end.setObjectName("timeEdit_end")
        self.gridLayout.addWidget(self.timeEdit_end, 6, 1, 1, 1)
        self.timeEdit_start = QtWidgets.QTimeEdit(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(10)
        self.timeEdit_start.setFont(font)
        self.timeEdit_start.setObjectName("timeEdit_start")
        self.gridLayout.addWidget(self.timeEdit_start, 5, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 3, 0, 1, 1)
        self.lineEdit_classroom = QtWidgets.QLineEdit(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(10)
        self.lineEdit_classroom.setFont(font)
        self.lineEdit_classroom.setObjectName("lineEdit_classroom")
        self.gridLayout.addWidget(self.lineEdit_classroom, 4, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 5, 0, 1, 1)
        self.comboBox_day = QtWidgets.QComboBox(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(10)
        self.comboBox_day.setFont(font)
        self.comboBox_day.setStyleSheet("QComboBox {\n"
"    \n"
"    border-color: rgb(69, 90, 100);\n"
"    border: 1px solid gray;\n"
"    border-radius: 3px;\n"
"    padding: 1px 2px 1px 2px;\n"
"    min-width: 30px;\n"
"\n"
"}\n"
"QComboBox::drop-down {\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    width: 30px;\n"
"\n"
"    border-left-width: 1px;\n"
"    border-left-color: darkgray;\n"
"    border-left-style: solid; /* just a single line */\n"
"    border-top-right-radius: 3px; /* same radius as the QComboBox */\n"
"    border-bottom-right-radius: 3px;\n"
"}\n"
"QComboBox::down-arrow {\n"
"    \n"
"    image: url(:/icon/pic/week.png);\n"
"}\n"
"")
        self.comboBox_day.setObjectName("comboBox_day")
        self.comboBox_day.addItem("")
        self.comboBox_day.addItem("")
        self.comboBox_day.addItem("")
        self.comboBox_day.addItem("")
        self.comboBox_day.addItem("")
        self.comboBox_day.addItem("")
        self.comboBox_day.addItem("")
        self.gridLayout.addWidget(self.comboBox_day, 1, 1, 1, 1)
        self.label_11 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.gridLayout.addWidget(self.label_11, 2, 0, 1, 1)
        self.comboBox_no = QtWidgets.QComboBox(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(10)
        self.comboBox_no.setFont(font)
        self.comboBox_no.setStyleSheet("QComboBox {\n"
"    \n"
"    border-color: rgb(69, 90, 100);\n"
"    border: 1px solid gray;\n"
"    border-radius: 3px;\n"
"    padding: 1px 2px 1px 2px;\n"
"    min-width: 30px;\n"
"\n"
"}\n"
"QComboBox::drop-down {\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    width: 30px;\n"
"\n"
"    border-left-width: 1px;\n"
"    border-left-color: darkgray;\n"
"    border-left-style: solid; /* just a single line */\n"
"    border-top-right-radius: 3px; /* same radius as the QComboBox */\n"
"    border-bottom-right-radius: 3px;\n"
"}\n"
"QComboBox::down-arrow {\n"
"    \n"
"    image: url(:/icon/pic/number.png);\n"
"}\n"
"")
        self.comboBox_no.setObjectName("comboBox_no")
        self.comboBox_no.addItem("")
        self.comboBox_no.addItem("")
        self.comboBox_no.addItem("")
        self.comboBox_no.addItem("")
        self.gridLayout.addWidget(self.comboBox_no, 2, 1, 1, 1)
        self.label_12 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.gridLayout.addWidget(self.label_12, 0, 0, 1, 1)
        self.lineEdit_sid = QtWidgets.QLineEdit(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(10)
        self.lineEdit_sid.setFont(font)
        self.lineEdit_sid.setDragEnabled(True)
        self.lineEdit_sid.setObjectName("lineEdit_sid")
        self.gridLayout.addWidget(self.lineEdit_sid, 0, 1, 1, 1)
        self.label_10 = QtWidgets.QLabel(Form)
        self.label_10.setGeometry(QtCore.QRect(620, 30, 61, 31))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_10.setFont(font)
        self.label_10.setStyleSheet("background-color: rgb(69, 90, 100);\n"
"color: rgb(255, 255, 255);")
        self.label_10.setObjectName("label_10")
        self.label_9 = QtWidgets.QLabel(Form)
        self.label_9.setGeometry(QtCore.QRect(470, 30, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setStyleSheet("background-color: rgb(69, 90, 100);\n"
"color: rgb(255, 255, 255);")
        self.label_9.setObjectName("label_9")
        self.label_8 = QtWidgets.QLabel(Form)
        self.label_8.setGeometry(QtCore.QRect(320, 30, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("background-color: rgb(69, 90, 100);\n"
"color: rgb(255, 255, 255);")
        self.label_8.setObjectName("label_8")
        self.label_7 = QtWidgets.QLabel(Form)
        self.label_7.setGeometry(QtCore.QRect(190, 30, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("background-color: rgb(69, 90, 100);\n"
"color: rgb(255, 255, 255);")
        self.label_7.setObjectName("label_7")
        self.label_6 = QtWidgets.QLabel(Form)
        self.label_6.setGeometry(QtCore.QRect(50, 30, 61, 31))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("background-color: rgb(69, 90, 100);\n"
"color: rgb(255, 255, 255);")
        self.label_6.setObjectName("label_6")
        self.pushButton_save = QtWidgets.QPushButton(Form)
        self.pushButton_save.setGeometry(QtCore.QRect(780, 390, 131, 41))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_save.setFont(font)
        self.pushButton_save.setStyleSheet("QPushButton{\n"
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
"QPushButton:default{\n"
"    color: rgb(255, 255, 255);\n"
"    border-width: 1px;\n"
"    border-radius:6px;\n"
"    border-top-color: rgb(255,150,60);\n"
"    border-right-color: qlineargradient(spread:pad, x1:0, y1:1, x2:1, y2:0, stop:0 rgba(200, 70, 20, 255), stop:1 rgba(255,150,60, 255));\n"
"    border-left-color:  qlineargradient(spread:pad, x1:1, y1:0, x2:0, y2:0, stop:0 rgba(200, 70, 20, 255), stop:1 rgba(255,150,60, 255));\n"
"    border-bottom-color: rgb(200,70,20);\n"
"    border-style: solid;\n"
"    padding: 2px;\n"
"    background-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(220, 220, 220, 255), stop:1 rgba(255, 255, 255, 255));\n"
"}\n"
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
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icon/pic/save.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_save.setIcon(icon1)
        self.pushButton_save.setObjectName("pushButton_save")
        self.pushButton_1_1 = QtWidgets.QPushButton(Form)
        self.pushButton_1_1.setGeometry(QtCore.QRect(20, 80, 131, 71))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(8)
        self.pushButton_1_1.setFont(font)
        self.pushButton_1_1.setStyleSheet("QPushButton{\n"
"    \n"
"    \n"
"    color: rgb(0, 0, 0);\n"
"    border-width: 1px;\n"
"    border-radius: 6px;\n"
"    \n"
"    border-color: rgb(0, 0, 0);\n"
"    border-style: solid;\n"
"    padding: 4px;\n"
"    \n"
"    background-color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton::disabled\n"
"{\n"
"    color: rgb(0, 0, 0);\n"
"    border-width: 2px;\n"
"    border-radius: 6px;\n"
"    \n"
"    border-color: rgb(0, 0, 0);\n"
"    border-style: solid;\n"
"    padding: 4px;\n"
"    \n"
"    background-color: rgb(255, 255, 255);\n"
"}\n"
"")
        self.pushButton_1_1.setDefault(False)
        self.pushButton_1_1.setObjectName("pushButton_1_1")
        self.pushButton_2_1 = QtWidgets.QPushButton(Form)
        self.pushButton_2_1.setGeometry(QtCore.QRect(160, 80, 131, 71))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(8)
        self.pushButton_2_1.setFont(font)
        self.pushButton_2_1.setStyleSheet("QPushButton{\n"
"    \n"
"    \n"
"    color: rgb(0, 0, 0);\n"
"    border-width: 1px;\n"
"    border-radius: 6px;\n"
"    \n"
"    border-color: rgb(0, 0, 0);\n"
"    border-style: solid;\n"
"    padding: 4px;\n"
"    \n"
"    background-color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton::disabled\n"
"{\n"
"    color: rgb(0, 0, 0);\n"
"    border-width: 2px;\n"
"    border-radius: 6px;\n"
"    \n"
"    border-color: rgb(0, 0, 0);\n"
"    border-style: solid;\n"
"    padding: 4px;\n"
"    \n"
"    background-color: rgb(255, 255, 255);\n"
"}\n"
"")
        self.pushButton_2_1.setObjectName("pushButton_2_1")
        self.pushButton_3_1 = QtWidgets.QPushButton(Form)
        self.pushButton_3_1.setGeometry(QtCore.QRect(300, 80, 131, 71))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(8)
        self.pushButton_3_1.setFont(font)
        self.pushButton_3_1.setStyleSheet("QPushButton{\n"
"    \n"
"    \n"
"    color: rgb(0, 0, 0);\n"
"    border-width: 1px;\n"
"    border-radius: 6px;\n"
"    \n"
"    border-color: rgb(0, 0, 0);\n"
"    border-style: solid;\n"
"    padding: 4px;\n"
"    \n"
"    background-color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton::disabled\n"
"{\n"
"    color: rgb(0, 0, 0);\n"
"    border-width: 2px;\n"
"    border-radius: 6px;\n"
"    \n"
"    border-color: rgb(0, 0, 0);\n"
"    border-style: solid;\n"
"    padding: 4px;\n"
"    \n"
"    background-color: rgb(255, 255, 255);\n"
"}\n"
"")
        self.pushButton_3_1.setObjectName("pushButton_3_1")
        self.pushButton_4_1 = QtWidgets.QPushButton(Form)
        self.pushButton_4_1.setGeometry(QtCore.QRect(440, 80, 131, 71))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(8)
        self.pushButton_4_1.setFont(font)
        self.pushButton_4_1.setStyleSheet("QPushButton{\n"
"    \n"
"    \n"
"    color: rgb(0, 0, 0);\n"
"    border-width: 1px;\n"
"    border-radius: 6px;\n"
"    \n"
"    border-color: rgb(0, 0, 0);\n"
"    border-style: solid;\n"
"    padding: 4px;\n"
"    \n"
"    background-color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton::disabled\n"
"{\n"
"    color: rgb(0, 0, 0);\n"
"    border-width: 2px;\n"
"    border-radius: 6px;\n"
"    \n"
"    border-color: rgb(0, 0, 0);\n"
"    border-style: solid;\n"
"    padding: 4px;\n"
"    \n"
"    background-color: rgb(255, 255, 255);\n"
"}\n"
"")
        self.pushButton_4_1.setObjectName("pushButton_4_1")
        self.pushButton_5_1 = QtWidgets.QPushButton(Form)
        self.pushButton_5_1.setGeometry(QtCore.QRect(580, 80, 131, 71))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(8)
        self.pushButton_5_1.setFont(font)
        self.pushButton_5_1.setStyleSheet("QPushButton{\n"
"    \n"
"    \n"
"    color: rgb(0, 0, 0);\n"
"    border-width: 1px;\n"
"    border-radius: 6px;\n"
"    \n"
"    border-color: rgb(0, 0, 0);\n"
"    border-style: solid;\n"
"    padding: 4px;\n"
"    \n"
"    background-color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton::disabled\n"
"{\n"
"    color: rgb(0, 0, 0);\n"
"    border-width: 2px;\n"
"    border-radius: 6px;\n"
"    \n"
"    border-color: rgb(0, 0, 0);\n"
"    border-style: solid;\n"
"    padding: 4px;\n"
"    \n"
"    background-color: rgb(255, 255, 255);\n"
"}\n"
"")
        self.pushButton_5_1.setObjectName("pushButton_5_1")
        self.pushButton_3_2 = QtWidgets.QPushButton(Form)
        self.pushButton_3_2.setGeometry(QtCore.QRect(300, 170, 131, 71))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(8)
        self.pushButton_3_2.setFont(font)
        self.pushButton_3_2.setStyleSheet("QPushButton{\n"
"    \n"
"    \n"
"    color: rgb(0, 0, 0);\n"
"    border-width: 1px;\n"
"    border-radius: 6px;\n"
"    \n"
"    border-color: rgb(0, 0, 0);\n"
"    border-style: solid;\n"
"    padding: 4px;\n"
"    \n"
"    background-color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton::disabled\n"
"{\n"
"    color: rgb(0, 0, 0);\n"
"    border-width: 2px;\n"
"    border-radius: 6px;\n"
"    \n"
"    border-color: rgb(0, 0, 0);\n"
"    border-style: solid;\n"
"    padding: 4px;\n"
"    \n"
"    background-color: rgb(255, 255, 255);\n"
"}\n"
"")
        self.pushButton_3_2.setObjectName("pushButton_3_2")
        self.pushButton_5_2 = QtWidgets.QPushButton(Form)
        self.pushButton_5_2.setGeometry(QtCore.QRect(580, 170, 131, 71))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(8)
        self.pushButton_5_2.setFont(font)
        self.pushButton_5_2.setStyleSheet("QPushButton{\n"
"    \n"
"    \n"
"    color: rgb(0, 0, 0);\n"
"    border-width: 1px;\n"
"    border-radius: 6px;\n"
"    \n"
"    border-color: rgb(0, 0, 0);\n"
"    border-style: solid;\n"
"    padding: 4px;\n"
"    \n"
"    background-color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton::disabled\n"
"{\n"
"    color: rgb(0, 0, 0);\n"
"    border-width: 2px;\n"
"    border-radius: 6px;\n"
"    \n"
"    border-color: rgb(0, 0, 0);\n"
"    border-style: solid;\n"
"    padding: 4px;\n"
"    \n"
"    background-color: rgb(255, 255, 255);\n"
"}\n"
"")
        self.pushButton_5_2.setObjectName("pushButton_5_2")
        self.pushButton_4_2 = QtWidgets.QPushButton(Form)
        self.pushButton_4_2.setGeometry(QtCore.QRect(440, 170, 131, 71))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(8)
        self.pushButton_4_2.setFont(font)
        self.pushButton_4_2.setStyleSheet("QPushButton{\n"
"    \n"
"    \n"
"    color: rgb(0, 0, 0);\n"
"    border-width: 1px;\n"
"    border-radius: 6px;\n"
"    \n"
"    border-color: rgb(0, 0, 0);\n"
"    border-style: solid;\n"
"    padding: 4px;\n"
"    \n"
"    background-color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton::disabled\n"
"{\n"
"    color: rgb(0, 0, 0);\n"
"    border-width: 2px;\n"
"    border-radius: 6px;\n"
"    \n"
"    border-color: rgb(0, 0, 0);\n"
"    border-style: solid;\n"
"    padding: 4px;\n"
"    \n"
"    background-color: rgb(255, 255, 255);\n"
"}\n"
"")
        self.pushButton_4_2.setObjectName("pushButton_4_2")
        self.pushButton_2_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2_2.setGeometry(QtCore.QRect(160, 170, 131, 71))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(8)
        self.pushButton_2_2.setFont(font)
        self.pushButton_2_2.setStyleSheet("QPushButton{\n"
"    \n"
"    \n"
"    color: rgb(0, 0, 0);\n"
"    border-width: 1px;\n"
"    border-radius: 6px;\n"
"    \n"
"    border-color: rgb(0, 0, 0);\n"
"    border-style: solid;\n"
"    padding: 4px;\n"
"    \n"
"    background-color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton::disabled\n"
"{\n"
"    color: rgb(0, 0, 0);\n"
"    border-width: 2px;\n"
"    border-radius: 6px;\n"
"    \n"
"    border-color: rgb(0, 0, 0);\n"
"    border-style: solid;\n"
"    padding: 4px;\n"
"    \n"
"    background-color: rgb(255, 255, 255);\n"
"}\n"
"")
        self.pushButton_2_2.setObjectName("pushButton_2_2")
        self.pushButton_1_2 = QtWidgets.QPushButton(Form)
        self.pushButton_1_2.setGeometry(QtCore.QRect(20, 170, 131, 71))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(8)
        self.pushButton_1_2.setFont(font)
        self.pushButton_1_2.setStyleSheet("QPushButton{\n"
"    \n"
"    \n"
"    color: rgb(0, 0, 0);\n"
"    border-width: 1px;\n"
"    border-radius: 6px;\n"
"    \n"
"    border-color: rgb(0, 0, 0);\n"
"    border-style: solid;\n"
"    padding: 4px;\n"
"    \n"
"    background-color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton::disabled\n"
"{\n"
"    color: rgb(0, 0, 0);\n"
"    border-width: 2px;\n"
"    border-radius: 6px;\n"
"    \n"
"    border-color: rgb(0, 0, 0);\n"
"    border-style: solid;\n"
"    padding: 4px;\n"
"    \n"
"    background-color: rgb(255, 255, 255);\n"
"}\n"
"")
        self.pushButton_1_2.setObjectName("pushButton_1_2")
        self.pushButton_3_3 = QtWidgets.QPushButton(Form)
        self.pushButton_3_3.setGeometry(QtCore.QRect(300, 260, 131, 71))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(8)
        self.pushButton_3_3.setFont(font)
        self.pushButton_3_3.setStyleSheet("QPushButton{\n"
"    \n"
"    \n"
"    color: rgb(0, 0, 0);\n"
"    border-width: 1px;\n"
"    border-radius: 6px;\n"
"    \n"
"    border-color: rgb(0, 0, 0);\n"
"    border-style: solid;\n"
"    padding: 4px;\n"
"    \n"
"    background-color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton::disabled\n"
"{\n"
"    color: rgb(0, 0, 0);\n"
"    border-width: 2px;\n"
"    border-radius: 6px;\n"
"    \n"
"    border-color: rgb(0, 0, 0);\n"
"    border-style: solid;\n"
"    padding: 4px;\n"
"    \n"
"    background-color: rgb(255, 255, 255);\n"
"}\n"
"")
        self.pushButton_3_3.setObjectName("pushButton_3_3")
        self.pushButton_5_3 = QtWidgets.QPushButton(Form)
        self.pushButton_5_3.setGeometry(QtCore.QRect(580, 260, 131, 71))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(8)
        self.pushButton_5_3.setFont(font)
        self.pushButton_5_3.setStyleSheet("QPushButton{\n"
"    \n"
"    \n"
"    color: rgb(0, 0, 0);\n"
"    border-width: 1px;\n"
"    border-radius: 6px;\n"
"    \n"
"    border-color: rgb(0, 0, 0);\n"
"    border-style: solid;\n"
"    padding: 4px;\n"
"    \n"
"    background-color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton::disabled\n"
"{\n"
"    color: rgb(0, 0, 0);\n"
"    border-width: 2px;\n"
"    border-radius: 6px;\n"
"    \n"
"    border-color: rgb(0, 0, 0);\n"
"    border-style: solid;\n"
"    padding: 4px;\n"
"    \n"
"    background-color: rgb(255, 255, 255);\n"
"}\n"
"")
        self.pushButton_5_3.setObjectName("pushButton_5_3")
        self.pushButton_4_3 = QtWidgets.QPushButton(Form)
        self.pushButton_4_3.setGeometry(QtCore.QRect(440, 260, 131, 71))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(8)
        self.pushButton_4_3.setFont(font)
        self.pushButton_4_3.setStyleSheet("QPushButton{\n"
"    \n"
"    \n"
"    color: rgb(0, 0, 0);\n"
"    border-width: 1px;\n"
"    border-radius: 6px;\n"
"    \n"
"    border-color: rgb(0, 0, 0);\n"
"    border-style: solid;\n"
"    padding: 4px;\n"
"    \n"
"    background-color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton::disabled\n"
"{\n"
"    color: rgb(0, 0, 0);\n"
"    border-width: 2px;\n"
"    border-radius: 6px;\n"
"    \n"
"    border-color: rgb(0, 0, 0);\n"
"    border-style: solid;\n"
"    padding: 4px;\n"
"    \n"
"    background-color: rgb(255, 255, 255);\n"
"}\n"
"")
        self.pushButton_4_3.setObjectName("pushButton_4_3")
        self.pushButton_2_3 = QtWidgets.QPushButton(Form)
        self.pushButton_2_3.setGeometry(QtCore.QRect(160, 260, 131, 71))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(8)
        self.pushButton_2_3.setFont(font)
        self.pushButton_2_3.setStyleSheet("QPushButton{\n"
"    \n"
"    \n"
"    color: rgb(0, 0, 0);\n"
"    border-width: 1px;\n"
"    border-radius: 6px;\n"
"    \n"
"    border-color: rgb(0, 0, 0);\n"
"    border-style: solid;\n"
"    padding: 4px;\n"
"    \n"
"    background-color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton::disabled\n"
"{\n"
"    color: rgb(0, 0, 0);\n"
"    border-width: 2px;\n"
"    border-radius: 6px;\n"
"    \n"
"    border-color: rgb(0, 0, 0);\n"
"    border-style: solid;\n"
"    padding: 4px;\n"
"    \n"
"    background-color: rgb(255, 255, 255);\n"
"}\n"
"")
        self.pushButton_2_3.setObjectName("pushButton_2_3")
        self.pushButton_1_3 = QtWidgets.QPushButton(Form)
        self.pushButton_1_3.setGeometry(QtCore.QRect(20, 260, 131, 71))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(8)
        self.pushButton_1_3.setFont(font)
        self.pushButton_1_3.setStyleSheet("QPushButton{\n"
"    \n"
"    \n"
"    color: rgb(0, 0, 0);\n"
"    border-width: 1px;\n"
"    border-radius: 6px;\n"
"    \n"
"    border-color: rgb(0, 0, 0);\n"
"    border-style: solid;\n"
"    padding: 4px;\n"
"    \n"
"    background-color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton::disabled\n"
"{\n"
"    color: rgb(0, 0, 0);\n"
"    border-width: 2px;\n"
"    border-radius: 6px;\n"
"    \n"
"    border-color: rgb(0, 0, 0);\n"
"    border-style: solid;\n"
"    padding: 4px;\n"
"    \n"
"    background-color: rgb(255, 255, 255);\n"
"}\n"
"")
        self.pushButton_1_3.setObjectName("pushButton_1_3")
        self.pushButton_3_4 = QtWidgets.QPushButton(Form)
        self.pushButton_3_4.setGeometry(QtCore.QRect(300, 350, 131, 71))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(8)
        self.pushButton_3_4.setFont(font)
        self.pushButton_3_4.setStyleSheet("QPushButton{\n"
"    \n"
"    \n"
"    color: rgb(0, 0, 0);\n"
"    border-width: 1px;\n"
"    border-radius: 6px;\n"
"    \n"
"    border-color: rgb(0, 0, 0);\n"
"    border-style: solid;\n"
"    padding: 4px;\n"
"    \n"
"    background-color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton::disabled\n"
"{\n"
"    color: rgb(0, 0, 0);\n"
"    border-width: 2px;\n"
"    border-radius: 6px;\n"
"    \n"
"    border-color: rgb(0, 0, 0);\n"
"    border-style: solid;\n"
"    padding: 4px;\n"
"    \n"
"    background-color: rgb(255, 255, 255);\n"
"}\n"
"")
        self.pushButton_3_4.setObjectName("pushButton_3_4")
        self.pushButton_5_4 = QtWidgets.QPushButton(Form)
        self.pushButton_5_4.setGeometry(QtCore.QRect(580, 350, 131, 71))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(8)
        self.pushButton_5_4.setFont(font)
        self.pushButton_5_4.setStyleSheet("QPushButton{\n"
"    \n"
"    \n"
"    color: rgb(0, 0, 0);\n"
"    border-width: 1px;\n"
"    border-radius: 6px;\n"
"    \n"
"    border-color: rgb(0, 0, 0);\n"
"    border-style: solid;\n"
"    padding: 4px;\n"
"    \n"
"    background-color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton::disabled\n"
"{\n"
"    color: rgb(0, 0, 0);\n"
"    border-width: 2px;\n"
"    border-radius: 6px;\n"
"    \n"
"    border-color: rgb(0, 0, 0);\n"
"    border-style: solid;\n"
"    padding: 4px;\n"
"    \n"
"    background-color: rgb(255, 255, 255);\n"
"}\n"
"")
        self.pushButton_5_4.setObjectName("pushButton_5_4")
        self.pushButton_4_4 = QtWidgets.QPushButton(Form)
        self.pushButton_4_4.setGeometry(QtCore.QRect(440, 350, 131, 71))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(8)
        self.pushButton_4_4.setFont(font)
        self.pushButton_4_4.setStyleSheet("QPushButton{\n"
"    \n"
"    \n"
"    color: rgb(0, 0, 0);\n"
"    border-width: 1px;\n"
"    border-radius: 6px;\n"
"    \n"
"    border-color: rgb(0, 0, 0);\n"
"    border-style: solid;\n"
"    padding: 4px;\n"
"    \n"
"    background-color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton::disabled\n"
"{\n"
"    color: rgb(0, 0, 0);\n"
"    border-width: 2px;\n"
"    border-radius: 6px;\n"
"    \n"
"    border-color: rgb(0, 0, 0);\n"
"    border-style: solid;\n"
"    padding: 4px;\n"
"    \n"
"    background-color: rgb(255, 255, 255);\n"
"}\n"
"")
        self.pushButton_4_4.setObjectName("pushButton_4_4")
        self.pushButton_2_4 = QtWidgets.QPushButton(Form)
        self.pushButton_2_4.setGeometry(QtCore.QRect(160, 350, 131, 71))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(8)
        self.pushButton_2_4.setFont(font)
        self.pushButton_2_4.setStyleSheet("QPushButton{\n"
"    \n"
"    \n"
"    color: rgb(0, 0, 0);\n"
"    border-width: 1px;\n"
"    border-radius: 6px;\n"
"    \n"
"    border-color: rgb(0, 0, 0);\n"
"    border-style: solid;\n"
"    padding: 4px;\n"
"    \n"
"    background-color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton::disabled\n"
"{\n"
"    color: rgb(0, 0, 0);\n"
"    border-width: 2px;\n"
"    border-radius: 6px;\n"
"    \n"
"    border-color: rgb(0, 0, 0);\n"
"    border-style: solid;\n"
"    padding: 4px;\n"
"    \n"
"    background-color: rgb(255, 255, 255);\n"
"}\n"
"")
        self.pushButton_2_4.setObjectName("pushButton_2_4")
        self.pushButton_1_4 = QtWidgets.QPushButton(Form)
        self.pushButton_1_4.setGeometry(QtCore.QRect(20, 350, 131, 71))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(8)
        self.pushButton_1_4.setFont(font)
        self.pushButton_1_4.setStyleSheet("QPushButton{\n"
"    \n"
"    \n"
"    color: rgb(0, 0, 0);\n"
"    border-width: 1px;\n"
"    border-radius: 6px;\n"
"    \n"
"    border-color: rgb(0, 0, 0);\n"
"    border-style: solid;\n"
"    padding: 4px;\n"
"    \n"
"    background-color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton::disabled\n"
"{\n"
"    color: rgb(0, 0, 0);\n"
"    border-width: 2px;\n"
"    border-radius: 6px;\n"
"    \n"
"    border-color: rgb(0, 0, 0);\n"
"    border-style: solid;\n"
"    padding: 4px;\n"
"    \n"
"    background-color: rgb(255, 255, 255);\n"
"}\n"
"")
        self.pushButton_1_4.setObjectName("pushButton_1_4")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Timetable Input Dialog"))
        self.pushButton_add.setText(_translate("Form", "更新"))
        self.label.setText(_translate("Form", "星期:"))
        self.label_2.setText(_translate("Form", "班级:"))
        self.label_5.setText(_translate("Form", "下课时间:"))
        self.label_3.setText(_translate("Form", "课程:"))
        self.label_4.setText(_translate("Form", "上课时间:"))
        self.comboBox_day.setItemText(0, _translate("Form", "星期一"))
        self.comboBox_day.setItemText(1, _translate("Form", "星期二"))
        self.comboBox_day.setItemText(2, _translate("Form", "星期三"))
        self.comboBox_day.setItemText(3, _translate("Form", "星期四"))
        self.comboBox_day.setItemText(4, _translate("Form", "星期五"))
        self.comboBox_day.setItemText(5, _translate("Form", "星期六"))
        self.comboBox_day.setItemText(6, _translate("Form", "星期天"))
        self.label_11.setText(_translate("Form", "序号:"))
        self.comboBox_no.setItemText(0, _translate("Form", "1"))
        self.comboBox_no.setItemText(1, _translate("Form", "2"))
        self.comboBox_no.setItemText(2, _translate("Form", "3"))
        self.comboBox_no.setItemText(3, _translate("Form", "4"))
        self.label_12.setText(_translate("Form", "学生ID"))
        self.label_10.setText(_translate("Form", "星期五"))
        self.label_9.setText(_translate("Form", "星期四"))
        self.label_8.setText(_translate("Form", "星期三"))
        self.label_7.setText(_translate("Form", "星期二"))
        self.label_6.setText(_translate("Form", "星期一"))
        self.pushButton_save.setText(_translate("Form", "保存"))
        self.pushButton_1_1.setText(_translate("Form", "计算机课程\n"
"A3-202\n"
"12:00\n"
"14:00"))
        self.pushButton_2_1.setText(_translate("Form", "计算机课程\n"
"A3-202\n"
"12:00\n"
"14:00"))
        self.pushButton_3_1.setText(_translate("Form", "计算机课程\n"
"A3-202\n"
"12:00\n"
"14:00"))
        self.pushButton_4_1.setText(_translate("Form", "计算机课程\n"
"A3-202\n"
"12:00\n"
"14:00"))
        self.pushButton_5_1.setText(_translate("Form", "计算机课程\n"
"A3-202\n"
"12:00\n"
"14:00"))
        self.pushButton_3_2.setText(_translate("Form", "计算机课程\n"
"A3-202\n"
"12:00\n"
"14:00"))
        self.pushButton_5_2.setText(_translate("Form", "计算机课程\n"
"A3-202\n"
"12:00\n"
"14:00"))
        self.pushButton_4_2.setText(_translate("Form", "计算机课程\n"
"A3-202\n"
"12:00\n"
"14:00"))
        self.pushButton_2_2.setText(_translate("Form", "计算机课程\n"
"A3-202\n"
"12:00\n"
"14:00"))
        self.pushButton_1_2.setText(_translate("Form", "计算机课程\n"
"A3-202\n"
"12:00\n"
"14:00"))
        self.pushButton_3_3.setText(_translate("Form", "计算机课程\n"
"A3-202\n"
"12:00\n"
"14:00"))
        self.pushButton_5_3.setText(_translate("Form", "计算机课程\n"
"A3-202\n"
"12:00\n"
"14:00"))
        self.pushButton_4_3.setText(_translate("Form", "计算机课程\n"
"A3-202\n"
"12:00\n"
"14:00"))
        self.pushButton_2_3.setText(_translate("Form", "计算机课程\n"
"A3-202\n"
"12:00\n"
"14:00"))
        self.pushButton_1_3.setText(_translate("Form", "计算机课程\n"
"A3-202\n"
"12:00\n"
"14:00"))
        self.pushButton_3_4.setText(_translate("Form", "计算机课程\n"
"A3-202\n"
"12:00\n"
"14:00"))
        self.pushButton_5_4.setText(_translate("Form", "计算机课程\n"
"A3-202\n"
"12:00\n"
"14:00"))
        self.pushButton_4_4.setText(_translate("Form", "计算机课程\n"
"A3-202\n"
"12:00\n"
"14:00"))
        self.pushButton_2_4.setText(_translate("Form", "计算机课程\n"
"A3-202\n"
"12:00\n"
"14:00"))
        self.pushButton_1_4.setText(_translate("Form", "计算机课程\n"
"A3-202\n"
"12:00\n"
"14:00"))
import resource_rc
