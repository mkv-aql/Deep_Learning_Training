__author__ = 'mkv-aql'
import tensorflow as tf

tf.__version__
print(tf.__version__) # 2.11.0

mnist = tf.keras.datasets.mnist # 28x28 images of hand-written digits 0-9 (10 classes)