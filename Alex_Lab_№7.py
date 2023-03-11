import numpy as np
import matplotlib.pyplot as plt


def plot3d():
    x = np.linspace(-3.14, 3.14)
    y = np.linspace(-1, 1)
    xs=np.sin(y)
    ys=np.sin(x)

    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.plot(xs, ys, marker='x')
    ax.bar([9.54, 9.64, 9.74, 9.84, 9.94, 10.04, 10.14, 10.24, 10.34], [4, 7, 8, 7, 12, 5, 4, 3, 0], width=0.1)
    plt.show()


if __name__ == '__main__':
    plot3d()
