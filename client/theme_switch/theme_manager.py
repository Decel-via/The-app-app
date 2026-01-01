from PyQt6.QtWidgets import QApplication


DARK_THEME = """
QWidget {
    background-color: #0f172a;
    color: white;
    font-family: 'Segoe UI';
}

/* Inputs */
QLineEdit {
    background-color: #1e293b;
    border-radius: 8px;
    padding: 10px;
    color: white;
    border: 1px solid #111827;
}

/* Buttons */
QPushButton {
    background-color: #1e293b;
    color: white;
    border-radius: 8px;
    padding: 10px;
    font-size: 15px;
    border: none;
}

QPushButton:hover {
    background-color: #334155;
}

/* Primary CTA button */
QPushButton#primaryButton {
    background-color: #2563eb;
    font-weight: 600;
}

QPushButton#primaryButton:hover {
    background-color: #1d4ed8;
}

/* Text link-style button */
QPushButton#linkButton {
    background-color: transparent;
    border: none;
    color: #60a5fa;
    padding: 0px;
    font-size: 14px;
    text-align: left;
}

QPushButton#linkButton:hover {
    color: #93c5fd;
    text-decoration: underline;
}

/* Muted labels */
QLabel#mutedLabel {
    color: white;
    font-size: 13px;
}

/* Card container */
QFrame#card {
    background-color: #020617;
    border-radius: 16px;
}

/* Password strength bar */
QFrame#passwordStrength {
    background-color: #16a34a;
    border-radius: 3px;
}

/* Dividers */
QFrame[frameShape="4"] {  /* QFrame.HLine */
    color: #1f2933;
}
"""

LIGHT_THEME = """
QWidget {
    background-color: #e5e7eb;
    color: #111827;
    font-family: 'Segoe UI';
}

/* Inputs */
QLineEdit {
    background-color: #ffffff;
    border-radius: 8px;
    padding: 10px;
    color: #111827;
    border: 1px solid #d1d5db;
}

/* Buttons */
QPushButton {
    background-color: #ffffff;
    color: #111827;
    border-radius: 8px;
    padding: 10px;
    font-size: 15px;
    border: 1px solid #d1d5db;
}

QPushButton:hover {
    background-color: #f3f4f6;
}

/* Primary CTA button */
QPushButton#primaryButton {
    background-color: #2563eb;
    color: white;
    border: none;
    font-weight: 600;
}

QPushButton#primaryButton:hover {
    background-color: #1d4ed8;
}

/* Text link-style button */
QPushButton#linkButton {
    background-color: transparent;
    border: none;
    color: #2563eb;
    padding: 0px;
    font-size: 14px;
    text-align: left;
}

QPushButton#linkButton:hover {
    color: #1d4ed8;
    text-decoration: underline;
}

/* Muted labels */
QLabel#mutedLabel {
    color: #6b7280;
    font-size: 13px;
}

/* Card container */
QFrame#card {
    background-color: #f9fafb;
    border-radius: 16px;
}

/* Password strength bar */
QFrame#passwordStrength {
    background-color: #16a34a;
    border-radius: 3px;
}

/* Dividers */
QFrame[frameShape="4"] {  /* QFrame.HLine */
    color: #e5e7eb;
}
"""


class ThemeManager:
    DARK = "dark"
    LIGHT = "light"

    def __init__(self, initial_theme: str = DARK):
        if initial_theme not in (self.DARK, self.LIGHT):
            initial_theme = self.DARK
        self.current_theme = initial_theme

    def apply(self) -> None:
        app = QApplication.instance()
        if not app:
            return

        if self.current_theme == self.DARK:
            app.setStyleSheet(DARK_THEME)
        else:
            app.setStyleSheet(LIGHT_THEME)

    def set_theme(self, theme: str) -> None:
        if theme not in (self.DARK, self.LIGHT):
            return
        self.current_theme = theme
        self.apply()

    def toggle(self) -> None:
        if self.current_theme == self.DARK:
            self.current_theme = self.LIGHT
        else:
            self.current_theme = self.DARK
        self.apply()
