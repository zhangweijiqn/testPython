#coding=utf8
# http://old.sebug.net/paper/books/scipydoc/numpy_intro.html
import numpy as np

#创建数组
a = np.array([1, 2, 3, 4])
a.shape #数组的大小
a.dtype #数组的类型
b = np.array([[1, 2, 3, 4],[4, 5, 6, 7], [7, 8, 9, 10]])
b.shape #dtype('int64')
b.dtype #(3, 4)
#可以通过dtype参数在创建时指定元素类型
c = np.array([[1, 2, 3, 4],[4, 5, 6, 7], [7, 8, 9, 10]], dtype=np.float)

#上面的例子都是先创建一个Python序列，然后通过array函数将其转换为数组,NumPy提供了很多专门用来创建数组的函数。
#arange函数类似于python的range函数，通过指定开始值、终值和步长来创建一维数组，注意数组不包括终值
np.arange(0,1,0.1) # array([ 0. ,  0.1,  0.2,  0.3,  0.4,  0.5,  0.6,  0.7,  0.8,  0.9])
#linspace函数通过指定开始值、终值和元素个数来创建一维数组，可以通过endpoint关键字指定是否包括终值，缺省设置是包括终值
np.linspace(0, 1, 12)
#logspace函数和linspace类似，不过它创建等比数列，下面的例子产生1(10^0)到100(10^2)、有20个元素的等比数列
np.logspace(0, 2, 20)
#此外，使用frombuffer, fromstring, fromfile等函数可以从字节序列创建数组
def func(i):
   return i%4+1
np.fromfunction(func, (10,))    # shape=(10,)
# array([ 1.,  2.,  3.,  4.,  1.,  2.,  3.,  4.,  1.,  2.])

# 可以通过修改数组的shape属性，在保持数组元素个数不变的情况下，改变数组每个轴的长度。
b.shape = 4,3
# 当某个轴的元素为-1时，将根据数组元素的个数自动计算此轴的长度
b.shape = 2,-1

#使用数组的reshape方法，可以创建一个改变了尺寸的新数组，原数组的shape保持不变
d = b.reshape(4,3)
# 数组b和d其实共享数据存储内存区域，因此修改其中任意一个数组的元素都会同时修改另外一个数组的内容：
a[1] = 100 # 将数组a的第一个元素改为100
b[0][0]=10

#存取元素
# 用整数作为下标可以获取数组中的某个元素
a[0]
# 用范围作为下标获取数组的一个切片，包括a[3]不包括a[5]
a[3:5]
# 省略开始下标，表示从a[0]开始
a[:5]
# 下标可以使用负数，表示从数组后往前数
a[:-1]
# 下标还可以用来修改元素的值
a[2:4] = 100,101
a[1:-1:2]# 范围中的第三个参数表示步长，2表示隔一个元素取一个元素
a[::-1] # 省略范围的开始下标和结束下标，步长为-1，整个数组头尾颠倒
a[5:1:-2] # 步长为负数时，开始下标必须大于结束下标
a[:]#省略开始结束下标，取所有元素的值
a[::] #省略开始结束下标及步长，取所有元素的值
a[::-1]#逆序取所有元素的值
#和Python的列表序列不同，通过下标范围获取的新的数组是原始数组的一个视图。它与原始数组共享同一块数据空间。






sizes = [4,6,1]
print sizes[:-1]
print sizes[1:]
# print sizes[1,:]
print zip(sizes[:-1],sizes[1:])
print np.random.randn(10)   #Return a sample (or samples) from the "standard normal" distribution. parameters are dimension(均值为0,方差为1的高斯分布)
print np.random.randn(2,3)
np.random.rand()    #Random values in a given shape.

weights = [np.random.randn(y,x) for x,y in zip(sizes[:-1],sizes[1:])]
# 输入d1输出d2的层，权重为矩阵，维度为d1*d2: 	 d1*(d1,d2) => d2
# 利用切片操作巧妙的将相邻2个组合到一起。sizes[:-1]除最后一个元素之外的序列，sizes[1:]除第0个元素之外的序列。
print weights
biases = [np.random.randn(y,1) for y in sizes[1:]]
#biases大小为输入的大小，输入层除外。
print biases


weights = [np.random.randn(y, x)/np.sqrt(x) for x, y in zip(sizes[:-1],sizes[1:])]
print weights
