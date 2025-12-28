from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QLabel, QPushButton,
    QVBoxLayout, QHBoxLayout, QFrame, QStackedWidget, QLineEdit
)
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont
import sys

from app import Dashboard   # your existing dashboard class


class LogInPage(QWidget):
    def __init__(self, switch_to_dashboard_callback):
        super().__init__()
        self.switch_to_dashboard = switch_to_dashboard_callback



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
                font-size: 15px;
            }
             
            QPushButton:hover {
                background-color: #334155;
            }
        """)
        #]when self.setAutoFillBackground(True)
        main_layout = QVBoxLayout(self)
        #main_layout.setContentsMargins(50, 50, 50, 50)  # Make background visible around buttons
        #main_layout.setSpacing(20)
        title_label = QLabel("Trakka")
        title_font = QFont("Arial", 24, QFont.Weight.Bold)
        title_label.setFont(title_font)
        title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        main_layout.addWidget(title_label)

        button_layout = QHBoxLayout()
        lower_button_layout = QHBoxLayout()

        login_button = QPushButton("Log In")
        #login_button.setStyleSheet("background-color: #0f172a;")

        login_button.clicked.connect(self.handle_login)
        button_layout.addWidget(login_button)

        signup_button = QPushButton("Sign Up")
        signup_button.clicked.connect(self.handle_signup)
        button_layout.addWidget(signup_button)

        guest_button = QPushButton("Continue as Guest")
        guest_button.clicked.connect(self.handle_guest)
        guest_button.setFixedWidth(500)
        lower_button_layout.addWidget(guest_button)
        #main_layout.addWidget(guest_button)

        main_layout.addLayout(button_layout)
        main_layout.addLayout(lower_button_layout)

        # separator = QFrame()
        # separator.setFrameShape(QFrame.Shape.HLine)
        # separator.setFrameShadow(QFrame.Shadow.Sunken)
        # main_layout.addWidget(separator)









    def handle_login(self):
        print("Log In button clicked")
        

    def handle_signup(self):
        print("Sign Up button clicked")

    def handle_guest(self):
        print("Continue as Guest button clicked")
        self.switch_to_dashboard() 


class LogInWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Trakka - Log In")
        self.setMinimumSize(1000, 600)
        self.setStyleSheet("background-color: #0f172a;")  # Replace with any color

        # Stacked widget as the ONE central widget
        self.stack = QStackedWidget()
        self.setCentralWidget(self.stack)

        # Pages
        self.login_page = LogInPage(self.show_dashboard)
        self.dashboard_page = Dashboard()  

        self.stack.addWidget(self.login_page)      
        self.stack.addWidget(self.dashboard_page)  

        self.stack.setCurrentIndex(0) 

    def show_dashboard(self):
        self.stack.setCurrentIndex(1)



