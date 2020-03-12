import sys

from PyQt5.QtWidgets import QApplication

from src.window import Window


class Application:
    def __init__(self):
        self.app = QApplication(sys.argv)
        self.window = Window()

    def show_window(self):
        """Function shows application window."""
        self.window.show()
        sys.exit(self.app.exec_())

    def run(self):
        """Function starts the application."""
        self.show_window()
