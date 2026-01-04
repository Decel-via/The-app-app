#------------------------------------------------------------
# This file controls:
#  - Window (main app)
#  - Theme application
#  - Page navigation (StartUp/Login/Signup/Dashboard)
#------------------------------------------------------------

from PyQt6.QtWidgets import QMainWindow, QStackedWidget

from StartUp import StartUpPage
from SignUp import SignUpPage
from LogIn import LoginPage
from Dashboard import Dashboard

from theme_switch.theme_manager import ThemeManager
from PyQt6.QtGui import QIcon


class LogInWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle(" ")
        self.setWindowIcon(QIcon("images/Logo.png"))
        self.setMinimumSize(1100, 650)
        

        # Theme system
        self.theme = ThemeManager("dark")  # default theme
        self.theme.apply()

        self.stack = QStackedWidget()
        self.setCentralWidget(self.stack)

        # Screens
        self.startup  = StartUpPage(self.show_dashboard, self.show_signup, self.show_login, self.theme)
        self.signup   = SignUpPage(self.show_startup)
        self.login    = LoginPage(self.show_startup, self.show_dashboard)
        self.dashboard= Dashboard(self.show_startup)

        self.stack.addWidget(self.startup)     
        self.stack.addWidget(self.dashboard)   
        self.stack.addWidget(self.signup)      
        self.stack.addWidget(self.login)       

        self.show_startup()

    # Navigation shortcuts
    def show_startup(self):  self.stack.setCurrentIndex(0)
    def show_dashboard(self):self.stack.setCurrentIndex(1)
    def show_signup(self):   self.stack.setCurrentIndex(2)
    def show_login(self):    self.stack.setCurrentIndex(3)
