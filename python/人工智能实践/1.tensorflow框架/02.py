# 计算图：搭建神经网络的计算过程，只搭建，不运算
import tensorflow as tf

x = tf.constant([[1.0,2.0]])        # x是一个一行两列的张量
w = tf.constant([[3.0],[4.0]])      # y是一个两行一列的张量

y = tf.matmul(x,w)                  # matmul矩阵乘法
print(y)
# Tensor("MatMul:0", shape=(1, 1), dtype=float32) 通过shape看出结果是一行一列的二维张量





