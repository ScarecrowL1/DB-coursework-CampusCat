from threading import Thread

from PyQt5.QtCore import *
from PyQt5.QtWidgets import QMainWindow, QWidget, QMessageBox

from admin import admin
from loginWindow import Ui_Login

from register import register

from database import dataBase

import sys

from user import user


class login(Ui_Login, QMainWindow):
    sig = pyqtSignal(str)

    def __init__(self):
        super(login, self).__init__()

        self.setupUi(self)
        self.setWindowTitle("校园猫管理平台")
        self.activateButton()
        self.sig.connect(self.handler)

        self.registerWindow = None
        self.userState = None
        self.nextWindow = None

    def activateButton(self):
        self.regButton.clicked.connect(self.register_)
        self.loginButton.clicked.connect(self.login_)

    def register_(self):
        self.registerWindow = register()
        self.registerWindow.show()

    def login_(self):
        username = self.usernameEdit.text()
        passwd = self.passwordEdit.text()
        if '' in [username, passwd]:
            QMessageBox.information(self, '警告', '请检查是否填写完整', QMessageBox.Ok)
            return
        thread = Thread(target=self.loginCheck, args=(username, passwd))
        thread.start()

    def loginCheck(self, username, passwd):
        database = dataBase()
        cnt, res = database.select('userinfo', 'userName', username)
        # 找不到用户
        if cnt == 0:
            self.sig.emit('notfound')
            return
        # 找到用户
        else:
            # 获得当前用户的权限和正确密码
            self.userState = res[0][3]
            correctPwd = res[0][2]

        if passwd != correctPwd:
            self.sig.emit('incorrect')
            return

        self.sig.emit('pass')

    def handler(self, argv):
        if argv == 'notfound':
            QMessageBox.warning(self, '警告', '用户名不存在！', QMessageBox.Ok)
            return
        if argv == 'incorrect':
            QMessageBox.warning(self, '警告', '用户名或密码错误', QMessageBox.Ok)
            return
        if argv == 'pass':
            username = self.usernameEdit.text()
            if self.userState == 1:
                QMessageBox.information(self, '欢迎使用', '管理员用户 '+username+' 你好', QMessageBox.Ok)
                self.nextWindow = admin(username=username)
            else:
                QMessageBox.information(self, '欢迎使用', '普通用户 '+username+' 你好', QMessageBox.Ok)
                self.nextWindow = user(username=username)

            self.nextWindow.show()
            self.close()
