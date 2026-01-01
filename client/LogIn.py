from PyQt6.QtWidgets import (
    QWidget, QLabel, QPushButton, QVBoxLayout, QHBoxLayout,
    QFrame, QLineEdit, QCheckBox
)
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont


class LoginPage(QWidget):
    def __init__(self, go_back, go_dashboard):
        super().__init__()

        # For targeting page
        self.setObjectName("loginPage")

        # === Outer layout: center content on dark background === #
        outer_layout = QVBoxLayout(self)
        outer_layout.setContentsMargins(60, 60, 60, 60)
        outer_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # === Card === #
        card = QFrame()
        card.setObjectName("card") # from QFrame#card from theme_manager
        card.setFixedWidth(420)

        card_layout = QVBoxLayout(card)
        card_layout.setContentsMargins(36, 32, 36, 32)
        card_layout.setSpacing(16)

        # Title
        title = QLabel("Welcome back 👋")
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        title.setFont(QFont("Segoe UI", 18, QFont.Weight.Bold))
        card_layout.addWidget(title)

        # Email label + input
        email_label = QLabel("Email")
        email_label.setObjectName("mutedLabel")  # muted label style from theme_manager
        card_layout.addWidget(email_label)

        self.email_input = QLineEdit()
        self.email_input.setPlaceholderText("Enter your email")
        card_layout.addWidget(self.email_input)

        # Password label + input
        password_label = QLabel("Password")
        password_label.setObjectName("mutedLabel")
        card_layout.addWidget(password_label)

        self.password_input = QLineEdit()
        self.password_input.setPlaceholderText("Enter your password")
        self.password_input.setEchoMode(QLineEdit.EchoMode.Password)
        card_layout.addWidget(self.password_input)

        # Remember me + Forgot password
        options_layout = QHBoxLayout()
        self.remember_me = QCheckBox("Remember me")
        options_layout.addWidget(self.remember_me)

        options_layout.addStretch()

        forgot_btn = QPushButton("Forgot password?")
        forgot_btn.setObjectName("linkButton")   # link style from theme_manager
        forgot_btn.setCursor(Qt.CursorShape.PointingHandCursor)
        options_layout.addWidget(forgot_btn)

        card_layout.addLayout(options_layout)

        # Log In button 
        login_btn = QPushButton("Log In")
        login_btn.setObjectName("primaryButton")  
        login_btn.setFixedHeight(40)
        login_btn.setCursor(Qt.CursorShape.PointingHandCursor)
        login_btn.clicked.connect(go_dashboard)
        card_layout.addWidget(login_btn)

        # Bottom row: New to TRAKKA? Create an account >
        bottom_layout = QHBoxLayout()
        new_label = QLabel("New to TRAKKA?")
        new_label.setObjectName("mutedLabel")
        bottom_layout.addWidget(new_label)

        signup_btn = QPushButton("Create an account  >")
        signup_btn.setObjectName("linkButton")
        signup_btn.setCursor(Qt.CursorShape.PointingHandCursor)
        signup_btn.clicked.connect(go_back)
        bottom_layout.addWidget(signup_btn)

        bottom_layout.addStretch()
        card_layout.addLayout(bottom_layout)

        # Add card to outer layout
        outer_layout.addWidget(card)
