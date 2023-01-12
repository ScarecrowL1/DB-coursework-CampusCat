from threading import Thread

from PyQt5.QtCore import *

from adminWindow import Ui_adminWindow
from database import dataBase
from newAdmin import newAdmin
from PyQt5.QtWidgets import *


class admin(Ui_adminWindow, QMainWindow):
    sig_cat = pyqtSignal(list)
    sig_wit = pyqtSignal(list)
    sig_feed = pyqtSignal(list)

    def __init__(self, username):
        super(admin, self).__init__()
        self.setupUi(self)
        self.activateButton()
        self.setWindowTitle('校园猫管理平台（管理员端）')
        self.fillBox()
        self.sig_cat.connect(self.genCatTable)
        self.sig_wit.connect(self.genWitTable)
        self.sig_feed.connect(self.genFeedTable)
        self.sizeTables()
        self.showCat()
        self.showWitness()
        self.showFeed()
        self.username = username
        self.newAdminWindow = None

    def activateButton(self):
        self.catinfoBtn.clicked.connect(self.switch)
        self.witnessBtn.clicked.connect(self.switch)
        self.feedBtn.clicked.connect(self.switch)

        self.newAdminBtn.clicked.connect(self.newAdmin)

        self.addCatButton.clicked.connect(self.addCat)
        self.addWitButton.clicked.connect(self.addWitness)
        self.addFeedBtn.clicked.connect(self.addFeed)

    def switch(self):
        sender = self.sender()
        if sender.text() == '猫猫花名册':
            self.stackedWidget.setCurrentIndex(0)
        if sender.text() == '猫猫位置打卡':
            self.stackedWidget.setCurrentIndex(1)
        if sender.text() == '记录我的投喂':
            self.stackedWidget.setCurrentIndex(2)

    def newAdmin(self):
        self.newAdminWindow = newAdmin()
        self.newAdminWindow.show()

    def fillBox(self):
        database = dataBase()
        cnt, cat = database.selectAll('cat')
        self.witCatNameBox.addItems(a[4] for a in cat)
        self.feedCatBox.addItems(a[4] for a in cat)

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

    def addCat(self):
        catName = self.addCatNameEdit.text()
        catGender = self.addCatGenderBox.currentText()
        catRace = self.AddCatRaceEdit.text()
        catLoc = self.addLocBox.currentText()
        catVac = self.addCatVacBox.currentText()
        catOther = self.addOtherEdit.toPlainText()

        if '' in [catName, catRace]:
            QMessageBox.information(self, '提示', '除了备注都是必填~请检查表单', QMessageBox.Ok)
            return
        database = dataBase()
        cnt, res = database.select('cat', 'catName', catName)
        if cnt > 0:
            QMessageBox.information(self, '提示', '该猫已存在，或与档案内的猫重名', QMessageBox.Ok)
        cnt, res = database.select('catrace', 'raceName', catRace)
        if cnt == 0:
            database.addRace(catRace)

        raceNum = database.getRaceNum(catRace)
        locNum = database.getLocNum(catLoc)
        vacNum = database.getVacNum(catVac)

        database.addCat(vacNum, raceNum, locNum, catName, catGender, catOther)
        database.update()
        QMessageBox.information(self, '提示', '添加成功', QMessageBox.Ok)

        self.addCatNameEdit.clear()
        self.addOtherEdit.clear()
        self.AddCatRaceEdit.clear()
        self.showCat()

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
        catName = self.feedCatBox.currentText()
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

