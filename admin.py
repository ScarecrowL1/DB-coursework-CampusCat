from adminWindow import Ui_adminWindow
from database import dataBase
from newAdmin import newAdmin
from PyQt5.QtWidgets import *



class admin(Ui_adminWindow, QMainWindow):

    def __init__(self):
        super(admin, self).__init__()
        self.setupUi(self)
        self.activateButton()
        self.fillBox()
        self.newAdminWindow = None


    def activateButton(self):
        self.catinfoBtn.clicked.connect(self.switch)
        self.witnessBtn.clicked.connect(self.switch)
        self.feedBtn.clicked.connect(self.switch)
        self.newAdminBtn.clicked.connect(self.newAdmin)

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
