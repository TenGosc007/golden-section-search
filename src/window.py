from PyQt5 import QtCore
from PyQt5.QtWidgets import QMainWindow, QLabel, QPushButton, QComboBox

from src.config import Config


class Window(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.config = Config()
        self.setObjectName('window')
        self.setGeometry(self.config.X_POS, self.config.Y_POS, self.config.APP_WIDTH, self.config.APP_HEIGHT)
        self.setWindowTitle('Golden Section Search')
        self.init_ui()

    def init_ui(self):
        """Function initializes user interface."""
        self.func_label = self.create_label(20, 20, 'Funkcja wejściowa f(x)')
        function_list = self.get_template_function_list()
        self.func_combo_box = self.create_combobox(20, 45, 500, 25, function_list)
        self.func_button = self.create_button(530, 45, 0, 25, 'Wyświetl funkcje', self.print_function)
        self.print_label = self.create_label(20, 80, '')

    def create_label(self, x, y, text):
        """Function creates label on the app window."""
        label = QLabel(self)
        label.setGeometry(QtCore.QRect(x, y, 0, 0))
        label.setText(text)
        label.adjustSize()
        return label

    def create_button(self, x, y, width, height, text, function):
        """Function creates button on the app window."""
        button = QPushButton(self)
        button.setGeometry(QtCore.QRect(x, y, width, height))
        button.setText(text)
        button.adjustSize()
        button.clicked.connect(function)
        return button

    def create_combobox(self, x, y, width, height, function_list=None):
        """Function creates combo box for entering functions."""
        combo_box = QComboBox(self)
        combo_box.setGeometry(QtCore.QRect(x, y, width, height))
        combo_box.setEditable(True)
        if function_list:
            combo_box.addItem('')
            for item in function_list:
                combo_box.addItem(item)
        return combo_box

    def get_template_function_list(self):
        """Function returns list of template functions."""
        return self.config.TEMPLATE_FUNCTIONS

    def print_function(self):
        """Function changes text to function in combo_box"""
        function = str(self.func_combo_box.currentText())
        self.print_label.setText(function)
        self.print_label.adjustSize()
