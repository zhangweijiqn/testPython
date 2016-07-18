#coding=utf-8
import tensorflow as tf

def testSaveGraph():
    W = tf.Variable([[1,2,3],[4,5,6]],dtype=tf.float32,name="weight")
    b = tf.Variable([[1,2,3]],dtype=tf.float32,name="biase")

    init = tf.initialize_all_variables()

    saver = tf.train.Saver()

    with tf.Session() as sess:
        sess.run(init)
        save_path = saver.save(sess,"logs/save_net.ckpt")
        print "save path: ",save_path

def testReadGraph():
    # restore variables
    # redefine the same shape and same type for your variables ,注意是同name和同shape
    W = tf.Variable(tf.zeros((2, 3)), dtype=tf.float32, name="weight")
    b = tf.Variable(tf.zeros((1, 3)), dtype=tf.float32, name="biase")

    # not need init step

    saver = tf.train.Saver()
    with tf.Session() as sess:
        saver.restore(sess, "logs/save_net.ckpt")
        print("weights:", sess.run(W))
        print("biases:", sess.run(b))

# testSaveGraph()
testReadGraph()