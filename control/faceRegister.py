from view.faceregister import*
from PyQt5.QtWidgets import QWidget,QMessageBox
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from model.connectsqlite import ConnectSqlite
import model.configuration
from control.timeTable import TimeTable
from datetime import datetime
import cv2

class FaceRegister(QWidget, Ui_FaceRegisterForm):

    def __init__(self, re, parent=None):
        super(FaceRegister, self).__init__(parent)
        self.setupUi(self)

        self.CAM_OPEN_FLAG = False
        #recognize model
        self.re = re
        #sqlite3 connect
        self.dbcon = ConnectSqlite(model.configuration.DATABASE_PATH)
        #connect the pushbutton and function
        self.pushButton_open.clicked.connect(self.open_cam)
        self.pushButton_stop.clicked.connect(self.stop_cam)
        self.pushButton_take_photo.clicked.connect(self.take_photo)
        self.pushButton_register.clicked.connect(self.register)
        self.pushButton_add_timetable.clicked.connect(self.add_timetable)
        #face feature
        self.face_fingerprint = None
        #timetable
        self.timetable = None
        #face_img
        self.frame_photo = None
        # none timetable pic
        self.timetable_none = "border-image: url(:/icon/pic/na.png);"
        self.timetable_yes = "border-image: url(:/icon/pic/yes.png);"
        self.label.setStyleSheet(self.timetable_none)

    #add the timetable
    def add_timetable(self):
        sid = self.lineEdit_sno.text()
        if sid == '':
            # show messegebox
            reply = QMessageBox.warning(self, 'Error', 'Please input the name and ID firstly!',
                                        QMessageBox.Yes, QMessageBox.Yes)
        else:
            #timetable dialog
            self.timetable_dialog = TimeTable(sid)
            self.timetable_dialog.show()
            self.timetable_dialog.timeTableSignal.connect(self.getTimeTableSignal)
    #get the timetable from dialog
    def getTimeTableSignal(self,dict_receive):
        print(dict_receive)
        self.timetable = dict_receive
        self.label.setStyleSheet(self.timetable_yes)
    # open the camera
    def open_cam(self):
        if not self.CAM_OPEN_FLAG:
            self.timer_camera = QTimer()  # 定义定时器
            #opencv read the camera
            self.cap = cv2.VideoCapture(0)
            self.cap.set(3,640)
            self.cap.set(4,480)
            #create the QTimer to show the frame
            self.timer_camera.start(10)
            self.timer_camera.timeout.connect(self.show_frame)
            self.CAM_OPEN_FLAG = True
        else:
            # show messegebox
            reply = QMessageBox.warning(self, 'Error', 'The camera is opened!',
                                        QMessageBox.Yes, QMessageBox.Yes)
    # stop the camera
    def stop_cam(self):
        if self.CAM_OPEN_FLAG:
            # stop the QTmer
            self.timer_camera.stop()
            #clear the label
            self.label_frame.clear()
            #release the camera
            self.cap.release()
            #turn off the flag
            self.CAM_OPEN_FLAG = False
        else:
            # show messegebox
            reply = QMessageBox.warning(self, 'Error', 'The camera is not opened!',
                                        QMessageBox.Yes, QMessageBox.Yes)
    #show the frame on the label
    def show_frame(self):
        if (self.cap.isOpened()):
            ret, self.frame = self.cap.read()
            if ret:
                self.show_label(self.frame,self.label_frame)
    # take the photo
    def take_photo(self):
        print("take photo")
        # face feature
        self.face_fingerprint = None
        # timetable
        self.timetable = None
        # face_img
        self.frame_photo = None
        # 清空人脸照片和人脸特征点照片
        self.label_face.setPixmap(QPixmap(""))
        self.label_face_feature.setPixmap(QPixmap(""))
        if self.CAM_OPEN_FLAG:
            code, self.frame_photo, frame_feature, self.face_fingerprint = self.re.take_photo(self.frame)
            print(code)
            # if there is no faces
            if code == 0:
                # 将拍摄到的照片显示在人脸照片label上
                self.show_label(self.frame_photo,self.label_face)
                # 显示对话框，未检测到人脸
                reply = QMessageBox.warning(self, 'Error', 'No face detected!',
                                            QMessageBox.Yes, QMessageBox.Yes)
            # if there is one
            elif code == 1:
                self.show_label(self.frame_photo, self.label_face)
                self.show_label(frame_feature, self.label_face_feature)
                print(list(self.face_fingerprint))
            #if there is more than one face
            else:
                # 将拍摄到的照片显示在人脸照片label上
                self.show_label(self.frame_photo, self.label_face)
                # 显示对话框，未检测到人脸
                reply = QMessageBox.warning(self, 'Error', 'More than one face detected',
                                            QMessageBox.Yes, QMessageBox.Yes)
        else:
            # show messegebox
            reply = QMessageBox.warning(self, 'Error', 'Please open the camera firstly!',
                                        QMessageBox.Yes, QMessageBox.Yes)
    #register
    def register(self):
        print("register")
        #name = 'Tommy'
        name = self.lineEdit_name.text()
        student_id = self.lineEdit_sno.text()

        if name == '' or student_id == '':
            # show messegebox
            reply = QMessageBox.warning(self, 'Error', 'Please input the name and ID firstly!',
                                        QMessageBox.Yes, QMessageBox.Yes)
        else:
            if self.face_fingerprint == None:
                reply = QMessageBox.warning(self, 'Error', 'No face feature detected!',
                                            QMessageBox.Yes, QMessageBox.Yes)
            else:
                # id = '123456'
                change_time = datetime.now()
                timetable = str(self.timetable)
                face_data = str(self.face_fingerprint)
                face_img = self.frame_photo
                print(face_img.shape)
                insert_list = [name, timetable, face_data, face_img, change_time, student_id]

                # select all the student_id
                all_sid = self.dbcon.return_all_sid()
                print(type(student_id),type(all_sid[1]))
                if student_id not in all_sid:
                    if self.timetable != None:
                        save_result = self.dbcon.insert_facedata_table(insert_list)
                        if save_result == 0:
                            # show messegebox
                            reply = QMessageBox.information(self, 'Success', 'Your face feature and timetable has saved!',
                                                        QMessageBox.Yes, QMessageBox.Yes)

                            #clear the window
                            # face feature
                            self.face_fingerprint = None
                            # timetable
                            self.timetable = None
                            # face_img
                            self.frame_photo = None
                            # 清空人脸照片和人脸特征点照片
                            self.label_face.setPixmap(QPixmap(""))
                            self.label_face_feature.setPixmap(QPixmap(""))
                            self.label.setStyleSheet(self.timetable_none)

                            self.lineEdit_sno.setText("")
                            self.lineEdit_name.setText("")

                        else:
                            # show messegebox
                            reply = QMessageBox.warning(self, 'Error', 'Write to the database Failed!\n' + save_result,
                                                        QMessageBox.Yes, QMessageBox.Yes)

                    else:
                        # show messegebox
                        reply = QMessageBox.warning(self, 'Error', 'Please create your timetable!',
                                                    QMessageBox.Yes, QMessageBox.Yes)
                else:
                    # show messegebox
                    reply = QMessageBox.warning(self, 'Error', 'Your ID have registered!',
                                                QMessageBox.Yes, QMessageBox.Yes)
    #show the label on the frame
    def show_label(self,frame,label):
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)  # 转换为RGB图像
        height, width, bytesPerComponent = frame.shape
        bytesPerLine = bytesPerComponent * width
        q_image = QImage(frame.data, width, height, bytesPerLine,  # 将图片转换为QImage格式
                         QImage.Format_RGB888)
        label.setPixmap(QPixmap.fromImage(q_image))
        label.setScaledContents(True)  # 拉伸铺满label
    #close all
    def close_all(self):
        if self.CAM_OPEN_FLAG:
            # stop the QTmer
            self.timer_camera.stop()
            self.cap.release()
        self.close()

