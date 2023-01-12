from PyQt5.QtWidgets import *
from addAdminWindow import Ui_addAdminWindow
from database import dataBase


class newAdmin(Ui_addAdminWindow, QWidget):
    def __init__(self):
        super(newAdmin, self).__init__()
        self.setupUi(self)
        self.setWindowTitle('新增管理员')
        self.noButton.clicked.connect(self.close)
        self.yesButton.clicked.connect(self.confirmAdmin)

    def confirmAdmin(self):
        newAdminName = self.newAdminEdit.text()
        conName = self.conNameEdit.text()
        passwd = self.passwdEdit.text()

        if '' in [newAdminName, conName, passwd]:
            QMessageBox.information(self, "警告", "请检查是否填写完整", QMessageBox.Ok)
            return
        if len(newAdminName) > 18:
            QMessageBox.information(self, "警告", "用户名格式错误", QMessageBox.Ok)
            return
        if newAdminName != conName:
            QMessageBox.information(self, "警告", "两次输入用户名不一致，请重新输入", QMessageBox.Ok)
            return

        database = dataBase()
        res = database.select("userinfo", "userName", newAdminName)
        if res[0] == 0:  # res[0]存储着返回项目个数
            QMessageBox.information(self, "警告", "该用户名不存在，请检查", QMessageBox.Ok)
            return

        database.addAdmin(newAdminName)
        database.update()
        QMessageBox.information(self, '提示', '该用户已被设置为管理员', QMessageBox.Ok)
        self.close()
