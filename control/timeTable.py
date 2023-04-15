from view.timetableui import*
from model.createTimetable import comepare_time
from PyQt5.QtWidgets import QWidget,QMessageBox

from PyQt5.QtCore import pyqtSignal,QTime

class TimeTable(QWidget, Ui_Form):
    # the signal and slot to connect the Register Window
    #注意在pyqt里不可以将信号定义为类的对象属性只可以定义成类属性
    timeTableSignal = pyqtSignal(object)
    def __init__(self, student_id,parent=None):
        super(TimeTable, self).__init__(parent)
        self.setupUi(self)
        #connect the button and function
        self.pushButton_add.clicked.connect(self.add)
        self.pushButton_save.clicked.connect(self.save)
        for i in range(1, 6):
            for j in range(1, 5):
                exec("self.pushButton_{}_{}.clicked.connect(self.select_table)".format(i, j))

        self.comboBox_no.currentIndexChanged.connect(self.combobox_change)
        self.comboBox_day.currentIndexChanged.connect(self.combobox_change)
        #dict of timetable
        self.tableDict = {"Monday":[[],[],[],[]],
                                    "Tuesday":[[],[],[],[]],
                                    "Wednesday":[[],[],[],[]],
                                    "Thursday": [[], [], [], []],
                                    "Friday": [[], [], [], []]}
        # the table stylesheet
        self.unselect_style ="\"color: rgb(0, 0, 0);border-width: 1px;border-radius: 6px;border-color: rgb(0, 0, 0);border-style: solid;padding: 4px;\""

        self.select_style = "\"color: rgb(0, 0, 0);border-width: 2px;border-radius: 6px;border-color: rgb(0, 0, 0);border-style: solid;padding: 4px;\""
        #show all course on the table
        self.show_on_table()
        #set the table unselet
        self.set_unselect_all()
        #current row and index
        self.current_table = [0,0]
       #Enabled the student ID
        #
        # 自定义信号

        self.lineEdit_sid.setEnabled(False)
        self.student_id = student_id

        self.lineEdit_sid.setText(self.student_id)
        self.timeEdit_start.setDisplayFormat("HH:mm")
        self.timeEdit_end.setDisplayFormat("HH:mm")
    def add(self):
        day = self.comboBox_day.currentText()
        course = self.lineEdit_course.text()
        room = self.lineEdit_classroom.text()
        start_time = self.timeEdit_start.text()
        end_time = self.timeEdit_end.text()
        print(start_time)
        if course == '' or room == '':
            # show messegebox
            reply = QMessageBox.warning(self, 'Error', 'Please input the course and classroom!',
                                        QMessageBox.Yes, QMessageBox.Yes)
        else:
            compare = comepare_time(start_time,end_time)
            if compare == 1:
                print("add")
                current_day = list(self.tableDict.keys())[self.current_table[0] - 1]
                current_index = self.current_table[1] -1
                self.tableDict[current_day][current_index] = [course,room,start_time,end_time]
                self.show_on_table()


            else:
                # show messegebox
                reply = QMessageBox.warning(self, 'Error', 'Please check the start and end time!',
                                            QMessageBox.Yes, QMessageBox.Yes)

    def save(self):
        if self.tableDict == {"Monday":[[],[],[],[]],
                                    "Tuesday":[[],[],[],[]],
                                    "Wednesday":[[],[],[],[]],
                                    "Thursday": [[], [], [], []],
                                    "Friday": [[], [], [], []]}:
            # show messegebox
            reply = QMessageBox.warning(self, 'Error', 'You must input at least one record!',
                                        QMessageBox.Yes, QMessageBox.Yes)
        else:
            print("save")
            self.timeTableSignal.emit(self.tableDict)  # 发射信号
            self.close()

    def show_on_table(self):
        for i,day in enumerate(self.tableDict.keys()):
            print(i, day)
            for j,course in enumerate(self.tableDict[day]):
                print(j, course)
                if course != []:
                    t = '\n'.join(course)
                    exec("self.pushButton_{}_{}.setText(t)".format(i+1,j+1))
                else:
                    exec("self.pushButton_{}_{}.setText('')".format(i+1,j+1))

    def select_table(self):
        sender = self.sender()
        button_object = sender.objectName().split("_")
        self.comboBox_day.setCurrentIndex(int(button_object[1]) - 1)
        self.comboBox_no.setCurrentIndex(int(button_object[2]) - 1)
        self.current_table = [int(button_object[1]),int(button_object[2])]
        self.set_unselect_all()

        current_record = list(self.tableDict.values())[int(button_object[1]) - 1][int(button_object[2]) - 1]
        if current_record == []:
            self.lineEdit_classroom.setText("")
            self.lineEdit_course.setText("")
            start = QTime.fromString("00:00")
            end = QTime.fromString("00:00")
            self.timeEdit_start.setTime(start)
            self.timeEdit_end.setTime(end)

        else:
            self.lineEdit_classroom.setText(current_record[1])
            self.lineEdit_course.setText(current_record[0])
            start_time1 = int(current_record[2].split(':')[0])
            start_time2 = int(current_record[2].split(':')[1])
            start_time1_format = str('{:0>2d}'.format(start_time1))
            start_time2_format = str('{:0>2d}'.format(start_time2))
            start = QTime.fromString(start_time1_format + ':' + start_time2_format)
            end_time1 = int(current_record[3].split(':')[0])
            end_time2 = int(current_record[3].split(':')[1])
            end_time1_format = str('{:0>2d}'.format(end_time1))
            end_time2_format = str('{:0>2d}'.format(end_time2))
            end = QTime.fromString(end_time1_format + ':' + end_time2_format)
            self.timeEdit_start.setTime(start)
            self.timeEdit_end.setTime(end)

        exec("self." + sender.objectName() + ".setStyleSheet(" + self.select_style + ")")

    def combobox_change(self):
        combo_day = self.comboBox_day.currentIndex() + 1
        combo_no = self.comboBox_no.currentIndex() + 1
        self.current_table = [combo_day, combo_no]
        self.set_unselect_all()
        exec("self.pushButton_{}_{}".format(combo_day,combo_no) + ".setStyleSheet(" + self.select_style + ")")

    def set_unselect_all(self):
        for i in range(1,6):
            for j in range(1,5):
                exec("self.pushButton_{}_{}.setStyleSheet({})".format(i,j,self.unselect_style))

