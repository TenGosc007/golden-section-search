import numpy as np
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure
from matplotlib.patches import Ellipse
from mpl_toolkits.mplot3d import art3d


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

        ax.plot_surface(x_surf, y_surf, z_surf, rstride=1, cstride=1, cmap='viridis_r', alpha=.9)  # plot a 3d surface plot

        width, height = abs(x2 - x1) / 50, abs(y2 - y1) / 50
        p = Ellipse((x_surf[0, 10], y_surf[10, 0]), width, height, color='r')
        ax.add_patch(p)
        art3d.pathpatch_2d_to_3d(p, z=z_surf[10, 10], zdir="z")

        ax.set_xlabel('x1 label')
        ax.set_ylabel('x2 label')
        ax.set_zlabel('y label')

        self.canvas.draw()
