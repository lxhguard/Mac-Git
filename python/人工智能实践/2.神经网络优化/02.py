'''
损失函数loss：预测值（y）与已知答案（y_）的差距
    NN优化目标： loss最小-->3种：均方误差mse,自定义,ce

例题：预测酸奶日销量y。x1,x2是影响日销量的因素。
建模前，应预先采集的数据有：每日x1，x2和销量y_(即已知答案，最佳情况：产量=销量)
拟造数据集X，Y_： y_ = x1 + x2  噪声：-0.05～+0.05   拟合可以预测销量的函数


自定义损失函数
loss = tf.reduce_sum(  tf.where(tf.greater(y,y_)    ,  COST(y-y_)   ,     PROFIT(y_-y)    ))
                        y>y_?                           真:                      假
'''

# coding:utf-8
#   酸奶成本1元，酸奶利润9元
#   预测少了损失大，故不要预测少，故生成的模型会多预测一些
#   0导入模块，生成模拟数据集
import tensorflow as tf
import numpy as np

BATCH_SIZE = 8
#   一次喂入神经网络的特征最大值
SEED = 23455
COST = 1
PROFIT = 9

#   基于seed产生随机数
rdm = np.random.RandomState(SEED)
#   随机数返回32行2列的矩阵，表示32组体积和重量，作为输入数据集
X = rdm.rand(32, 2)
#   X是32组，每组2个特征构成的32行2列矩阵
#   从X这个32行2列的矩阵中，取出一行，判断如果和小于1，给Y赋值1，如果和不小于1，给Y赋值0
#   Y作为输入数据集的标签（正确答案）
Y = [[x1 + x2 + (rdm.rand() / 10.0 - 0.05)] for (x1, x2) in X]

#  1定义神经网络的输入.参数和输出，定义前向传播过程
x = tf.placeholder(tf.float32, shape=(None, 2))
#   知道有体积和重量2个特征，不知道可以拿到多少组特征。shape()第一位表示有多少组，第二位表示每组有多少个
y_ = tf.placeholder(tf.float32, shape=(None, 1))
#   y_表示标准答案，也就是合格是1，不合格是0的标签。有多少个标签不知道，用None占位。只有一个元素，就是合格还是不合格。


#   参数要匹配输入和输出。输入是2个特征，输出是1个数。所以w1是2行，对应x；w2是1列，对应y。隐藏层用3个神经元。
#   为了保证所有同学生成的随机参数一致，我们加入了随机种子 seed=1。
w1 = tf.Variable(tf.random_normal([2, 1], stddev=1, seed=1))

#   这是前向传播的矩阵过程描述，用矩阵乘法实现
y = tf.matmul(x, w1)

#   2定义损失函数及反向传播方法
#   定义损失函数使得预测少了的损失大，于是模型应该偏向多的方向预测
loss = tf.reduce_sum(tf.where(tf.greater(y,y_),(y-y_)*COST,(y_-y)*PROFIT))
#   reduce_mean均方误差 计算loss
train_step = tf.train.GradientDescentOptimizer(0.001).minimize(loss)


#   3生成会话，训练STEPS轮
with tf.Session() as sess:
    init_op = tf.global_variables_initializer()
    sess.run(init_op)

    #   训练模型
    STEPS = 2000
    。
    #   训练2000轮
    for i in range(STEPS):
        start = (i * BATCH_SIZE) % 32
        end = start + BATCH_SIZE
        sess.run(train_step, feed_dict={x: X[start:end], y_: Y[start:end]})
        #   每轮从X的数据集和Y的标签中，抽取相应的从start到end个特征和标签喂入神经网络，用sess.run执行训练过程
        #   每500轮打印一次loss值
        if i % 500 == 0:
            print("After %d training step(s), w1 is " % (i))
            print(sess.run(w1))
            print("\n")
        print("Final w1 is: \n", sess.run(w1))

#   在本代码中2中尝试其他反向传播方法，看收敛速度的影响，把体会写到笔记中
















