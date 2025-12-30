from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QLabel, QPushButton,
    QVBoxLayout, QHBoxLayout, QFrame
)
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont
import sys



def go_home(self):
    from Login import LoginWindow
    self.login - LoginWindow()
    self.login.show()
    self.close()
