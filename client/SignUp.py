from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QLabel, QPushButton,
    QVBoxLayout, QHBoxLayout, QFrame, QStackedWidget, QLineEdit
)
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont



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

        username_layout = QHBoxLayout()
        email_layout = QHBoxLayout()
        password_layout = QHBoxLayout()

        username = QLineEdit()
        username.setPlaceholderText("Username")
        username.setFixedWidth(600)

        email = QLineEdit()
        email.setPlaceholderText("Email")
        email.setFixedWidth(600)

        password = QLineEdit()
        password.setPlaceholderText("Password")
        password.setEchoMode(QLineEdit.EchoMode.Password)
        password.setFixedWidth(600)

        button_layout = QHBoxLayout()

        back_btn = QPushButton("Back")
        back_btn.clicked.connect(go_back)
        back_btn.setFixedWidth(300)

        signUp_btn = QPushButton("Sign Up")
        #signUp_btn.clicked.connect(go_back)
        signUp_btn.setFixedWidth(300)

        layout.addWidget(title)
        username_layout.addWidget(username)
        email_layout.addWidget(email)
        password_layout.addWidget(password)


        button_layout.addWidget(signUp_btn)
        button_layout.addWidget(back_btn)

        layout.addLayout(username_layout)
        layout.addLayout(email_layout)
        layout.addLayout(password_layout)
        layout.addSpacing(50)
        layout.addLayout(button_layout)
        layout.addSpacing(30)
