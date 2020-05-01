from PyQt5 import QtCore
from PyQt5.QtWidgets import QMainWindow, QLabel, QPushButton, QComboBox, QLineEdit, QTextBrowser, QMessageBox, QWidget, \
    QGridLayout

from src.algorithm import Algorithm
from src.config import Config
from src.math_interpreter import MathInterpreter
from src.plot_field import PlotField
from src.utils import example_function_n5


class Window(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.config = Config()
        self.setObjectName('window')
        self.setGeometry(self.config.X_POS, self.config.Y_POS, self.config.APP_WIDTH, self.config.APP_HEIGHT)
        self.setWindowTitle('Golden Section Search')
        self.grid_cols = 10
        self.grid_rows = 30
        self.create_grid_layout()
        self.init_ui()
        self.init_chart_field()

    def create_grid_layout(self):
        self.grid_layout_widget_left = QWidget(self)
        self.grid_layout_widget_left.setGeometry(QtCore.QRect(0, 0, self.config.APP_WIDTH / 2, self.config.APP_HEIGHT))
        self.grid_layout_widget_left.setObjectName('grid_layout_widget_left')
        self.grid_layout_left = QGridLayout(self.grid_layout_widget_left)
        self.grid_layout_left.setContentsMargins(10, 10, 10, 10)
        self.grid_layout_left.setObjectName('grid_layout_left')

        self.grid_layout_widget_right = QWidget(self)
        self.grid_layout_widget_right.setGeometry(
            QtCore.QRect(self.config.APP_WIDTH / 2, 0, self.config.APP_WIDTH / 2, self.config.APP_HEIGHT))
        self.grid_layout_widget_right.setObjectName('grid_layout_widget_right')
        self.grid_layout_right = QGridLayout(self.grid_layout_widget_right)
        self.grid_layout_right.setContentsMargins(10, 10, 10, 10)
        self.grid_layout_right.setObjectName('grid_layout_right')

    def init_ui(self):
        """Function initializes user interface."""
        function_list = self.get_template_function_list()
        self.func_label = self.create_label(self.grid_layout_widget_left, self.grid_layout_left, 0, 0, 1, 10,
                                            'Funkcja wejściowa y')
        self.func_combo_box = self.create_combobox(self.grid_layout_widget_left, self.grid_layout_left, 1, 0, 1, 10,
                                                   function_list)

        self.stop_criterion_label = self.create_label(self.grid_layout_widget_left, self.grid_layout_left, 2, 0, 1, 10,
                                                      'Kryterium stopu')
        stop_criterion_list = ['dla x: ||x\u2099 - x\u2099 \u208B \u2081|| \u2264 \u03B5',
                               'dla f(x): |f(x\u2099) - f(x\u2099 \u208B \u2081)| \u2264 \u03B5',
                               'Liczba iteracji']
        self.stop_criterion_combo_box = self.create_combobox(self.grid_layout_widget_left, self.grid_layout_left, 3, 0,
                                                             1, 8,
                                                             stop_criterion_list, editable=False)
        self.iteration_input = self.create_input(self.grid_layout_widget_left, self.grid_layout_left, 3, 8, 1, 2,
                                                 enabled=False)
        self.stop_criterion_combo_box.currentIndexChanged.connect(self.enable_iterations_input)

        self.search_range_label = self.create_label(self.grid_layout_widget_left, self.grid_layout_left, 4, 0, 1, 10,
                                                    'Przedziały poszukiwań')

        self.x1_label = self.create_label(self.grid_layout_widget_left, self.grid_layout_left, 5, 0, 1, 2, 'Dla x1:')
        self.x1_a_label = self.create_label(self.grid_layout_widget_left, self.grid_layout_left, 5, 1, 1, 1,
                                            '    x\u2080 = ')
        self.x1_a_input = self.create_input(self.grid_layout_widget_left, self.grid_layout_left, 5, 2, 1, 2)
        self.x1_b_label = self.create_label(self.grid_layout_widget_left, self.grid_layout_left, 5, 4, 1, 1,
                                            '     d = ')
        self.x1_b_input = self.create_input(self.grid_layout_widget_left, self.grid_layout_left, 5, 5, 1, 2)

        self.x2_label = self.create_label(self.grid_layout_widget_left, self.grid_layout_left, 6, 0, 1, 2, 'Dla x2:')
        self.x2_a_label = self.create_label(self.grid_layout_widget_left, self.grid_layout_left, 6, 1, 1, 1,
                                            '    x\u2080 = ')
        self.x2_a_input = self.create_input(self.grid_layout_widget_left, self.grid_layout_left, 6, 2, 1, 2)
        self.x2_b_label = self.create_label(self.grid_layout_widget_left, self.grid_layout_left, 6, 4, 1, 1,
                                            '     d = ')
        self.x2_b_input = self.create_input(self.grid_layout_widget_left, self.grid_layout_left, 6, 5, 1, 2)

        self.x3_label = self.create_label(self.grid_layout_widget_left, self.grid_layout_left, 7, 0, 1, 2, 'Dla x3:')
        self.x3_a_label = self.create_label(self.grid_layout_widget_left, self.grid_layout_left, 7, 1, 1, 1,
                                            '    x\u2080 = ')
        self.x3_a_input = self.create_input(self.grid_layout_widget_left, self.grid_layout_left, 7, 2, 1, 2)
        self.x3_b_label = self.create_label(self.grid_layout_widget_left, self.grid_layout_left, 7, 4, 1, 1,
                                            '     d = ')
        self.x3_b_input = self.create_input(self.grid_layout_widget_left, self.grid_layout_left, 7, 5, 1, 2)

        self.x4_label = self.create_label(self.grid_layout_widget_left, self.grid_layout_left, 8, 0, 1, 2, 'Dla x4:')
        self.x4_a_label = self.create_label(self.grid_layout_widget_left, self.grid_layout_left, 8, 1, 1, 1,
                                            '    x\u2080 = ')
        self.x4_a_input = self.create_input(self.grid_layout_widget_left, self.grid_layout_left, 8, 2, 1, 2)
        self.x4_b_label = self.create_label(self.grid_layout_widget_left, self.grid_layout_left, 8, 4, 1, 1,
                                            '     d = ')
        self.x4_b_input = self.create_input(self.grid_layout_widget_left, self.grid_layout_left, 8, 5, 1, 2)

        self.x5_label = self.create_label(self.grid_layout_widget_left, self.grid_layout_left, 9, 0, 1, 2, 'Dla x5:')
        self.x5_a_label = self.create_label(self.grid_layout_widget_left, self.grid_layout_left, 9, 1, 1, 1,
                                            '    x\u2080 = ')
        self.x5_a_input = self.create_input(self.grid_layout_widget_left, self.grid_layout_left, 9, 2, 1, 2)
        self.x5_b_label = self.create_label(self.grid_layout_widget_left, self.grid_layout_left, 9, 4, 1, 1,
                                            '     d = ')
        self.x5_b_input = self.create_input(self.grid_layout_widget_left, self.grid_layout_left, 9, 5, 1, 2)

        self.tau_label = self.create_label(self.grid_layout_widget_left, self.grid_layout_left, 10, 1, 1, 1,
                                           '     \u03c4 = ')
        self.tau_input = self.create_input(self.grid_layout_widget_left, self.grid_layout_left, 10, 2, 1, 1, text='1')

        self.epsilon_label = self.create_label(self.grid_layout_widget_left, self.grid_layout_left, 10, 3, 1, 1,
                                               '     \u03b5 = ')
        self.epsilon_input = self.create_input(self.grid_layout_widget_left, self.grid_layout_left, 10, 4, 1, 1,
                                               text='0.001')

        self.func_button = self.create_button(self.grid_layout_widget_left, self.grid_layout_left, 11, 2, 1, 6,
                                              'Znajdź minimum',
                                              self.run_algorithm)

        self.prompter = self.create_prompter(self.grid_layout_widget_left, self.grid_layout_left, 12, 0, 15, 10)

    def init_chart_field(self):
        """Function initializes chart inputs and chart field."""
        self.plot_field = PlotField(self)
        self.x1_range_label = self.create_label(self.grid_layout_widget_right, self.grid_layout_right, 0, 4, 1, 6,
                                                'Rysunek warstwic dla n = 2')
        self.grid_layout_right.addWidget(self.plot_field.toolbar, 1, 0, 1, 10)
        self.grid_layout_right.addWidget(self.plot_field.canvas, 2, 0, 1, 10)

        self.x1_range_label = self.create_label(self.grid_layout_widget_right, self.grid_layout_right, 3, 0, 1, 1,
                                                '        Zakres x1:')
        self.x1_range_input1 = self.create_input(self.grid_layout_widget_right, self.grid_layout_right, 3, 2, 1, 1,
                                                 enabled=False, text='0')
        self.x1_range_input2 = self.create_input(self.grid_layout_widget_right, self.grid_layout_right, 3, 4, 1, 1,
                                                 enabled=False, text='1')

        self.x2_range_label = self.create_label(self.grid_layout_widget_right, self.grid_layout_right, 4, 0, 1, 2,
                                                '        Zakres x2:')
        self.x2_range_input1 = self.create_input(self.grid_layout_widget_right, self.grid_layout_right, 4, 2, 1, 1,
                                                 enabled=False, text='0')
        self.x2_range_input2 = self.create_input(self.grid_layout_widget_right, self.grid_layout_right, 4, 4, 1, 1,
                                                 enabled=False, text='1')

        self.draw_button = self.create_button(self.grid_layout_widget_right, self.grid_layout_right, 5, 0, 1, 10,
                                              'Rysuj',
                                              self.plot_field.plot, enabled=False)

    def create_label(self, widget, layout, row, cell, height, width, text):
        """Function creates label on the app window."""
        label = QLabel(widget)
        label.setText(text)
        label.setFixedSize(((self.config.APP_WIDTH - 20) / self.grid_cols) * width,
                           ((self.config.APP_HEIGHT - 20) / self.grid_rows) * height)
        layout.addWidget(label, row, cell, height, width)
        return label

    def create_button(self, widget, layout, row, cell, height, width, text, function, enabled=True):
        """Function creates button on the app window."""
        button = QPushButton(widget)
        button.setText(text)
        button.clicked.connect(function)
        button.setFixedSize((((self.config.APP_WIDTH / 2) - 20) / self.grid_cols) * width,
                            ((self.config.APP_HEIGHT - 20) / self.grid_rows) * height)
        layout.addWidget(button, row, cell, height, width)
        button.setEnabled(enabled)
        return button

    def create_combobox(self, widget, layout, row, cell, height, width, function_list=None, editable=True):
        """Function creates combo box for entering functions."""
        combo_box = QComboBox(widget)
        combo_box.setEditable(editable)
        if function_list:
            if editable:
                combo_box.addItem('')
            for item in function_list:
                combo_box.addItem(item)
        combo_box.setFixedSize((((self.config.APP_WIDTH / 2) - 20) / self.grid_cols) * width,
                               ((self.config.APP_HEIGHT - 20) / self.grid_rows) * height)
        layout.addWidget(combo_box, row, cell, height, width)
        return combo_box

    def create_input(self, widget, layout, row, cell, height, width, enabled=True, text=None):
        """Function creates input."""
        input_field = QLineEdit(widget)
        input_field.setEnabled(enabled)
        if text:
            input_field.setText(text)
        input_field.setFixedSize((((self.config.APP_WIDTH / 2) - 20) / self.grid_cols) * width,
                                 ((self.config.APP_HEIGHT - 20) / self.grid_rows) * height)
        layout.addWidget(input_field, row, cell, height, width)
        return input_field

    def create_prompter(self, widget, layout, row, cell, height, width):
        """Function creates prompter to display all app states."""
        prompter = QTextBrowser(widget)
        prompter.setFixedSize((((self.config.APP_WIDTH / 2) - 20) / self.grid_cols) * width,
                              ((self.config.APP_HEIGHT - 20) / self.grid_rows) * height)
        layout.addWidget(prompter, row, cell, height, width)
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

    def enable_drawing_chart(self, variables_amount):
        if variables_amount == 2:
            self.x1_range_input1.setEnabled(True)
            self.x1_range_input2.setEnabled(True)
            self.x2_range_input1.setEnabled(True)
            self.x2_range_input2.setEnabled(True)
            self.draw_button.setEnabled(True)

    def run_algorithm(self):
        """Function changes text to function in combo_box"""
        function = str(self.func_combo_box.currentText())
        stop_criterion = str(self.stop_criterion_combo_box.currentText())
        x1a, x1b = float(self.x1_a_input.text() or 0), float(self.x1_b_input.text() or 1)
        x2a, x2b = float(self.x2_a_input.text() or 0), float(self.x2_b_input.text() or 1)
        x3a, x3b = float(self.x3_a_input.text() or 0), float(self.x3_b_input.text() or 1)
        x4a, x4b = float(self.x4_a_input.text() or 0), float(self.x4_b_input.text() or 1)
        x5a, x5b = float(self.x5_a_input.text() or 0), float(self.x5_b_input.text() or 1)
        tau = float(self.tau_input.text())
        epsilon = float(self.epsilon_input.text())

        if stop_criterion == 'Liczba iteracji':
            stop_criterion += f' L = {self.iteration_input.text()}'

        vars_value = [1.0, 0.0, 0.0, 5.0]
        self.math_interpreter = MathInterpreter(function)
        self.plot_field.math_interpreter = self.math_interpreter
        self.enable_drawing_chart(self.math_interpreter.variables_amount())

        if not function or stop_criterion == 'Liczba iteracji L = ':
            self.create_error_message('Jedno z wymaganych pól nie jest wypełnione!')
        else:
            input_info = f'------------------------ Dane wejściowe ------------------------\n\n' \
                         f'Funkcja wejściowa:\ny = {function}\n\n' \
                         f'Zmienne w funkcji:\n {self.math_interpreter.get_variables()}\n\n' \
                         f'Liczba zmiennych:\nn = {self.math_interpreter.variables_amount()}\n\n' \
                         f'Wynik funkcji wyjściowej:\ny = {self.math_interpreter.calculate(vars_value)}\n\n' \
                         f'Token list: {self.math_interpreter.get_token_list()}\n\n'\
                         f'Wynik funkcji wyjściowej2:\ny = {self.math_interpreter.calculate([2,1,-2,0])}\n\n' \
                         f'Kryterium stopu:\n{stop_criterion}\n\n' \
                         f'Przedziały poszukiwań:\n' \
                         f'Dla x1: x\u2080={x1a}, d={x1b}\n' \
                         f'Dla x2: x\u2080={x2a}, d={x2b}\n' \
                         f'Dla x3: x\u2080={x3a}, d={x3b}\n' \
                         f'Dla x4: x\u2080={x4a}, d={x4b}\n' \
                         f'Dla x5: x\u2080={x5a}, d={x5b}\n\n' \
                         f'\u03c4={tau}\n\u03b5={epsilon}\n'

            self.prompter.append(input_info)

            # TODO: function parser which returns n and function value evaluator
            # temporary
            function_evaluator = example_function_n5
            n = 5
            # a = [x1a, x2a, x3a, x4a, x5a]
            # b = [x1b, x2b, x3b, x4b, x5b]
            x0 = [0, 0, 0, 0, 0]  # temporary constant
            d = [1, 1, 1, 1, 1]
            stop = None  # temporary
            algorithm = Algorithm(x0, d, n, tau, epsilon, stop, function_evaluator, self.prompter)
            algorithm.find_minimum_value()
