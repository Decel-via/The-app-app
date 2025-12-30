from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QLabel, QPushButton,
    QVBoxLayout, QHBoxLayout, QFrame
)
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont





class Dashboard(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Trakka Dashboard")
        self.setMinimumSize(1000, 600)
        

        # Central widget
        central = QWidget()
        self.setCentralWidget(central)
        main_layout = QHBoxLayout(central)

        # LEFT SIDEBAR
        left_sidebar = QFrame()
        left_sidebar.setFixedWidth(220)
        left_sidebar.setStyleSheet("""
            QFrame {
                background-color: #121826;
            }
            QPushButton {
                color: white;
                background-color: transparent;
                border: none;
                text-align: left;
                padding: 14px;
                font-size: 15px;
            }
            QPushButton:hover {
                background-color: #1f2937;
            }
        """)

        left_layout = QVBoxLayout(left_sidebar)

        title = QLabel("🚀 Dashboard")
        title.setStyleSheet("color: white;")
        title.setFont(QFont("Segoe UI", 18, QFont.Weight.Bold))
        left_layout.addWidget(title)
        left_layout.addSpacing(20)

        for name in ["Home", "Tasks", "Projects", "Statistics", "Settings"]:
            left_layout.addWidget(QPushButton(name))

        left_layout.addStretch()

        # MAIN CONTENT AREA
        content = QFrame()
        content.setStyleSheet("""
            QFrame {
                background-color: #0f172a;
            }
            QLabel {
                color: white;
            }
        """)
        content_layout = QVBoxLayout(content)

        header = QLabel("Welcome Back 👋")
        header.setFont(QFont("Segoe UI", 26, QFont.Weight.Bold))
        content_layout.addWidget(header)

        subtitle = QLabel("Here's an overview of your system")
        subtitle.setStyleSheet("color: #94a3b8;")
        content_layout.addWidget(subtitle)
        content_layout.addSpacing(20)

        # CARDS SECTION
        cards_layout = QHBoxLayout()
        for title_text, value in [
            ("Active Users", "1,248"),
            ("Revenue", "£87,540"),
            ("Errors", "3")
        ]:
            card = QFrame()
            card.setStyleSheet("""
                QFrame {
                    background-color: #1e293b;
                    border-radius: 14px;
                }
            """)
            card_layout = QVBoxLayout(card)

            card_title = QLabel(title_text)
            card_title.setStyleSheet("color: #94a3b8;")
            card_value = QLabel(value)
            card_value.setFont(QFont("Segoe UI", 22, QFont.Weight.Bold))

            card_layout.addWidget(card_title)
            card_layout.addWidget(card_value)
            cards_layout.addWidget(card)

        content_layout.addLayout(cards_layout)
        content_layout.addStretch()

        # RIGHT SIDEBAR
        right_sidebar = QFrame()
        right_sidebar.setFixedWidth(260)
        right_sidebar.setStyleSheet("""
            QFrame {
                background-color: #111827;
            }
            QLabel {
                color: white;
            }
        """)

        right_layout = QVBoxLayout(right_sidebar)

        # PROFILE SECTION (TOP RIGHT)
        profile_card = QFrame()
        profile_card.setStyleSheet("""
            QFrame {
                background-color: #1e293b;
                border-radius: 12px;
            }
        """)
        profile_layout = QHBoxLayout(profile_card)

        # Avatar
        avatar = QLabel("👤")
        avatar.setFixedSize(55, 55)
        avatar.setAlignment(Qt.AlignmentFlag.AlignCenter)
        avatar.setStyleSheet("""
            QLabel {
                background-color: #3b82f6;
                border-radius: 27px;
                font-size: 18px;
                font-weight: bold;
            }
        """)

        # Name + role
        info_layout = QVBoxLayout()
        name = QLabel("User")
        name.setFont(QFont("Segoe UI", 11, QFont.Weight.Bold))

        role = QLabel("Cyber & Cloud")
        role.setStyleSheet("color:#94a3b8; font-size:11px;")

        info_layout.addWidget(name)
        info_layout.addWidget(role)

        profile_layout.addWidget(avatar)
        profile_layout.addLayout(info_layout)

        right_layout.addWidget(profile_card)
        right_layout.addSpacing(15)

        # Statistics Section
        statistics = QLabel("Statistics")
        statistics.setFont(QFont("Segoe UI", 8, QFont.Weight.Bold))
        #placeholder.setStyleSheet("color:white; font-size:11px;")
        right_layout.addWidget(statistics)

        right_layout.addStretch()

        # For adding widgets to the sidebars
        main_layout.addWidget(left_sidebar)
        main_layout.addWidget(content, 1)   
        main_layout.addWidget(right_sidebar)





