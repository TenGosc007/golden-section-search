import sys

from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel

from src.config import Config


class Application:
    def __init__(self):
        self.config = Config()

    def window(self):
        """Function sets up application window."""
        app = QApplication(sys.argv)
        win = QMainWindow()
        win.setGeometry(self.config.X_POS, self.config.Y_POS, self.config.APP_WIDTH, self.config.APP_HEIGHT)
        win.setWindowTitle('Golden Section Search')

        self.create_label(win, 'Enter function', 10, 10)

        win.show()
        sys.exit(app.exec_())

    @staticmethod
    def create_label(win, text, x_pos, y_pos):
        """Function create label on the app window."""
        label = QLabel(win)
        label.setText(text)
        label.move(x_pos, y_pos)

    def run(self):
        """Function starts the application."""
        self.window()
