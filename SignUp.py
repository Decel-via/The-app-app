from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QLabel, QPushButton,
    QVBoxLayout, QHBoxLayout, QFrame, QStackedWidget, QLineEdit
)
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont
import sys


class SignUpPage(QWidget):
    def __init__(self, go_back):
        super().__init__()

        self.setStyleSheet("""
            QWidget {
                background-color: #0f172a;
                color: white;
                font-family: Segoe UI;
            }
            QLineEdit {
                background-color: #1e293b;
                border-radius: 8px;
                padding: 10px;
                color: white;
                border: none;
            }
            QPushButton {
                background-color: #1e293b;
                color: white;
                border-radius: 8px;
                padding: 10px;
            }
            QPushButton:hover {
                background-color: #334155;
            }
        """)

        layout = QVBoxLayout(self)

        title = QLabel("Sign Up")
        title.setFont(QFont("Arial", 22, QFont.Weight.Bold))
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)

        username = QLineEdit()
        username.setPlaceholderText("Username")

        email = QLineEdit()
        email.setPlaceholderText("Email")

        password = QLineEdit()
        password.setPlaceholderText("Password")
        password.setEchoMode(QLineEdit.EchoMode.Password)

        back_btn = QPushButton("Back")
        back_btn.clicked.connect(go_back)  # ✅ THIS IS THE KEY

        layout.addWidget(title)
        layout.addWidget(username)
        layout.addWidget(email)
        layout.addWidget(password)
        layout.addWidget(back_btn)
