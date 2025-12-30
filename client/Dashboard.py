from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QLabel, QPushButton,
    QVBoxLayout, QHBoxLayout, QFrame,QToolButton, QMenu )

from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont,QAction
from PyQt6.QtWidgets import QComboBox
from PyQt6.QtCore import pyqtSignal
from PyQt6.QtGui import QCursor
from PyQt6.QtCore import QPoint




class Dashboard(QMainWindow):
    def __init__(self, go_back):
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

        
        #Task button
        task_button = QPushButton("Tasks")
        left_layout.addWidget(task_button)

        proj_button = QPushButton("Projects")
        left_layout.addWidget(proj_button)

        stat_button = QPushButton("Statistics")
        left_layout.addWidget(stat_button)

        settings_button = QPushButton("Settings")
        left_layout.addWidget(settings_button)


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

        # profile_box = QComboBox()
        # profile_box.addItems(["Profile", "Log Out"])
        #
        # #profile_box.activated.connect()
        #
        # profile_box.setStyleSheet("""
        #     QComboBox {
        #         background-color: #1e293b;
        #         color: white;
        #         border-radius: 8px;
        #         padding: 8px;
        #     }""")
        # profile_box.hide()  # hidden until needed
        #
        # #profile_layout is login
        #
        profile_layout = QHBoxLayout(profile_card)
        # Create dropdown menu
        menu = QMenu()

        # Add menu actions
        profile_action = QAction("Your profile", self)
        settings_action = QAction("Settings", self)
        logout_action = QAction("Sign out", self)

        # Connect signals
        profile_action.triggered.connect(lambda: print("Profile clicked"))
        settings_action.triggered.connect(lambda: print("Settings clicked"))
        logout_action.triggered.connect(lambda: print("Logged out"))

        menu.addAction(profile_action)
        menu.addAction(settings_action)
        menu.addSeparator()
        menu.addAction(logout_action)
        menu.hide()
        # Attach menu to profile button

        # qmenu background
        menu.setStyleSheet("""
            QMenu {
                background-color: #1e293b;
                color: white;
                border: 1px solid #374151;
                border-radius: 8px;
                padding: 1px;
            }
            QMenu::item {
                padding: 8px 24px;
                border-radius: 4px;
                color: white;
            }
            QMenu::item:selected {
                background-color: #374151;
            }  
        """)


        # Avatar
        avatar = ClickableLabel("👤")
        avatar.setFixedSize(55, 55)
        avatar.setAlignment(Qt.AlignmentFlag.AlignCenter)
        avatar.setStyleSheet("""
            QLabel {
                background-color: #3b82f6;
                border-radius: 27px;
                font-size: 18px;
                font-weight: bold;
            }
            QWidget:hover {
                background-color: #334155;
            }
        """)
        avatar.clicked.connect(lambda: menu.hide() if menu.isVisible() else menu.show())
        # Name + role
        info_layout = QVBoxLayout()
        name = QLabel("User")
        name.setFont(QFont("Segoe UI", 11, QFont.Weight.Bold))

        role = QLabel("Cyber & Cloud")
        role.setStyleSheet("color:#94a3b8; font-size:11px;")

        info_layout.addWidget(name)
        info_layout.addWidget(role)

        #profile_layout
        profile_layout.addWidget(avatar)
        profile_layout.addLayout(info_layout)
        profile_layout.addWidget(menu)


        right_layout.addWidget(profile_card)
        right_layout.addSpacing(15)

        # Statistics Section
        statistics = QLabel("Statistics")
        statistics.setFont(QFont("Segoe UI", 8, QFont.Weight.Bold))
        #placeholder.setStyleSheet("color:white; font-size:11px;")
        right_layout.addWidget(menu)
        right_layout.addWidget(statistics)



        right_layout.addStretch()

        # For adding widgets to the sidebars
        main_layout.addWidget(left_sidebar)
        main_layout.addWidget(content, 1)   
        main_layout.addWidget(right_sidebar)

        

class ClickableWidget(QWidget):
    clicked = pyqtSignal()

    def mousePressEvent(self, event):
        self.clicked.emit()
        super().mousePressEvent(event)

class ClickableLabel(QLabel):
    clicked = pyqtSignal()

    def mousePressEvent(self, event):
        self.clicked.emit()
        super().mousePressEvent(event)



