#coding=utf8
import tensorflow as tf

''' TensorFlow创建变量，常量，操作 '''

state  = tf.Variable(0,name='counter')  #Variable 用来定义变量，初始值0
print state.name

one  = tf.constant(1)   #constant 定义常量

new_value = tf.add(state,one)   #add 执行加法
update = tf.assign(state,new_value) #将new_value赋值给state


# Add an op to initialize the variables.
init = tf.initialize_all_variables()    #初始化所有变量，定义的变量需要执行此操作

with tf.Session() as sess:
    sess.run(init)
    for _ in range(5):
        sess.run(update)
        print sess.run(state)


# Create two variables.
weights = tf.Variable(tf.random_normal([784, 200], stddev=0.35), name="weights")
biases = tf.Variable(tf.zeros([200]), name="biases")

