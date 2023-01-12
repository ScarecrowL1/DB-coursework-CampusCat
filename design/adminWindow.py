# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'adminWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_adminWindow(object):
    def setupUi(self, adminWindow):
        adminWindow.setObjectName("adminWindow")
        adminWindow.resize(1255, 663)
        self.centralwidget = QtWidgets.QWidget(adminWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(260, 10, 731, 81))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.feedBtn = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.feedBtn.setObjectName("feedBtn")
        self.gridLayout.addWidget(self.feedBtn, 0, 2, 1, 1)
        self.catinfoBtn = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.catinfoBtn.setObjectName("catinfoBtn")
        self.gridLayout.addWidget(self.catinfoBtn, 0, 0, 1, 1)
        self.witnessBtn = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.witnessBtn.setObjectName("witnessBtn")
        self.gridLayout.addWidget(self.witnessBtn, 0, 1, 1, 1)
        self.newAdminBtn = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.newAdminBtn.setObjectName("newAdminBtn")
        self.gridLayout.addWidget(self.newAdminBtn, 0, 3, 1, 1)
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setGeometry(QtCore.QRect(50, 100, 1171, 561))
        self.stackedWidget.setObjectName("stackedWidget")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.catTabel = QtWidgets.QTableWidget(self.page)
        self.catTabel.setGeometry(QtCore.QRect(270, 0, 881, 551))
        self.catTabel.setColumnCount(7)
        self.catTabel.setObjectName("catTabel")
        self.catTabel.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.catTabel.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.catTabel.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.catTabel.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.catTabel.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.catTabel.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.catTabel.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.catTabel.setHorizontalHeaderItem(6, item)
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.page)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(30, 0, 201, 51))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.addCatNameEdit = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.addCatNameEdit.setObjectName("addCatNameEdit")
        self.horizontalLayout.addWidget(self.addCatNameEdit)
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.page)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(30, 60, 201, 51))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.addCatGenderBox = QtWidgets.QComboBox(self.horizontalLayoutWidget_2)
        self.addCatGenderBox.setObjectName("addCatGenderBox")
        self.addCatGenderBox.addItem("")
        self.addCatGenderBox.addItem("")
        self.horizontalLayout_2.addWidget(self.addCatGenderBox)
        self.horizontalLayoutWidget_3 = QtWidgets.QWidget(self.page)
        self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(30, 120, 201, 51))
        self.horizontalLayoutWidget_3.setObjectName("horizontalLayoutWidget_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_3 = QtWidgets.QLabel(self.horizontalLayoutWidget_3)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_3.addWidget(self.label_3)
        self.AddCatRaceEdit = QtWidgets.QLineEdit(self.horizontalLayoutWidget_3)
        self.AddCatRaceEdit.setObjectName("AddCatRaceEdit")
        self.horizontalLayout_3.addWidget(self.AddCatRaceEdit)
        self.label_4 = QtWidgets.QLabel(self.page)
        self.label_4.setGeometry(QtCore.QRect(0, 530, 151, 21))
        self.label_4.setObjectName("label_4")
        self.horizontalLayoutWidget_4 = QtWidgets.QWidget(self.page)
        self.horizontalLayoutWidget_4.setGeometry(QtCore.QRect(30, 210, 201, 51))
        self.horizontalLayoutWidget_4.setObjectName("horizontalLayoutWidget_4")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_4)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.addLocBox = QtWidgets.QComboBox(self.horizontalLayoutWidget_4)
        self.addLocBox.setObjectName("addLocBox")
        self.horizontalLayout_4.addWidget(self.addLocBox)
        self.label_5 = QtWidgets.QLabel(self.page)
        self.label_5.setGeometry(QtCore.QRect(30, 190, 91, 16))
        self.label_5.setObjectName("label_5")
        self.horizontalLayoutWidget_5 = QtWidgets.QWidget(self.page)
        self.horizontalLayoutWidget_5.setGeometry(QtCore.QRect(30, 270, 201, 41))
        self.horizontalLayoutWidget_5.setObjectName("horizontalLayoutWidget_5")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_5)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_6 = QtWidgets.QLabel(self.horizontalLayoutWidget_5)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_5.addWidget(self.label_6)
        self.addCatVacBox = QtWidgets.QComboBox(self.horizontalLayoutWidget_5)
        self.addCatVacBox.setObjectName("addCatVacBox")
        self.horizontalLayout_5.addWidget(self.addCatVacBox)
        self.label_7 = QtWidgets.QLabel(self.page)
        self.label_7.setGeometry(QtCore.QRect(30, 320, 54, 12))
        self.label_7.setObjectName("label_7")
        self.addOtherEdit = QtWidgets.QTextEdit(self.page)
        self.addOtherEdit.setGeometry(QtCore.QRect(30, 340, 201, 81))
        self.addOtherEdit.setObjectName("addOtherEdit")
        self.addCatButton = QtWidgets.QPushButton(self.page)
        self.addCatButton.setGeometry(QtCore.QRect(60, 440, 141, 51))
        self.addCatButton.setObjectName("addCatButton")
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.witnessTable = QtWidgets.QTableWidget(self.page_2)
        self.witnessTable.setGeometry(QtCore.QRect(380, 0, 791, 541))
        self.witnessTable.setColumnCount(5)
        self.witnessTable.setObjectName("witnessTable")
        self.witnessTable.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.witnessTable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.witnessTable.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.witnessTable.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.witnessTable.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.witnessTable.setHorizontalHeaderItem(4, item)
        self.label_8 = QtWidgets.QLabel(self.page_2)
        self.label_8.setGeometry(QtCore.QRect(80, 110, 54, 12))
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.page_2)
        self.label_9.setGeometry(QtCore.QRect(80, 220, 54, 12))
        self.label_9.setObjectName("label_9")
        self.witCatNameBox = QtWidgets.QComboBox(self.page_2)
        self.witCatNameBox.setGeometry(QtCore.QRect(150, 210, 151, 31))
        self.witCatNameBox.setObjectName("witCatNameBox")
        self.addWitButton = QtWidgets.QPushButton(self.page_2)
        self.addWitButton.setGeometry(QtCore.QRect(180, 310, 75, 23))
        self.addWitButton.setObjectName("addWitButton")
        self.witLocBox = QtWidgets.QComboBox(self.page_2)
        self.witLocBox.setGeometry(QtCore.QRect(150, 100, 151, 31))
        self.witLocBox.setObjectName("witLocBox")
        self.stackedWidget.addWidget(self.page_2)
        self.page_3 = QtWidgets.QWidget()
        self.page_3.setObjectName("page_3")
        self.feedTable = QtWidgets.QTableWidget(self.page_3)
        self.feedTable.setGeometry(QtCore.QRect(380, 0, 771, 521))
        self.feedTable.setColumnCount(6)
        self.feedTable.setObjectName("feedTable")
        self.feedTable.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.feedTable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.feedTable.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.feedTable.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.feedTable.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.feedTable.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.feedTable.setHorizontalHeaderItem(5, item)
        self.label_10 = QtWidgets.QLabel(self.page_3)
        self.label_10.setGeometry(QtCore.QRect(60, 140, 61, 16))
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.page_3)
        self.label_11.setGeometry(QtCore.QRect(60, 10, 301, 51))
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.page_3)
        self.label_12.setGeometry(QtCore.QRect(80, 70, 221, 16))
        self.label_12.setObjectName("label_12")
        self.feedCatBox = QtWidgets.QComboBox(self.page_3)
        self.feedCatBox.setGeometry(QtCore.QRect(130, 130, 171, 41))
        self.feedCatBox.setObjectName("feedCatBox")
        self.label_13 = QtWidgets.QLabel(self.page_3)
        self.label_13.setGeometry(QtCore.QRect(60, 240, 54, 12))
        self.label_13.setObjectName("label_13")
        self.feedFoodBox = QtWidgets.QComboBox(self.page_3)
        self.feedFoodBox.setGeometry(QtCore.QRect(130, 230, 171, 41))
        self.feedFoodBox.setObjectName("feedFoodBox")
        self.label_14 = QtWidgets.QLabel(self.page_3)
        self.label_14.setGeometry(QtCore.QRect(60, 330, 61, 16))
        self.label_14.setObjectName("label_14")
        self.addFeedBtn = QtWidgets.QPushButton(self.page_3)
        self.addFeedBtn.setGeometry(QtCore.QRect(160, 430, 75, 23))
        self.addFeedBtn.setObjectName("addFeedBtn")
        self.feedLocBox = QtWidgets.QComboBox(self.page_3)
        self.feedLocBox.setGeometry(QtCore.QRect(130, 319, 171, 41))
        self.feedLocBox.setObjectName("feedLocBox")
        self.stackedWidget.addWidget(self.page_3)
        adminWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(adminWindow)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(adminWindow)

    def retranslateUi(self, adminWindow):
        _translate = QtCore.QCoreApplication.translate
        adminWindow.setWindowTitle(_translate("adminWindow", "MainWindow"))
        self.feedBtn.setText(_translate("adminWindow", "记录我的投喂"))
        self.catinfoBtn.setText(_translate("adminWindow", "猫猫花名册"))
        self.witnessBtn.setText(_translate("adminWindow", "猫猫位置打卡"))
        self.newAdminBtn.setText(_translate("adminWindow", "新增管理员"))
        self.catTabel.setSortingEnabled(False)
        item = self.catTabel.horizontalHeaderItem(0)
        item.setText(_translate("adminWindow", "猫猫编号"))
        item = self.catTabel.horizontalHeaderItem(1)
        item.setText(_translate("adminWindow", "猫猫名字"))
        item = self.catTabel.horizontalHeaderItem(2)
        item.setText(_translate("adminWindow", "性别"))
        item = self.catTabel.horizontalHeaderItem(3)
        item.setText(_translate("adminWindow", "品种"))
        item = self.catTabel.horizontalHeaderItem(4)
        item.setText(_translate("adminWindow", "常出现地点"))
        item = self.catTabel.horizontalHeaderItem(5)
        item.setText(_translate("adminWindow", "疫苗状态"))
        item = self.catTabel.horizontalHeaderItem(6)
        item.setText(_translate("adminWindow", "备注"))
        self.label.setText(_translate("adminWindow", "猫名："))
        self.label_2.setText(_translate("adminWindow", "性别："))
        self.addCatGenderBox.setItemText(0, _translate("adminWindow", "公"))
        self.addCatGenderBox.setItemText(1, _translate("adminWindow", "母"))
        self.label_3.setText(_translate("adminWindow", "品种："))
        self.label_4.setText(_translate("adminWindow", "作为管理员，请细心填写~"))
        self.label_5.setText(_translate("adminWindow", "常出现地点："))
        self.label_6.setText(_translate("adminWindow", "疫苗状态："))
        self.label_7.setText(_translate("adminWindow", "备注："))
        self.addCatButton.setText(_translate("adminWindow", "新增猫猫"))
        item = self.witnessTable.horizontalHeaderItem(0)
        item.setText(_translate("adminWindow", "打卡编号"))
        item = self.witnessTable.horizontalHeaderItem(1)
        item.setText(_translate("adminWindow", "猫猫名字"))
        item = self.witnessTable.horizontalHeaderItem(2)
        item.setText(_translate("adminWindow", "地点"))
        item = self.witnessTable.horizontalHeaderItem(3)
        item.setText(_translate("adminWindow", "打卡用户"))
        item = self.witnessTable.horizontalHeaderItem(4)
        item.setText(_translate("adminWindow", "打卡时间"))
        self.label_8.setText(_translate("adminWindow", "打卡地点："))
        self.label_9.setText(_translate("adminWindow", "猫猫名字："))
        self.addWitButton.setText(_translate("adminWindow", "提交"))
        item = self.feedTable.horizontalHeaderItem(0)
        item.setText(_translate("adminWindow", "投喂编号"))
        item = self.feedTable.horizontalHeaderItem(1)
        item.setText(_translate("adminWindow", "猫猫名字"))
        item = self.feedTable.horizontalHeaderItem(2)
        item.setText(_translate("adminWindow", "食物"))
        item = self.feedTable.horizontalHeaderItem(3)
        item.setText(_translate("adminWindow", "投喂地点"))
        item = self.feedTable.horizontalHeaderItem(4)
        item.setText(_translate("adminWindow", "投喂用户"))
        item = self.feedTable.horizontalHeaderItem(5)
        item.setText(_translate("adminWindow", "投喂时间"))
        self.label_10.setText(_translate("adminWindow", "投喂猫猫："))
        self.label_11.setText(_translate("adminWindow", "注意，为了猫猫的健康，请勿喂食自带食物"))
        self.label_12.setText(_translate("adminWindow", "投喂务必领取提供的专用食物，谢谢"))
        self.label_13.setText(_translate("adminWindow", "投喂食物："))
        self.label_14.setText(_translate("adminWindow", "投喂地点："))
        self.addFeedBtn.setText(_translate("adminWindow", "提交"))
