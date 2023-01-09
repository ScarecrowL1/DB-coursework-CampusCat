from PyQt5.QtWidgets import QMainWindow, QWidget

from loginWindow import Ui_Login

from register import register

import sys


class login(Ui_Login, QMainWindow):
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
        pass