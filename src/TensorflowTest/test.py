#coding=utf8
import tensorflow as tf
import numpy as np

weights1 = tf.random_normal([100,10])
print weights1

weights2 =tf.random_uniform([100,10])
print weights2

biases = tf.zeros([1, 10])
print biases

