from PyQt5.QtWidgets import *

from registerWindow import Ui_Register
from database import dataBase


class register(Ui_Register, QMainWindow):
    def __init__(self):
        super(register, self).__init__()
        self.setupUi(self)
        self.noButton.clicked.connect(self.close)
        self.yesButton.clicked.connect(self.register_)

    def register_(self):
        username = self.usernameEdit.text()
        passwd = self.passwdEdit.text()
        conpasswd = self.conpwEdit.text()  # 确认密码

        # 输入合法性检测
        if '' in [username, passwd, conpasswd]:
            QMessageBox.information(self, "警告", "请检查是否填写完整", QMessageBox.Ok)
            return
        if len(username)>18  or len(passwd)>18 or len(passwd) < 8:
            QMessageBox.information(self, "警告", "用户名或密码格式错误（其中密码总长度不能超过18位,密码要大于8位）", QMessageBox.Ok)
            return
        if passwd != conpasswd :
            QMessageBox.information(self, "警告", "两次输入密码不一致，请重新输入", QMessageBox.Ok)
            return

        # 最后和数据库对比，如果用户名不重复，即可注册
        database = dataBase()
        res = database.select("userinfo", "userName", username)
        if res[0] > 0: # res[0]是返回项目个数
            QMessageBox.information(self, "警告", "用户名已存在", QMessageBox.Ok)
            return
        userRegInfo = [username, passwd]
        database.addUser(userRegInfo)
        database.update()
        QMessageBox.information(self, '注册', '注册成功', QMessageBox.Ok)
        self.close()
