
from PyQt5.QtWidgets import *

from userWindow import Ui_userWindow
class user(Ui_userWindow, QMainWindow):


    def __init__(self, username):
        super(user, self).__init__()
        self.setupUi(self)
        self.username = username

