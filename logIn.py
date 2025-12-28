
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QLabel, QPushButton,
    QVBoxLayout, QHBoxLayout, QFrame
)
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont
import os
import sys

class LogInWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Log In")
        self.setGeometry(100, 100, 400, 300)
        self.initUI()

    def initUI(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        main_layout = QVBoxLayout()

        title_label = QLabel("Trakka")
        title_font = QFont("Arial", 16, QFont.Weight.Bold)
        title_label.setFont(title_font)
        title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        main_layout.addWidget(title_label)

        button_layout = QHBoxLayout()

        login_button = QPushButton("Log In")
        login_button.clicked.connect(self.handle_login)
        button_layout.addWidget(login_button)

        signup_button = QPushButton("Sign Up")
        signup_button.clicked.connect(self.handle_signup)
        button_layout.addWidget(signup_button)

        main_layout.addLayout(button_layout)

        separator = QFrame()
        separator.setFrameShape(QFrame.Shape.HLine)
        separator.setFrameShadow(QFrame.Shadow.Sunken)
        main_layout.addWidget(separator)

        guest_button = QPushButton("Continue as Guest")
        guest_button.clicked.connect(self.handle_guest)
        main_layout.addWidget(guest_button, alignment=Qt.AlignmentFlag.AlignCenter)

        central_widget.setLayout(main_layout)

    def handle_login(self):
        print("Log In button clicked")

    def handle_signup(self):
        print("Sign Up button clicked")

    def handle_guest(self):
        print("Continue as Guest button clicked")
