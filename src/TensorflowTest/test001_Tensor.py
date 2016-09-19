#coding=utf8

"""通过和numpy对比来学习tensorflow中tensor"""

import numpy as np
import tensorflow as tf
sess = tf.InteractiveSession()  #使用交互式便于得到tensor结果

def testTensor():

    a = tf.zeros((2,2))
    print "shape of a:" #(2, 2)
    print  	a.get_shape()
    tf.reshape(a, (1,4))    #元素个数要保持一致

    b = tf.ones((2,2))
    print "ones:"
    print b.eval()

    c = tf.reduce_sum(b)    #会将tensor中所有元素sum
    print c.eval()  #4.0

    d = tf.reduce_sum(b,reduction_indices=0)    #会将tensor中各个dimension元素sum
    print d.eval()  #[ 2.  2.]

    e = tf.matmul(a, b) #矩阵相乘运算
    print "matrix a multiple matrix b:"
    print e.eval()

def testNumpy():

    a = np.zeros((2,2))
    print a
    print a.shape

    np.reshape(a, (1,4))
    print a.shape

    b = np.ones((2,2))
    print b

    c = np.sum(b)   #4.0
    print c

    d = np.sum(b, axis=1)   #[ 2.  2.]
    print d

    e = np.dot(a,b)
    print e

def testTensor2():

    input1 = tf.constant(3.0)
    input2 = tf.constant(4.0)
    input3 = tf.constant(5.0)
    intermed = tf.add(input2, input3)   #加法
    mul = tf.mul(input1, intermed)      #乘法

    # 创建一个常量节点， 产生一个1x2矩阵，这个op被作为一个节点
    # 加到默认视图中
    # 构造器的返回值代表该常量节点的返回值
    matrix1 = tf.constant([[3., 3.]])

    # 创建另一个常量节点, 产生一个2x1的矩阵
    matrix2 = tf.constant([[2.], [2.]])

    # 创建一个矩阵乘法matmul节点，把matrix1和matrix2作为输入：
    product = tf.matmul(matrix1, matrix2)

    #Outputs random values from a normal distribution
    weights1 = tf.random_normal([10,2]) #parameter: rowNum,ColNum
    print "权重矩阵1（正态分布）："
    print weights1.eval()   #直接打印tensor是看不到value的

    #Outputs random values from a uniform distribution
    weights2 =tf.random_uniform([10,2]) #parameter: rowNum,ColNum
    print "权重矩阵1（均匀分布）："
    print weights2.eval()

    biases = tf.zeros([1, 10])  #parameter: rowNum,ColNum
    print "偏置向量（全0）："
    print biases.eval() #[[ 0.  0.  0.  0.  0.  0.  0.  0.  0.  0.]]

    vec = tf.random_uniform([5],-1.0,1.0)   #-1到1之间，5个元素的向量
    print vec.eval()

def testData():
    x_data = np.linspace(-1,1,300)[:, np.newaxis]
    print x_data.shape
# testNumpy()
# testTensor()
# testTensor2()
testData()