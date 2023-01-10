from threading import Thread

from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QMainWindow, QWidget, QMessageBox

from loginWindow import Ui_Login

from register import register

import sys


class login(Ui_Login, QMainWindow):
    signal = pyqtSignal(int)

    def __init__(self):
        super(login, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("校园猫管理平台")
        self.activateButton()
        self.registerWindow = None

    def activateButton(self):
        self.regButton.clicked.connect(self.register_)
        self.loginButton.clicked.connect(self.login_)

    def register_(self):
        self.registerWindow = register()
        self.registerWindow.show()

    def login_(self):
        username = self.lineEdit_user_name.text()
        passwd = self.lineEdit_password.text()
        if '' in [username, passwd]:
            QMessageBox.information(self, '警告', '请检查是否填写完整', QMessageBox.Ok)
            return
        thread = Thread(target=self.loginCheck, args=(username, passwd))
        thread.start()

    def loginCheck(self, username, passwd):
        pass
