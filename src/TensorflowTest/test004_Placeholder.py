#coding=utf8
import tensorflow as tf
"""tensorflow feed操作"""
input1 = tf.placeholder(tf.float32)
#input1 = tf.placeholder(tf.float32,[2,2])
input2 = tf.placeholder(tf.float32)
ouput = tf.mul(input1, input2)

with tf.Session() as sess:
    print(sess.run(ouput, feed_dict={input1: [7.,5.], input2: [2.,6.]}))  #运行时，将具体参数值传入，传入格式python字典
