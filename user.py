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
        self.sig_cat.connect(self.genCatTable)
        self.showCat()

    def activateButton(self):
        self.catinfoBtn.clicked.connect(self.switch)
        self.witnessBtn.clicked.connect(self.switch)
        self.feedBtn.clicked.connect(self.switch)

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
