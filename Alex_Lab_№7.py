import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


def plot3d():
    x = np.linspace(-3.14, 3.14)
    y = np.linspace(-1, 1)
    xs=np.sin(y)
    ys=np.sin(x)

    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.plot(xs, ys, marker='x')
    plt.show()


if __name__ == '__main__':
    plot3d()
