import numpy as np
from matplotlib import cm
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure
from matplotlib.ticker import LinearLocator, FormatStrFormatter


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

        # make data
        x = np.arange(x1, x2, 0.1)
        y = np.arange(y1, y2, 0.1)
        x, y = np.meshgrid(x, y)

        z = np.zeros((len(x), len(y)))
        for i in range(len(x[0])):
            for j in range(len(y[0])):
                print('x', x[0][i])
                print('y', y[j][0])
                print('z', self.math_interpreter.calculate([x[0][i], y[j][0]]).value)

                z[i, j] = self.math_interpreter.calculate([x[0][i], y[j][0]]).value

        # plot the surface
        surf = ax.plot_surface(x, y, z, cmap=cm.coolwarm,
                               linewidth=0, antialiased=False)

        # add a color bar which maps values to colors
        self.figure.colorbar(surf, shrink=0.5, aspect=5)
        self.canvas.draw()
