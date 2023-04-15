from PyQt5.QtWidgets import QApplication
from PyQt5 import QtCore
from control.mainWindow import MyWindow
import sys

# PyQt使用高分辨率
# QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)

# 主函数
if __name__ == '__main__':
    app = QApplication(sys.argv)
    # 实例化主界面
    myWin = MyWindow()
    # 显示主界面
    myWin.show()
    sys.exit(app.exec_())
