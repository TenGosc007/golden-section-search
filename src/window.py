from PyQt5 import QtCore
from PyQt5.QtWidgets import QMainWindow, QLabel, QPushButton, QComboBox, QLineEdit, QTextBrowser, QMessageBox

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
        function_list = self.get_template_function_list()
        self.func_label = self.create_label(20, 20, 'Funkcja wejściowa y')
        self.func_combo_box = self.create_combobox(20, 45, 500, 25, function_list)

        self.stop_criterion_label = self.create_label(20, 80, 'Kryterium stopu')
        stop_criterion_list = ['dla x: ||x\u2099 - x\u2099 \u208B \u2081x|| \u2264 \u03B5',
                               'dla f(x): |f(x\u2099) - f(x\u2099 \u208B \u2081)| \u2264 \u03B5',
                               'Liczba iteracji']
        self.stop_criterion_combo_box = self.create_combobox(20, 105, 400, 25, stop_criterion_list, editable=False)
        self.iteration_input = self.create_input(430, 105, 90, 25, enabled=False)
        self.stop_criterion_combo_box.currentIndexChanged.connect(self.enable_iterations_input)

        self.search_range_label = self.create_label(20, 140, 'Przedziały poszukiwań')

        self.x1_label = self.create_label(20, 165, 'Dla x1:')
        self.x1_a_label = self.create_label(100, 165, 'a = ')
        self.x1_a_input = self.create_input(130, 165, 100, 25)
        self.x1_b_label = self.create_label(250, 165, 'b = ')
        self.x1_b_input = self.create_input(280, 165, 100, 25)

        self.x2_label = self.create_label(20, 200, 'Dla x2:')
        self.x2_a_label = self.create_label(100, 200, 'a = ')
        self.x2_a_input = self.create_input(130, 200, 100, 25)
        self.x2_b_label = self.create_label(250, 200, 'b = ')
        self.x2_b_input = self.create_input(280, 200, 100, 25)

        self.x3_label = self.create_label(20, 235, 'Dla x3:')
        self.x3_a_label = self.create_label(100, 235, 'a = ')
        self.x3_a_input = self.create_input(130, 235, 100, 25)
        self.x3_b_label = self.create_label(250, 235, 'b = ')
        self.x3_b_input = self.create_input(280, 235, 100, 25)

        self.x4_label = self.create_label(20, 270, 'Dla x4:')
        self.x4_a_label = self.create_label(100, 270, 'a = ')
        self.x4_a_input = self.create_input(130, 270, 100, 25)
        self.x4_b_label = self.create_label(250, 270, 'b = ')
        self.x4_b_input = self.create_input(280, 270, 100, 25)

        self.x5_label = self.create_label(20, 305, 'Dla x5:')
        self.x5_a_label = self.create_label(100, 305, 'a = ')
        self.x5_a_input = self.create_input(130, 305, 100, 25)
        self.x5_b_label = self.create_label(250, 305, 'b = ')
        self.x5_b_input = self.create_input(280, 305, 100, 25)

        self.prompter = self.create_prompter(20, Config.APP_HEIGHT - 320, 500, 300)

        self.func_button = self.create_button(170, 355, 200, 25, 'Wyświetl', self.print_on_prompter, auto_size=False)

    def create_label(self, x, y, text):
        """Function creates label on the app window."""
        label = QLabel(self)
        label.setGeometry(QtCore.QRect(x, y, 0, 0))
        label.setText(text)
        label.adjustSize()
        return label

    def create_button(self, x, y, width, height, text, function, auto_size=True):
        """Function creates button on the app window."""
        button = QPushButton(self)
        button.setGeometry(QtCore.QRect(x, y, width, height))
        button.setText(text)
        if auto_size:
            button.adjustSize()
        button.clicked.connect(function)
        return button

    def create_combobox(self, x, y, width, height, function_list=None, editable=True):
        """Function creates combo box for entering functions."""
        combo_box = QComboBox(self)
        combo_box.setGeometry(QtCore.QRect(x, y, width, height))
        combo_box.setEditable(editable)
        if function_list:
            if editable:
                combo_box.addItem('')
            for item in function_list:
                combo_box.addItem(item)
        return combo_box

    def create_input(self, x, y, width, height, enabled=True):
        """Function creates input."""
        input_field = QLineEdit(self)
        input_field.setGeometry(QtCore.QRect(x, y, width, height))
        input_field.setEnabled(enabled)
        return input_field

    def create_prompter(self, x, y, width, height):
        """Function creates prompter to display all app states."""
        prompter = QTextBrowser(self)
        prompter.setGeometry(QtCore.QRect(x, y, width, height))
        return prompter

    def create_error_message(self, text):
        """Function creates error message box and displays it."""
        msg = QMessageBox(self)
        msg.setIcon(QMessageBox.Critical)
        msg.setText('\n' + text)
        msg.setWindowTitle('Error')
        msg.exec_()

    def get_template_function_list(self):
        """Function returns list of template functions."""
        return self.config.TEMPLATE_FUNCTIONS

    def enable_iterations_input(self):
        """Function enable iterations input when iteration number is set as stop criterion."""
        if self.stop_criterion_combo_box.currentText() == 'Liczba iteracji':
            self.iteration_input.setEnabled(True)
        else:
            self.iteration_input.setEnabled(False)

    def print_on_prompter(self):
        """Function changes text to function in combo_box"""
        function = str(self.func_combo_box.currentText())
        stop_criterion = str(self.stop_criterion_combo_box.currentText())
        x1a, x1b = str(self.x1_a_input.text()), str(self.x1_b_input.text())
        x2a, x2b = str(self.x2_a_input.text()), str(self.x2_b_input.text())
        x3a, x3b = str(self.x3_a_input.text()), str(self.x3_b_input.text())
        x4a, x4b = str(self.x4_a_input.text()), str(self.x4_b_input.text())
        x5a, x5b = str(self.x5_a_input.text()), str(self.x5_b_input.text())

        if stop_criterion == 'Liczba iteracji':
            stop_criterion += f' L = {self.iteration_input.text()}'

        if not function or stop_criterion == 'Liczba iteracji L = ':
            self.create_error_message('Jedno z wymaganych pól nie jest wypełnione!')
        else:
            string = f'Funkcja wejściowa:\ny = {function}\n\n' \
                     f'Kryterium stopu:\n{stop_criterion}\n\n' \
                     f'Przedziały poszukiwań:\n' \
                     f'Dla x1: a={x1a}, b={x1b}\n' \
                     f'Dla x2: a={x2a}, b={x2b}\n' \
                     f'Dla x3: a={x3a}, b={x3b}\n' \
                     f'Dla x4: a={x4a}, b={x4b}\n' \
                     f'Dla x5: a={x5a}, b={x5b}'
            self.prompter.setText(string)
