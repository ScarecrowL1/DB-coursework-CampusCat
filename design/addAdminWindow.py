# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'addAdminWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_addAdminWindow(object):
    def setupUi(self, addAdminWindow):
        addAdminWindow.setObjectName("addAdminWindow")
        addAdminWindow.resize(369, 408)
        self.gridLayoutWidget = QtWidgets.QWidget(addAdminWindow)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(30, 10, 311, 281))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.conpwEdit = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.conpwEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.conpwEdit.setObjectName("conpwEdit")
        self.gridLayout.addWidget(self.conpwEdit, 2, 1, 1, 1)
        self.usernameEdit = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.usernameEdit.setObjectName("usernameEdit")
        self.gridLayout.addWidget(self.usernameEdit, 0, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.passwdEdit = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.passwdEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.passwdEdit.setObjectName("passwdEdit")
        self.gridLayout.addWidget(self.passwdEdit, 1, 1, 1, 1)
        self.gridLayoutWidget_2 = QtWidgets.QWidget(addAdminWindow)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(50, 260, 261, 141))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.yesButton = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.yesButton.setObjectName("yesButton")
        self.gridLayout_2.addWidget(self.yesButton, 0, 1, 1, 1)
        self.noButton = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.noButton.setObjectName("noButton")
        self.gridLayout_2.addWidget(self.noButton, 0, 0, 1, 1)

        self.retranslateUi(addAdminWindow)
        QtCore.QMetaObject.connectSlotsByName(addAdminWindow)

    def retranslateUi(self, addAdminWindow):
        _translate = QtCore.QCoreApplication.translate
        addAdminWindow.setWindowTitle(_translate("addAdminWindow", "Form"))
        self.label_3.setText(_translate("addAdminWindow", "您的密码:"))
        self.label.setText(_translate("addAdminWindow", "新增管理员用户名"))
        self.label_2.setText(_translate("addAdminWindow", "确认新增管理员用户名"))
        self.yesButton.setText(_translate("addAdminWindow", "确认"))
        self.noButton.setText(_translate("addAdminWindow", "取消"))
