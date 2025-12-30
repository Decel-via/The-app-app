
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QLabel, QPushButton,
    QVBoxLayout, QHBoxLayout, QFrame, QStackedWidget, QLineEdit
)
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont
import sys


class LoginPage(QWidget):
    def __init__(self,go_back, go_dashboard): # add callback for login and add callback for dashboard
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

        title = QLabel("Log In")
        title.setFont(QFont("Arial", 22, QFont.Weight.Bold))
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)

        email_layout = QHBoxLayout()
        password_layout = QHBoxLayout()

        email = QLineEdit()
        email.setPlaceholderText("Email/ Username")
        email.setFixedWidth(600)

        password = QLineEdit()
        password.setPlaceholderText("Password")
        password.setEchoMode(QLineEdit.EchoMode.Password)
        password.setFixedWidth(600)

        button_layout = QHBoxLayout()
        login_btn = QPushButton("Log In")
        login_btn.setFixedWidth(300)
        login_btn.clicked.connect(go_dashboard)

        back_btn = QPushButton("Back")
        back_btn.clicked.connect(go_back)
        back_btn.setFixedWidth(300)

        layout.addWidget(title)
        email_layout.addWidget(email)
        password_layout.addWidget(password)

        layout.addLayout(email_layout)
        layout.addLayout(password_layout)

        layout.addSpacing(50)

        button_layout.addWidget(login_btn)
        button_layout.addWidget(back_btn)

        layout.addLayout(button_layout)
        layout.addSpacing(30)
