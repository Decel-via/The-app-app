from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QLabel, QPushButton,
    QVBoxLayout, QHBoxLayout, QFrame, QStackedWidget, QLineEdit
)
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont
import sys

from Dashboard import Dashboard   # your existing dashboard class
from SignUp import SignUpPage
from LogIn import LoginPage


class StartUpPage(QWidget):
    def __init__(self, switch_to_dashboard_callback, switch_to_signup_callback, switch_to_login_callback ):
        super().__init__()
        self.switch_to_dashboard = switch_to_dashboard_callback
        self.switch_to_signup = switch_to_signup_callback
        self.switch_to_login = switch_to_login_callback



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

        login_button.clicked.connect(self.handle_login)
        button_layout.addWidget(login_button)

        signup_button = QPushButton("Sign Up")
        signup_button.clicked.connect(self.handle_signup)
        button_layout.addWidget(signup_button)

        guest_button = QPushButton("Continue as Guest")
        guest_button.clicked.connect(self.handle_guest)
        guest_button.setFixedWidth(500)
        lower_button_layout.addWidget(guest_button)

        main_layout.addLayout(button_layout)
        main_layout.addLayout(lower_button_layout)

    def handle_login(self):
        print("Log In button clicked")
        self.switch_to_login()

    def handle_signup(self):
        print("Sign Up button clicked")
        self.switch_to_signup()

    def handle_guest(self):
        print("Continue as Guest button clicked")
        self.switch_to_dashboard() 


class LogInWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Trakka - Welcome")
        self.setMinimumSize(1000, 600)
        self.setStyleSheet("background-color: #0f172a;")

        # ONE stacked widget
        self.stack = QStackedWidget()
        self.setCentralWidget(self.stack)

        # Pages (callbacks ONLY)
        self.startup_page = StartUpPage(
            self.show_dashboard,
            self.show_signup,
            self.show_login
        )

        self.login_page = LoginPage(
            self.show_start_up,
            self.show_dashboard
        )

        self.signup_page = SignUpPage(
            self.show_start_up
        )

        self.dashboard_page = Dashboard()

        # Add pages in a CLEAR order
        self.stack.addWidget(self.startup_page)   # index 0
        self.stack.addWidget(self.dashboard_page) # index 1
        self.stack.addWidget(self.signup_page)    # index 2
        self.stack.addWidget(self.login_page)     # index 3

        self.show_start_up()

    def show_start_up(self):
        self.stack.setCurrentIndex(0)

    def show_dashboard(self):
        self.stack.setCurrentIndex(1)

    def show_signup(self):
        self.stack.setCurrentIndex(2)

    def show_login(self):
        self.stack.setCurrentIndex(3)
