import pyqt5
from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow
import sys
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Hello PyQt5")
        self.setGeometry(100, 100, 400, 300)
        label = QLabel("Welcome to PyQt5!", self)
        label.setGeometry(150, 130, 200, 40)