#-*- coding:utf-8 -*-
from view.mainwindow import*
from control.faceRegister import FaceRegister
from control.faceCheckin import FaceCheckin
from control.faceRecord import FaceRecord
from control.checkinRecord import CheckInRecord
from PyQt5.QtWidgets import QMainWindow
import model.configuration
from model.recognizer import recognizer
class MyWindow(QMainWindow, Ui_MainWindow):

    def __init__(self, parent=None):
        super(MyWindow, self).__init__(parent)
        self.setupUi(self)
        #connect the button and function
        self.pushButton_register.clicked.connect(self.face_register)
        self.pushButton_checkin.clicked.connect(self.check_in)
        self.pushButton_face_record.clicked.connect(self.face_record)
        self.pushButton_checkin_record.clicked.connect(self.check_in_record)
        self.pushButton_about.clicked.connect(self.about)
        self.pushButton_exit.clicked.connect(self.exit)
        self.re = recognizer(model.configuration.PREDICTOR_PATH, model.configuration.FACE_REC_MODEL_PATH)
    #face register
    def face_register(self):
        self.close_logo()
        for i in range(self.verticalLayout.count()):
            self.verticalLayout.itemAt(i).widget().close_all()
        self.verticalLayout.addWidget(FaceRegister(self.re))
    #check-in
    def check_in(self):
        self.close_logo()
        for i in range(self.verticalLayout.count()):
            self.verticalLayout.itemAt(i).widget().close_all()
        self.verticalLayout.addWidget(FaceCheckin(self.re))
    #face record
    def face_record(self):
        self.close_logo()
        for i in range(self.verticalLayout.count()):
            self.verticalLayout.itemAt(i).widget().close_all()
        self.verticalLayout.addWidget(FaceRecord())
    #check in record
    def check_in_record(self):
        self.close_logo()
        for i in range(self.verticalLayout.count()):
            self.verticalLayout.itemAt(i).widget().close_all()
        self.verticalLayout.addWidget(CheckInRecord())
    #about
    def about(self):
        for i in range(self.verticalLayout.count()):
            self.verticalLayout.itemAt(i).widget().close_all()
        self.label_logo.setVisible(True)
        self.label_author.setVisible(True)
    #exit
    def exit(self):
        self.close()
    #close the welcome logo
    def close_logo(self):
        self.label_logo.setVisible(False)
        self.label_author.setVisible(False)

