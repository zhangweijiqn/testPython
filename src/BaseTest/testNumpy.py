#coding=utf8
import numpy as np
sizes = [2,3,1]
print sizes[:-1]
print sizes[1:]
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


