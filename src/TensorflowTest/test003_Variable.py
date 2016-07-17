#coding=utf8
import tensorflow as tf

''' TensorFlow创建变量，常量，操作 '''

def test1():
    state  = tf.Variable(0,name='counter')  #Variable 用来定义变量，初始值0
    print "state.name:",state.name
    print "state.value:",state.value()

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

def test2():

    Weights = tf.Variable(tf.random_uniform([1],-1.0,1.0),name="weights")  #1维，范围-1到1
    print Weights.name  #weights:0
    biase = tf.Variable(tf.zeros([1]),name="biase")
    print biase.name    #biase:0

test1()
test2()