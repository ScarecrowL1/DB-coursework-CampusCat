from adminWindow import Ui_userWindow
from PyQt5.QtWidgets import *

class admin(Ui_userWindow, QMainWindow):

    def __init__(self):
        super(admin, self).__init__()
        self.setupUi(self)
