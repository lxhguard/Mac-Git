#  基于tensorflow的神经网络用张量表示数据，用计算图搭建神经网络，用会话执行计算图，优化线上的权重（参数），得到模型

import tensorflow as tf

a = tf.constant([1.0,2.0])
b = tf.constant([3.0,4.0])

result = a + b
print(result)   # Tensor("add:0", shape=(2,), dtype=float32) 节点名 第0个输出 唯独 一位数组长度为2 数据类型







