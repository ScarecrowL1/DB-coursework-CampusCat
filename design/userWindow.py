# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'userWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_userWindow(object):
    def setupUi(self, userWindow):
        userWindow.setObjectName("userWindow")
        userWindow.resize(1254, 673)
        self.centralwidget = QtWidgets.QWidget(userWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(260, 10, 731, 81))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.witnessBtn = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.witnessBtn.setObjectName("witnessBtn")
        self.gridLayout.addWidget(self.witnessBtn, 0, 1, 1, 1)
        self.feedBtn = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.feedBtn.setObjectName("feedBtn")
        self.gridLayout.addWidget(self.feedBtn, 0, 2, 1, 1)
        self.catinfoBtn = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.catinfoBtn.setObjectName("catinfoBtn")
        self.gridLayout.addWidget(self.catinfoBtn, 0, 0, 1, 1)
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setGeometry(QtCore.QRect(10, 100, 1221, 561))
        self.stackedWidget.setObjectName("stackedWidget")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.catTabel = QtWidgets.QTableWidget(self.page)
        self.catTabel.setGeometry(QtCore.QRect(160, 0, 1001, 551))
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
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.witnessTable = QtWidgets.QTableWidget(self.page_2)
        self.witnessTable.setGeometry(QtCore.QRect(460, 0, 741, 541))
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
        self.feedTable.setGeometry(QtCore.QRect(380, 0, 831, 531))
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
        self.feedCatNameBox = QtWidgets.QComboBox(self.page_3)
        self.feedCatNameBox.setGeometry(QtCore.QRect(130, 130, 171, 41))
        self.feedCatNameBox.setObjectName("feedCatNameBox")
        self.label_13 = QtWidgets.QLabel(self.page_3)
        self.label_13.setGeometry(QtCore.QRect(60, 240, 54, 12))
        self.label_13.setObjectName("label_13")
        self.label_14 = QtWidgets.QLabel(self.page_3)
        self.label_14.setGeometry(QtCore.QRect(60, 330, 61, 16))
        self.label_14.setObjectName("label_14")
        self.addFeedButton = QtWidgets.QPushButton(self.page_3)
        self.addFeedButton.setGeometry(QtCore.QRect(160, 430, 75, 23))
        self.addFeedButton.setObjectName("addFeedButton")
        self.feedLocBox = QtWidgets.QComboBox(self.page_3)
        self.feedLocBox.setGeometry(QtCore.QRect(130, 320, 171, 41))
        self.feedLocBox.setObjectName("feedLocBox")
        self.feedFoodBox = QtWidgets.QComboBox(self.page_3)
        self.feedFoodBox.setGeometry(QtCore.QRect(130, 230, 171, 41))
        self.feedFoodBox.setObjectName("feedFoodBox")
        self.stackedWidget.addWidget(self.page_3)
        userWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(userWindow)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(userWindow)

    def retranslateUi(self, userWindow):
        _translate = QtCore.QCoreApplication.translate
        userWindow.setWindowTitle(_translate("userWindow", "MainWindow"))
        self.witnessBtn.setText(_translate("userWindow", "??????????????????"))
        self.feedBtn.setText(_translate("userWindow", "??????????????????"))
        self.catinfoBtn.setText(_translate("userWindow", "???????????????"))
        self.catTabel.setSortingEnabled(False)
        item = self.catTabel.horizontalHeaderItem(0)
        item.setText(_translate("userWindow", "????????????"))
        item = self.catTabel.horizontalHeaderItem(1)
        item.setText(_translate("userWindow", "????????????"))
        item = self.catTabel.horizontalHeaderItem(2)
        item.setText(_translate("userWindow", "??????"))
        item = self.catTabel.horizontalHeaderItem(3)
        item.setText(_translate("userWindow", "??????"))
        item = self.catTabel.horizontalHeaderItem(4)
        item.setText(_translate("userWindow", "???????????????"))
        item = self.catTabel.horizontalHeaderItem(5)
        item.setText(_translate("userWindow", "????????????"))
        item = self.catTabel.horizontalHeaderItem(6)
        item.setText(_translate("userWindow", "??????"))
        item = self.witnessTable.horizontalHeaderItem(0)
        item.setText(_translate("userWindow", "????????????"))
        item = self.witnessTable.horizontalHeaderItem(1)
        item.setText(_translate("userWindow", "????????????"))
        item = self.witnessTable.horizontalHeaderItem(2)
        item.setText(_translate("userWindow", "??????"))
        item = self.witnessTable.horizontalHeaderItem(3)
        item.setText(_translate("userWindow", "????????????"))
        item = self.witnessTable.horizontalHeaderItem(4)
        item.setText(_translate("userWindow", "????????????"))
        self.label_8.setText(_translate("userWindow", "???????????????"))
        self.label_9.setText(_translate("userWindow", "???????????????"))
        self.addWitButton.setText(_translate("userWindow", "??????"))
        item = self.feedTable.horizontalHeaderItem(0)
        item.setText(_translate("userWindow", "????????????"))
        item = self.feedTable.horizontalHeaderItem(1)
        item.setText(_translate("userWindow", "????????????"))
        item = self.feedTable.horizontalHeaderItem(2)
        item.setText(_translate("userWindow", "??????"))
        item = self.feedTable.horizontalHeaderItem(3)
        item.setText(_translate("userWindow", "????????????"))
        item = self.feedTable.horizontalHeaderItem(4)
        item.setText(_translate("userWindow", "????????????"))
        item = self.feedTable.horizontalHeaderItem(5)
        item.setText(_translate("userWindow", "????????????"))
        self.label_10.setText(_translate("userWindow", "???????????????"))
        self.label_11.setText(_translate("userWindow", "?????????????????????????????????????????????????????????"))
        self.label_12.setText(_translate("userWindow", "????????????????????????????????????????????????"))
        self.label_13.setText(_translate("userWindow", "???????????????"))
        self.label_14.setText(_translate("userWindow", "???????????????"))
        self.addFeedButton.setText(_translate("userWindow", "??????"))
