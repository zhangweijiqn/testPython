#coding=utf8
__author__ = 'zhangwj'
import tensorflow as tf

"""
指定设备的书写格式如下：

    /cpu:0:机器的CPU
    /gpu:0:机器的第一个GPU，如果有的话
    /gpu:1:机器的的第二个GPU，其他GPU以此类推

"""

# 手动指定给某个gpu执行
with tf.Session() as sess:
    with tf.device("/gpu:1"):
        matrix1 = tf.constant([[3., 3.]])
        matrix2 = tf.constant([[2.], [2.]])
        product = tf.matmul(matrix1, matrix2)

"""
指定设备的书写格式如下：

    /cpu:0:机器的CPU
    /gpu:0:机器的第一个GPU，如果有的话
    /gpu:1:机器的的第二个GPU，其他GPU以此类推

"""
