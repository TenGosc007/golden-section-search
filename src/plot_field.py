from random import random

import numpy as np
from matplotlib import cm
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure


class PlotField:
    def __init__(self, window):
        self.window = window
        self.figure = Figure()
        self.canvas = FigureCanvas(self.figure)
        self.toolbar = NavigationToolbar(self.canvas, self.window)
        self.math_interpreter = None

    def plot(self):
        ax = self.figure.gca(projection='3d')

        x1 = float(self.window.x1_range_input1.text())
        x2 = float(self.window.x1_range_input2.text())
        y1 = float(self.window.x2_range_input1.text())
        y2 = float(self.window.x2_range_input2.text())

        x_surf = np.arange(x1, x2, abs(x2 - x1) / 50)
        y_surf = np.arange(y1, y2, abs(y2 - y1) / 50)
        x_surf, y_surf = np.meshgrid(x_surf, y_surf)

        z_surf = np.zeros((len(x_surf), len(y_surf)))
        for i in range(len(x_surf[0])):
            for j in range(len(y_surf[0])):
                z_surf[i, j] = self.math_interpreter.calculate([x_surf[0, i], y_surf[j, 0]]).value
        ax.plot_surface(x_surf, y_surf, z_surf, cmap=cm.hot)  # plot a 3d surface plot

        ax.scatter(x_surf[0, 10], y_surf[10, 0], z_surf[10, 10], s=20, c='b')
        ax.set_xlabel('x label')
        ax.set_ylabel('y label')
        ax.set_zlabel('z label')

        self.canvas.draw()
