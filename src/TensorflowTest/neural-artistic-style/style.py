'''
https://github.com/janivanecky/Artistic-Style
Simple script implementing artistic style transfer based on the work of Gatys et al. (http://arxiv.org/abs/1508.06576)
VGG implementation for Tensorflow taken from https://github.com/machrisaa/tensorflow-vgg and slightly modified.

by Jan Ivanecky
MIT license

'''

import argparse
import numpy as np
from PIL import Image
Image.LOAD_TRUNCATED_IMAGES = True
import tensorflow as tf
import vgg

def load_image(path, shape=None, scale=1.0):
  img = Image.open(path)

  if shape is not None:
    # crop to obtain identical aspect ratio to shape
    width, height = img.size
    target_width, target_height = shape[0], shape[1]

    aspect_ratio = width / float(height)
    target_aspect = target_width / float(target_height)

    # if aspect_ratio > target_aspect: # if wider than wanted, crop the width
    #   new_width = int(height * target_aspect)
    #   if args.crop == 'right':
    #     img = img.crop((width - new_width, 0, width, height))
    #   elif args.crop == 'left':
    #     img = img.crop((0, 0, new_width, height))
    #   else:
    #     img = img.crop(((width - new_width) / 2, 0, (width + new_width) / 2, height))
    # else: # else crop the height
    #   new_height = int(width / target_aspect)
    #   if args.crop == 'top':
    #     img = img.crop((0, 0, width, new_height))
    #   elif args.crop == 'bottom':
    #     img = img.crop((0, height - new_height, width, height))
    #   else:
    #     img = img.crop((0, (height - new_height) / 2, width, (height + new_height) / 2))

    # resize to target now that we have the correct aspect ratio
    img = img.resize((target_width, target_height))

  # rescale
  w,h = img.size
  img = img.resize((int(w * scale), int(h * scale)))
  img.show()
  img = np.array(img)
  img = img / 255.0
  return img

def gram_matrix(activations):
  height = tf.shape(activations)[1]
  width = tf.shape(activations)[2]
  num_channels = tf.shape(activations)[3]
  gram_matrix = tf.transpose(activations, [0, 3, 1, 2])
  gram_matrix = tf.reshape(gram_matrix, [num_channels, width * height])
  gram_matrix = tf.matmul(gram_matrix, gram_matrix, transpose_b=True)
  return gram_matrix

def content_loss(const_layer, var_layer):
  diff = const_layer - var_layer
  diff_squared = diff * diff
  sum = tf.reduce_sum(diff_squared) / 2.0
  return sum

def style_loss(const_layers, var_layers):
  loss_style = 0.0
  layer_count = float(len(const_layers))
  for const_layer, var_layer in zip(const_layers, var_layers):
    gram_matrix_const = gram_matrix(const_layer)
    gram_matrix_var = gram_matrix(var_layer)

    size = tf.to_float(tf.size(const_layer))
    diff_style = gram_matrix_const - gram_matrix_var
    diff_style_sum = tf.reduce_sum(diff_style * diff_style) / (4.0 * size * size)
    loss_style += diff_style_sum
  return loss_style / layer_count

def main(content_image_path,style_image_path,content_scale,style_weight):
  # prepare input images
  content_image = load_image(content_image_path, scale=float(content_scale))
  WIDTH, HEIGHT = content_image.shape[1], content_image.shape[0]
  content_image = content_image.reshape((1, HEIGHT, WIDTH, 3))
  style_image = load_image(style_image_path, (WIDTH, HEIGHT))
  style_image = style_image.reshape((1, HEIGHT, WIDTH, 3))

  # prepare networks
  images = np.concatenate((content_image, style_image), 0).astype(np.float32)
  constants = tf.constant(images)
  with tf.name_scope("constant"):
    vgg_const = vgg.Vgg19()
    vgg_const.build(constants)

  # use noise as an initial image
  #input_image = tf.Variable(tf.truncated_normal([1, HEIGHT, WIDTH, 3], 0.5, 0.1))
  # use content image as an initial image
  input_image = tf.Variable(np.expand_dims(images[0,:,:,:], 0))
  with tf.name_scope("variable"):
    vgg_var = vgg.Vgg19()
    vgg_var.build(input_image)

  # which layers we want to use?
  style_layers_const = [vgg_const.conv1_1, vgg_const.conv2_1, vgg_const.conv3_1, vgg_const.conv4_1, vgg_const.conv5_1]
  style_layers_var = [vgg_var.conv1_1, vgg_var.conv2_1, vgg_var.conv3_1, vgg_var.conv4_1, vgg_var.conv5_1]
  content_layer_const = vgg_const.conv4_2
  content_layer_var = vgg_var.conv4_2

  # get activations of content and style images as TF constants
  sess = tf.Session()
  layers = sess.run([content_layer_const] + style_layers_const)
  content_layer_const = tf.constant(np.expand_dims(layers[0][0,:,:,:], 0))
  style_layers_const = [tf.constant(np.expand_dims(layer[1,:,:,:], 0)) for layer in layers[1:]]

  # compose the loss function
  content_style_ratio = 1e-4
  loss_content = content_loss(content_layer_const, content_layer_var)
  loss_style = style_loss(style_layers_const, style_layers_var)
  style_weight = float(style_weight)
  overall_loss = (1 - style_weight) * content_style_ratio * loss_content + style_weight * loss_style

  # set up optimizer
  output_image = tf.clip_by_value(tf.squeeze(input_image, [0]), 0, 1)
  train = tf.train.AdamOptimizer(learning_rate=0.05).minimize(overall_loss)


  # get the stylized image
  init = tf.initialize_all_variables()
  sess.run(init)
  min_loss, best_image = float("inf"), None
  for i in xrange(0,500):
    image, loss, _ = sess.run([output_image, overall_loss, train])
    if i % 5 == 0:
      print 'Iteration {}: {}'.format(i, loss)
      if(loss < min_loss):
        min_loss, best_image = loss, image

  # save the result
  best_image = np.clip(best_image, 0, 1)
  best_image = np.reshape(best_image, (HEIGHT,WIDTH,3))
  result = Image.fromarray(np.uint8(best_image * 255))
  result.save(output_image)
  result.show()

if __name__=="__main__":
  main("/home/zhangwj/MyProjects/testProjects/TestLanguageTech/testPython/src/resources/cat.jpg",
       "/home/zhangwj/MyProjects/testProjects/TestLanguageTech/testPython/src/resources/style.jpg",1.0,0.6)
# parse args



