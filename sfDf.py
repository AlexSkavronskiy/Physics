import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

x = np.linspace(-5, 5, 100)
y = np.sin(x)

fig, ax = plt.subplots()

ax.plot(x, y,
        linestyle = '-',
        linewidth = 1,
        color = 'crimson')
plt.show()

def plot3d():
    np.random.seed(40)
    xs = np.linspace(0, 10, 20)
    ys = xs
    zs = np.sin(xs)

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.plot(xs, ys, zs, marker='x', c='red')
    plt.show()


if __name__ == '__main__':
    #start()
    #tableLoad()
    #hist()
    plot3d()