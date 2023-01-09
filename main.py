# 开发第一个基于PyQt5的桌面应用

import sys

from PyQt5.QtWidgets import QApplication,QMainWindow

from login import login

if __name__ == '__main__':
    app = QApplication(sys.argv)

    mainWindow = login()
    mainWindow.show()
    # 进入程序的主循环，并通过exit函数确保主循环安全结束(该释放资源的一定要释放)
    sys.exit(app.exec_())
