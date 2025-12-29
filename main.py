
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QLabel, QPushButton,
    QVBoxLayout, QHBoxLayout, QFrame
)
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont
import os
import sys

import StartUp


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = StartUp.LogInWindow()
    window.show()
    sys.exit(app.exec())