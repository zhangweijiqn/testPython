#coding=utf8
__author__ = 'zhangwj'
# 参考教程3.1.1
import tensorflow as tf
import numpy as np

#crate data
x_data = np.random.rand(100).astype(np.float32)
y_data = x_data*0.1+0.3

#create tensorflow structure : weights + biase,
Weights = tf.Variable(tf.random_uniform([1],-1.0,1.0),name="weights")  #1维，范围-1到1
biase = tf.Variable(tf.zeros([1]),name="biase")

y = Weights*x_data+biase

loss = tf.reduce_mean(tf.square(y-y_data)) # loss function
optimizer = tf.train.GradientDescentOptimizer(0.5) #optimizer
train = optimizer.minimize(loss)

init = tf.initialize_all_variables()


sess = tf.Session()
sess.run(init)  #start to init

for step in range(201):
    sess.run(train)
    print step,sess.run(Weights),sess.run(biase)


# run 函数 传递的参数类型不同，作用不同:
'''
* If the *i*th element of `fetches` is an
      [`Operation`](../../api_docs/python/framework.md#Operation), the *i*th
      return value will be `None`.  #operate返回None
    * If the *i*th element of `fetches` is a
      [`Tensor`](../../api_docs/python/framework.md#Tensor), the *i*th return
      value will be a numpy ndarray containing the value of that tensor.    #tensor返回tensor的value
    * If the *i*th element of `fetches` is a
      [`SparseTensor`](../../api_docs/python/sparse_ops.md#SparseTensor),
      the *i*th return value will be a
      [`SparseTensorValue`](../../api_docs/python/sparse_ops.md#SparseTensorValue)
      containing the value of that sparse tensor.
    * If the *i*th element of `fetches` is produced by a `get_tensor_handle` op,
      the *i*th return value will be a numpy ndarray containing the handle of
      that tensor.
'''