# -------------------------------------------------------------------
# This file holds ONLY the StartUpPage UI/layout and theme toggle.
# All navigation and stacking is handled in manager.py
# -------------------------------------------------------------------

from PyQt6.QtWidgets import (
    QWidget, QLabel, QPushButton, QVBoxLayout, QHBoxLayout,
    QFrame, QLineEdit, QSizePolicy
)
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont, QPixmap


class StartUpPage(QWidget):

    def __init__(self,
                 switch_to_dashboard_callback,
                 switch_to_signup_callback,
                 switch_to_login_callback,
                 theme_manager):

        super().__init__()

        # Callbacks passed from manager.py -> used when buttons clicked
        self.switch_to_dashboard = switch_to_dashboard_callback
        self.switch_to_signup = switch_to_signup_callback
        self.switch_to_login = switch_to_login_callback

        self.theme_manager = theme_manager  # used for light/dark theme switching

        # ---------------------- MAIN LAYOUT ---------------------- #
        main_layout = QVBoxLayout(self)
        main_layout.setContentsMargins(60, 30, 60, 40)
        main_layout.setSpacing(20)

        # ---------------------- TOP BAR -------------------------- #
        top_bar = QHBoxLayout()
        top_bar.addStretch()

        self.theme_btn = QPushButton("☀")  # default dark -> button shows icon to switch to light
        self.theme_btn.setFixedSize(36, 36)
        self.theme_btn.clicked.connect(self.toggle_theme)

        top_bar.addWidget(self.theme_btn)
        main_layout.addLayout(top_bar)

        # ---------------------- CONTENT ----------------------  #
        content = QHBoxLayout()
        main_layout.addLayout(content)

        # =========== LEFT SIDE — Logo + Brand Text =============== #
        left = QVBoxLayout()
        content.addLayout(left, 2)

        logo = QLabel()
        pix = QPixmap("images/Logo.png")
        if not pix.isNull():
            pix = pix.scaled(108, 108, Qt.AspectRatioMode.KeepAspectRatio)
            logo.setPixmap(pix)

        title = QLabel("TRAKKA")
        title.setFont(QFont("Segoe UI", 22, QFont.Weight.Bold))

        row = QHBoxLayout()
        row.addWidget(logo)
        row.addWidget(title)
        row.addStretch()
        left.addLayout(row)

        hero = QLabel("Stay on top of your tasks\nand projects.")
        hero.setFont(QFont("Segoe UI", 22, QFont.Weight.DemiBold))

        subtitle = QLabel("Create, track & complete tasks all in one place.")
        subtitle.setObjectName("mutedLabel")

        left.addSpacing(30)
        left.addWidget(hero)
        left.addWidget(subtitle)
        left.addStretch()

        # =========== RIGHT SIDE — Sign Up Card =================== #
        right_container = QVBoxLayout()
        content.addLayout(right_container, 3)

        card = QFrame()
        card.setObjectName("card")
        card.setMaximumWidth(420)
        layout = QVBoxLayout(card)
        layout.setContentsMargins(32, 32, 32, 32)
        layout.addWidget(QLabel("Create your account", font=QFont("Segoe UI", 18, QFont.Weight.Bold)))

        # Form fields
        row = QHBoxLayout()
        self.first = QLineEdit(placeholderText="First Name")
        self.last = QLineEdit(placeholderText="Last Name")
        row.addWidget(self.first)
        row.addWidget(self.last)
        layout.addLayout(row)

        self.email = QLineEdit(placeholderText="Email")
        self.passwd = QLineEdit(placeholderText="Password")
        self.passwd.setEchoMode(QLineEdit.EchoMode.Password)

        layout.addWidget(self.email)
        layout.addWidget(self.passwd)

        # Create account btn
        signup_btn = QPushButton("Create Account", objectName="primaryButton")
        signup_btn.clicked.connect(self.switch_to_signup)
        layout.addWidget(signup_btn)

        # Continue as guest
        guest = QPushButton("Continue as Guest")
        guest.clicked.connect(self.switch_to_dashboard)
        layout.addWidget(guest)

        # Login option
        login_row = QHBoxLayout()
        login_row.addWidget(QLabel("Already have an account?", objectName="mutedLabel"))
        login_btn = QPushButton("Log In", objectName="linkButton")
        login_btn.clicked.connect(self.switch_to_login)
        login_row.addWidget(login_btn)
        layout.addLayout(login_row)


        right_container.addStretch()
        right_container.addWidget(card)
        right_container.addStretch()

    # ------------ THEME SWITCH LOGIC ------------ #
    def toggle_theme(self):
        self.theme_manager.toggle()          # swap theme
        self.theme_btn.setText("🌙" if self.theme_manager.current_theme == "light" else "☀")
