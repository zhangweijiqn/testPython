# coding=utf8
# http://old.sebug.net/paper/books/scipydoc/numpy_intro.html
import numpy as np

# NumPy数组是一个多维数组对象，称为ndarray

#  numpy类型  #
# 名称	描述
# bool	用一个字节存储的布尔类型（True或False）
# inti	由所在平台决定其大小的整数（一般为int32或int64）
# int8	一个字节大小，-128 至 127
# int16	整数，-32768 至 32767
# int32	整数，-2 ** 31 至 2 ** 32 -1
# int64	整数，-2 ** 63 至 2 ** 63 - 1
# uint8	无符号整数，0 至 255
# uint16	无符号整数，0 至 65535
# uint32	无符号整数，0 至 2 ** 32 - 1
# uint64	无符号整数，0 至 2 ** 64 - 1
# float16	半精度浮点数：16位，正负号1位，指数5位，精度10位
# float32	单精度浮点数：32位，正负号1位，指数8位，精度23位
# float64或float	双精度浮点数：64位，正负号1位，指数11位，精度52位
# complex64	复数，分别用两个32位浮点数表示实部和虚部
# complex128或complex	复数，分别用两个64位浮点数表示实部和虚部

# 类型转换
float64(42)

# 创建数组
# 使用array函数创建时，参数必须是由方括号括起来的列表，而不能使用多个数值作为参数调用array
a = np.array([1, 2, 3, 4])
a.shape  # 数组的形状
a.dtype  # 数组的类型
a.ndim  # 数组的维度
a.size  # 数组的大小，也就是元素的个数
a.itemsize  # 数组中每个元素的字节大小

a.sum(axis=0)   # 计算每一列的和
a.max(axis=0) # 获取每一行的最大值
a.max() #获取所有元素的最大值
a.min(axis=0) # 计算每一列的最小值
a.transpose()
a.ravel() # 平坦化数组

# 可使用双重序列来表示二维的数组，三重序列表示三维数组，以此类推。
b = np.array([[1, 2, 3, 4], [4, 5, 6, 7], [7, 8, 9, 10]])
b.shape  # dtype('int64')
b.dtype  # (3, 4)
b.ndim  # 2
b.size  # 12
# 可以通过dtype参数在创建时指定元素类型
c = np.array([[1, 2, 3, 4], [4, 5, 6, 7], [7, 8, 9, 10]], dtype=np.float)

# 上面的例子都是先创建一个Python序列，然后通过array函数将其转换为数组,NumPy提供了很多专门用来创建数组的函数。
# 用函数zeros可创建一个全是0的数组,默认创建的数组类型(dtype)都是float64。参数为维度，用小括号括起来
d = np.zeros((3, 4))
# 用函数ones可创建一个全为1的数组
d = np.ones((2, 3, 4), dtype=np.int16)
# 函数empty创建一个内容随机并且依赖与内存状态的数组。
d = np.empty((2, 3))

# 产生一个长度为10，元素值为0-1的随机数的数组
x = np.random.rand(10)  # 产生一个长度为10，元素值为0-1的随机数的数组
# arange函数类似于python的range函数，通过指定开始值、终值和步长来创建一维数组，注意数组不包括终值
np.arange(0, 1, 0.1)  # array([ 0. ,  0.1,  0.2,  0.3,  0.4,  0.5,  0.6,  0.7,  0.8,  0.9])
np.arange(
    24)  # array([ 0,  1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12, 13, 14, 15, 16,17, 18, 19, 20, 21, 22, 23])
np.arange(7, dtype=np.uint16)
# linspace函数通过指定开始值、终值和元素个数来创建一维数组，可以通过endpoint关键字指定是否包括终值，缺省设置是包括终值
np.linspace(0, 1, 12)
# logspace函数和linspace类似，不过它创建等比数列，下面的例子产生1(10^0)到100(10^2)、有20个元素的等比数列
np.logspace(0, 2, 20)


# 此外，使用frombuffer, fromstring, fromfile等函数可以从字节序列创建数组
def func(i):
    return i % 4 + 1


np.fromfunction(func, (10,))  # shape=(10,)
# array([ 1.,  2.,  3.,  4.,  1.,  2.,  3.,  4.,  1.,  2.])

# 可以通过修改数组的shape属性，在保持数组元素个数不变的情况下，改变数组每个轴的长度。
b.shape = 4, 3
# 当某个轴的元素为-1时，将根据数组元素的个数自动计算此轴的长度
b.shape = 2, -1

# 使用数组的reshape方法，可以创建一个改变了尺寸的新数组，原数组的shape保持不变
d = b.reshape(4, 3)
# 数组b和d其实共享数据存储内存区域，因此修改其中任意一个数组的元素都会同时修改另外一个数组的内容：
a[1] = 100  # 将数组a的第一个元素改为100
b[0][0] = 10

# 存取元素,切片
# 用整数作为下标可以获取数组中的某个元素
a[0]
# 用范围作为下标获取数组的一个切片，包括a[3]不包括a[5]
a[3:5]
# 省略开始下标，表示从a[0]开始
a[:5]
# 下标可以使用负数，表示从数组后往前数
a[:-1]
# 使用x>0.5返回的布尔数组收集x中的元素，因此得到的结果是x中所有大于0.5的元素的数组
x[x > 0.5]
# 下标还可以用来修改元素的值
a[2:4] = 100, 101
a[1:-1:2]  # 范围中的第三个参数表示步长，2表示隔一个元素取一个元素
a[::-1]  # 省略范围的开始下标和结束下标，步长为-1，整个数组头尾颠倒
a[5:1:-2]  # 步长为负数时，开始下标必须大于结束下标
a[:]  # 省略开始结束下标，取所有元素的值
a[::]  # 省略开始结束下标及步长，取所有元素的值
a[: :-1] # 反转a
a[-1] # 最后一行，等同于a[-1,:]，-1是第一个轴，而缺失的认为是：，相当于整个
# 和Python的列表序列不同，通过下标范围获取的新的数组是原始数组的一个视图。它与原始数组共享同一块数据空间。
# 切片数组返回它的一个视图：
s = b[:, 1:3]
s[:] = 10  # b相应的值也跟着改变

# 使用整数序列,使用整数序列作为下标获得的数组不和原始数组共享数据空间。
x = np.arange(10, 0, -1)  # array([10,  9,  8,  7,  6,  5,  4,  3,  2,  1])
# 获取x中的下标为3, 3, 1, 8的4个元素，组成一个新的数组,下标可以是负数
x[[3, 3, 1, 8]]  # array([7, 7, 9, 2])
# 整数序列下标也可以用来修改元素的值
x[[3, 5, 1]] = -1, -2, -3

# 多维数组操作
m = np.arange(0, 60, 10).reshape(-1, 1) + np.arange(0, 6)
m[0, 2:5]
m[:, 2]
m[2:, 2:]

# 结构数组
persontype = np.dtype({
    'names': ['name', 'age', 'weight'],
    'formats': ['S32', 'i', 'f']})
a = np.array([("Zhang", 32, 75.5), ("Wang", 24, 65.2)],
             dtype=persontype)

# ufunc是universal function的缩写，它是一种能对数组的每个元素进行操作的函数。NumPy内置的许多ufunc函数都是在C语言级别实现的，因此它们的计算速度非常快。
x = np.linspace(0, 2 * np.pi, 10)
y = np.sin(x)
np.add(x, y)
# y = x1 + x2:	add(x1, x2 [, y])
# y = x1 - x2:	subtract(x1, x2 [, y])
# y = x1 * x2:	multiply (x1, x2 [, y])
# y = x1 / x2:	divide (x1, x2 [, y]), 如果两个数组的元素为整数，那么用整数除法
# y = x1 / x2:	true divide (x1, x2 [, y]), 总是返回精确的商
# y = x1 // x2:	floor divide (x1, x2 [, y]), 总是对返回值取整
# y = -x:	negative(x [,y])
# y = x1**x2:	power(x1, x2 [, y])
# y = x1 % x2:	remainder(x1, x2 [, y]), mod(x1, x2, [, y])

# 基本运算
a = np.array([20, 30, 40, 50])
b = np.arange(4)
c = a - b
b ** 2
10 * np.sin(a)
# 矩阵
A = np.array([[1, 1], [0, 1]])
B = np.array([[2, 0], [3, 4]])
C = A * B  # 逐个元素相乘
np.dot(A, B)  # 矩阵相乘
#  +=和*=用来更改已存在数组而不创建一个新的数组
A *= 3  #
B += A
# matrix矩阵运算
a = np.matrix([[1, 2, 3], [5, 5, 6], [7, 9, 9]])
a * a ** -1

# 文件存取
a = np.arange(0, 12)
a.shape = 3, 4
a.tofile("a.bin")
b = np.fromfile("a.bin", dtype=np.int64)  # 需要在读入的时候设置正确的dtype和shape才能保证数据一致
b.shape = 3, 4  # 按照a的shape修改b的shape

# numpy.load和numpy.save函数以NumPy专用的二进制类型保存数据，这两个函数会自动处理元素类型和shape等信息,numpy.save输出的文件很难和其它语言编写的程序读入
np.save("a.npy", a)
c = np.load("a.npy")

# 将多个数组保存到一个文件中的话，可以使用numpy.savez函数。savez函数的第一个参数是文件名，其后的参数都是需要保存的数组
np.savez("a.npz", a, b, sin_array=c)
# 可以使用关键字参数为数组起一个名字，非关键字参数传递的数组会自动起名为arr_0, arr_1, ...。
# savez函数输出的是一个压缩文件(扩展名为npz)，其中每个文件都是一个save函数保存的npy文件，文件名对应于数组名。
r = np.load("a.npz")
r["arr_0"]  # 数组a
r["arr_1"]  # 数组b
r["sin_array"]  # 数组c

# 使用numpy.savetxt和numpy.loadtxt可以读写1维和2维的数组
np.savetxt("a.txt", a)  # 缺省按照'%.18e'格式保存数据，以空格分隔
np.loadtxt("a.txt")
np.savetxt("a.txt", a, fmt="%d", delimiter=",")  # 改为保存为整数，以逗号分隔
np.loadtxt("a.txt", delimiter=",")  # 读入的时候也需要指定逗号分隔

# 可以传递已经打开的文件对象，例如对于load和save函数来说，如果使用文件对象的话，可以将多个数组储存到一个npy文件中
a = np.arange(8)
b = np.add.accumulate(a)
c = a + b
f = file("a.npy", "wb")
np.save(f, a)  # 顺序将a,b,c保存进文件对象f
np.save(f, b)
np.save(f, c)
f.close()
f = file("a.npy", "rb")
np.load(f)  # 顺序从文件对象f中读取内容
np.load(f)
np.load(f)


# 复制
a = np.arange(12)
b = a
b is a  # True
# 不同的数组对象分享同一个数据。视图方法创造一个新的数组对象指向同一数据。
c = a.view()
c is a  # False
c.base is a  # True,c是a持有数据的镜像
# 深复制
d = a.copy()  # 这个复制方法完全复制数组和它的数据。

sizes = [4, 6, 1]
print sizes[:-1]
print sizes[1:]
# print sizes[1,:]
print zip(sizes[:-1], sizes[1:])
print np.random.randn(
    10)  # Return a sample (or samples) from the "standard normal" distribution. parameters are dimension(均值为0,方差为1的高斯分布)
print np.random.randn(2, 3)
np.random.rand()  # Random values in a given shape.

weights = [np.random.randn(y, x) for x, y in zip(sizes[:-1], sizes[1:])]
# 输入d1输出d2的层，权重为矩阵，维度为d1*d2: 	 d1*(d1,d2) => d2
# 利用切片操作巧妙的将相邻2个组合到一起。sizes[:-1]除最后一个元素之外的序列，sizes[1:]除第0个元素之外的序列。
print weights
biases = [np.random.randn(y, 1) for y in sizes[1:]]
# biases大小为输入的大小，输入层除外。
print biases

weights = [np.random.randn(y, x) / np.sqrt(x) for x, y in zip(sizes[:-1], sizes[1:])]
print weights
