#coding=utf8

from mpl_toolkits.mplot3d.axes3d import Axes3D
import matplotlib.pyplot as plt

"""
      (1) matplotlib must be installed
      (2) http://matplotlib.org/devdocs/gallery.html
"""

# imports specific to the plots in this example
import numpy as np
from matplotlib import cm
from mpl_toolkits.mplot3d.axes3d import get_test_data

def test3d():
    # Twice as wide as it is tall.
    fig = plt.figure(figsize=plt.figaspect(0.5))

    #---- First subplot
    ax = fig.add_subplot(1, 2, 1, projection='3d')
    X = np.arange(-5, 5, 0.25)
    Y = np.arange(-5, 5, 0.25)
    X, Y = np.meshgrid(X, Y)
    R = np.sqrt(X**2 + Y**2)
    Z = np.sin(R)
    surf = ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap=cm.coolwarm,
                           linewidth=0, antialiased=False)
    ax.set_zlim3d(-1.01, 1.01)

    fig.colorbar(surf, shrink=0.5, aspect=10)

    #---- Second subplot
    ax = fig.add_subplot(1, 2, 2, projection='3d')
    X, Y, Z = get_test_data(0.05)
    ax.plot_wireframe(X, Y, Z, rstride=10, cstride=10)

    plt.show()

def testDynamic():

    fig = plt.figure()
    ax = fig.add_subplot(1,1,1)

    #画一批背景散点作为对照，该部分可以省略
    x_data = np.linspace(-1,1,300)[:, np.newaxis]
    noise = np.random.normal(0, 0.05, x_data.shape)
    y_data = np.square(x_data) - 0.5 + noise
    ax.scatter(x_data, y_data)

    plt.ion()                   #默认情况下调用show后程序pause，但是调用此方法不pause
    plt.show()
    for i in range(1,10000):
        try:
            ax.lines.remove(lines[0])
        except Exception:
            pass
        # plot the prediction
        x_data = np.linspace(-1,1,300)[:, np.newaxis]
        noise = np.random.normal(0, 0.2, x_data.shape)
        y_data = np.square(x_data) - 0.5 + noise
        lines = ax.plot(x_data, y_data, 'r-', lw=3)
        plt.pause(0.2)

def baseTest():
    s0 = np.arange(-500,500,1)
    s1 = np.random.randn(1000)
    s2 = np.random.randn(1000)/np.sqrt(1000)

    plt.scatter(s0, s1)
    plt.show()

if __name__=='__main__':
    # testDynamic()
    baseTest()