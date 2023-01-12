from threading import Thread

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

from database import dataBase
from userWindow import Ui_userWindow


class user(Ui_userWindow, QMainWindow):
    sig_cat = pyqtSignal(list)
    sig_wit = pyqtSignal(list)
    sig_feed = pyqtSignal(list)

    def __init__(self, username):
        super(user, self).__init__()
        self.setupUi(self)
        self.setWindowTitle('校园猫管理平台')
        self.username = username
        self.activateButton()
        self.fillBox()
        self.sizeTables()
        self.sig_cat.connect(self.genCatTable)
        self.sig_wit.connect(self.genWitTable)
        self.sig_feed.connect(self.genFeedTable)
        self.showCat()
        self.showWitness()
        self.showFeed()



    def activateButton(self):
        self.catinfoBtn.clicked.connect(self.switch)
        self.witnessBtn.clicked.connect(self.switch)
        self.feedBtn.clicked.connect(self.switch)

        self.addWitButton.clicked.connect(self.addWitness)
        self.addFeedButton.clicked.connect(self.addFeed)

    def switch(self):
        sender = self.sender()
        if sender.text() == '猫猫花名册':
            self.stackedWidget.setCurrentIndex(0)
        if sender.text() == '猫猫位置打卡':
            self.stackedWidget.setCurrentIndex(1)
        if sender.text() == '记录我的投喂':
            self.stackedWidget.setCurrentIndex(2)

    def fillBox(self):
        database = dataBase()
        cnt, cat = database.selectAll('cat')
        self.witCatNameBox.addItems(a[4] for a in cat)
        self.feedCatNameBox.addItems(a[4] for a in cat)

    def addWitness(self):
        userName = self.username
        catName = self.witCatNameBox.currentText()
        locName = self.witLocBox.currentText()

        database = dataBase()
        userNum = database.getUserNum(userName)
        catNum = database.getCatNum(catName)
        locNum = database.getLocNum(locName)

        database.addWitness(userNum, locNum, catNum)
        database.update()
        QMessageBox.information(self, '提示', '添加成功', QMessageBox.Ok)

        self.showWitness()

    def addFeed(self):
        userName = self.username
        catName = self.feedCatNameBox.currentText()
        locName = self.feedLocBox.currentText()
        foodName = self.feedFoodBox.currentText()

        database = dataBase()
        userNum = database.getUserNum(userName)
        catNum = database.getCatNum(catName)
        locNum = database.getLocNum(locName)
        foodNum = database.getFoodNum(foodName)

        database.addFeed(foodNum, catNum, locNum, userNum)
        database.update()
        QMessageBox.information(self, '提示', '添加成功', QMessageBox.Ok)

        self.showFeed()

    def showCat(self):
        thread = Thread(target=self.getCatView())
        thread.start()

    def getCatView(self):
        database = dataBase()
        cnt, res = database.getCatView()
        self.sig_cat.emit([cnt, res])


    def genCatTable(self, res):
        catView = res[1]  # res第0个是cnt，第1个是集合的集合
        column = len(catView[0])  # 列数
        row = 0
        for info in catView:
            if self.catTabel.rowCount() <= row:
                self.catTabel.insertRow(row)
            for i in range(column):
                itemValue = info[i]
                item = QTableWidgetItem(str(itemValue))
                self.catTabel.setItem(row, i, item)
            row = row + 1
        for i in range(row):
            for j in range(column):
                item = self.catTabel.item(i, j)
                item.setTextAlignment(Qt.AlignVCenter | Qt.AlignHCenter)

    def showWitness(self):
        thread = Thread(target=self.getWitView())
        thread.start()

    def getWitView(self):
        database = dataBase()
        cnt, res = database.getWitView()
        self.sig_wit.emit([cnt, res])

    def genWitTable(self, res):
        witView = res[1]  # res第0个是cnt，第1个是集合的集合
        column = len(witView[0])  # 列数
        row = 0
        for info in witView:
            if self.witnessTable.rowCount() <= row:
                self.witnessTable.insertRow(row)
            for i in range(column):
                itemValue = info[i]
                item = QTableWidgetItem(str(itemValue))
                self.witnessTable.setItem(row, i, item)
            row = row + 1
        for i in range(row):
            for j in range(column):
                item = self.witnessTable.item(i, j)
                item.setTextAlignment(Qt.AlignVCenter | Qt.AlignHCenter)

    def showFeed(self):
        thread = Thread(target=self.getFeedView())
        thread.start()

    def getFeedView(self):
        database = dataBase()
        cnt, res = database.getFeedView()
        self.sig_feed.emit([cnt, res])

    def genFeedTable(self, res):
        FeedView = res[1]  # res第0个是cnt，第1个是集合的集合
        column = len(FeedView[0])  # 列数
        row = 0
        for info in FeedView:
            if self.feedTable.rowCount() <= row:
                self.feedTable.insertRow(row)
            for i in range(column):
                itemValue = info[i]
                item = QTableWidgetItem(str(itemValue))
                self.feedTable.setItem(row, i, item)
            row = row + 1
        for i in range(row):
            for j in range(column):
                item = self.feedTable.item(i, j)
                item.setTextAlignment(Qt.AlignVCenter | Qt.AlignHCenter)


def sizeTables(self):
    self.catTabel.setEditTriggers(QAbstractItemView.NoEditTriggers)
    self.catTabel.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)
    self.catTabel.verticalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)

    self.feedTable.setEditTriggers(QAbstractItemView.NoEditTriggers)
    self.feedTable.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)
    self.feedTable.verticalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)

    self.witnessTable.setEditTriggers(QAbstractItemView.NoEditTriggers)
    self.witnessTable.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)
    self.witnessTable.verticalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)