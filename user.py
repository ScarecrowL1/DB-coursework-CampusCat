from PyQt5.QtWidgets import *

from database import dataBase
from userWindow import Ui_userWindow


class user(Ui_userWindow, QMainWindow):

    def __init__(self, username):
        super(user, self).__init__()
        self.setupUi(self)
        self.setWindowTitle('校园猫管理平台')
        self.username = username
        self.activateButton()
        self.fillBox()

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

    def getCatView(self):
        database = dataBase()
