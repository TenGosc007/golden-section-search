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

    def reset(self):
        """Function clears canvas."""
        self.figure.clear()
        self.canvas.draw()

    def plot(self):
        """Function plots chart."""
        x1 = self.window.x1_range_input1.text()
        x2 = self.window.x1_range_input2.text()

        if not (x1 and x2):
            self.window.create_error_message('Jedno z wymaganych pól nie jest wypełnione!')
        else:
            ax = self.figure.gca(projection='3d')

            x_surf = np.arange(float(x1), float(x2), abs(float(x2) - float(x1)) / 50)
            y_surf = np.arange(float(x1), float(x2), abs(float(x2) - float(x1)) / 50)
            x_surf, y_surf = np.meshgrid(x_surf, y_surf)

            z_surf = np.zeros((len(x_surf), len(y_surf)))
            for i in range(len(x_surf[0])):
                for j in range(len(y_surf[0])):
                    z_surf[i, j] = self.math_interpreter.calculate([x_surf[0, i], y_surf[j, 0]])

            ax.plot_surface(x_surf, y_surf, z_surf, rstride=1, cstride=1, cmap='viridis_r', alpha=.5)
            z_min = np.amin(z_surf)
            size = abs(float(x2) - float(x1)) / 50
            xx, yy = self.window.algorithm.min_value
            zz = self.math_interpreter.calculate([xx, yy])
            p = Ellipse((xx, yy), size, size, color='r')
            ax.add_patch(p)
            art3d.pathpatch_2d_to_3d(p, z=zz, zdir="z")

            ax.contour(x_surf, y_surf, z_surf, zdir='z', offset=z_min, cmap='viridis_r')
            ax.set_xlabel('x1')
            ax.set_ylabel('x2')
            ax.set_zlabel('y')

            self.canvas.draw()
