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

def baseTest1():
    #散点图
    s0 = np.arange(-500,500,1)
    s2 = np.random.randn(1000)/np.sqrt(1000)

    plt.scatter(s0, s2)
    plt.show()

def baseTest2():
    #一条曲线, plot函数（常用）
    # Compute the x and y coordinates for points on a sine curve
    x = np.arange(0, 3 * np.pi, 0.1)
    y = np.sin(x)

    # Plot the points using matplotlib
    plt.plot(x, y)
    plt.show()  # You must call plt.show() to make graphics appear.

def baseTest3():
    #多条曲线，plot函数
    import numpy as np
    import matplotlib.pyplot as plt

    # Compute the x and y coordinates for points on sine and cosine curves
    x = np.arange(0, 3 * np.pi, 0.1)
    y_sin = np.sin(x)
    y_cos = np.cos(x)

    # Plot the points using matplotlib
    plt.plot(x, y_sin)
    plt.plot(x, y_cos)
    plt.xlabel('x axis label')
    plt.ylabel('y axis label')
    plt.title('Sine and Cosine')
    plt.legend(['Sine', 'Cosine'])
    plt.show()

def testSubplot():
    #You can plot different things in the same figure using the subplot function. Here is an example:
    import numpy as np
    import matplotlib.pyplot as plt

    # Compute the x and y coordinates for points on sine and cosine curves
    x = np.arange(0, 3 * np.pi, 0.1)
    y_sin = np.sin(x)
    y_cos = np.cos(x)

    # Set up a subplot grid that has height 2 and width 1,
    # and set the first such subplot as active.
    plt.subplot(2, 1, 1)

    # Make the first plot
    plt.plot(x, y_sin)
    plt.title('Sine')

    # Set the second subplot as active, and make the second plot.
    plt.subplot(2, 1, 2)
    plt.plot(x, y_cos)
    plt.title('Cosine')

    # Show the figure.
    plt.show()

def testImages():
    #You can use the imshow function to show images.
    import numpy as np
    from scipy.misc import imread, imresize
    import matplotlib.pyplot as plt

    img = imread('../resources/cat.jpg')
    print img.shape,img
    img_tinted = img * [1, 0.95, 0.9]

    # Show the original image
    plt.subplot(1, 2, 1)
    plt.imshow(img)

    # Show the tinted image
    plt.subplot(1, 2, 2)

    # A slight gotcha with imshow is that it might give strange results
    # if presented with data that is not uint8. To work around this, we
    # explicitly cast the image to uint8 before displaying it.
    plt.imshow(np.uint8(img_tinted))
    plt.show()

if __name__=='__main__':
    # testDynamic()
    testImages()