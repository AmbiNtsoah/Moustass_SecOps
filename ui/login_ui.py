from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QLineEdit, QBoxLayout
import sys

""" Class for our login """
class LoginInterface(QWidget):
    """ Constructor """
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Login")
        self.setFixedSize(300, 200)