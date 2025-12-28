
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QLabel, QPushButton,
    QVBoxLayout, QHBoxLayout, QFrame
)
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont
import os
import sys



class ModernDashboard(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Modern PyQt Dashboard")
        self.setMinimumSize(1000, 600)

        # Central widget
        central = QWidget()
        self.setCentralWidget(central)
        main_layout = QHBoxLayout(central)

        # Sidebar
        sidebar = QFrame()
        sidebar.setFixedWidth(220)
        sidebar.setStyleSheet("""
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

        sidebar_layout = QVBoxLayout(sidebar)
        title = QLabel("🚀 Dashboard")
        title.setStyleSheet("color: white;")
        title.setFont(QFont("Segoe UI", 18, QFont.Weight.Bold))
        sidebar_layout.addWidget(title)
        sidebar_layout.addSpacing(20)

        for name in ["Home", "Analytics", "Projects", "Settings"]:
            sidebar_layout.addWidget(QPushButton(name))

        sidebar_layout.addStretch()

        # Main content area
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

        # Cards section
        cards_layout = QHBoxLayout()
        for title_text, value in [("Active Users", "1,248"), ("Revenue", "£8,540"), ("Errors", "3")]:
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

        main_layout.addWidget(sidebar)
        main_layout.addWidget(content)

