from random import random

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar

from matplotlib.figure import Figure


class PlotField:
    def __init__(self, window):
        self.window = window
        self.figure = Figure()
        self.canvas = FigureCanvas(self.figure)
        self.toolbar = NavigationToolbar(self.canvas, self.window)

    def plot(self):
        """Plot some random stuff."""
        data = [random() for _ in range(10)]
        ax = self.figure.add_subplot(111)
        ax.clear()
        ax.plot(data, '*-')
        self.canvas.draw()
