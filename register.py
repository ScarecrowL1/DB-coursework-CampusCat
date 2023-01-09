from PyQt5.QtWidgets import *

from registerWindow import Ui_Register


class register(Ui_Register, QMainWindow):
    def __init__(self):
        super(register, self).__init__()
        self.setupUi(self)
        self.noButton.clicked.connect(self.close)
        self.yesButton.clicked.connect(self.register_)

        def register_():
            username = self.usernameEdit.text()
            passwd = self.passwdEdit.text()
            conpasswd = self.conpwEdit.text()