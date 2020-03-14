from PyQt5.QtWidgets import QMainWindow, QLabel, QPushButton

from src.config import Config


class Window(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.config = Config()
        self.setGeometry(self.config.X_POS, self.config.Y_POS, self.config.APP_WIDTH, self.config.APP_HEIGHT)
        self.setWindowTitle('Golden Section Search')
        self.init_ui()

    def init_ui(self):
        """Function initializes user interface."""
        self.func_label = self.create_label('Enter function', 10, 10)
        self.func_button = self.create_button('Click this button!', 10, 50, self.clicked)

    def create_label(self, text, x_pos, y_pos):
        """Function create label on the app window."""
        label = QLabel(self)
        label.setText(text)
        label.move(x_pos, y_pos)
        return label

    def create_button(self, text, x_pos, y_pos, function):
        """Function create button on the app window."""
        button = QPushButton(self)
        button.setText(text)
        button.move(x_pos, y_pos)
        button.clicked.connect(function)
        return button

    def clicked(self):
        """Function change label text on the app window."""
        self.func_label.setText('New text')
        self.func_label.adjustSize()
