#coding:utf-8
#   0导入模块，生成模拟数据集
import tensorflow as tf
import numpy as np
BATCH_SIZE = 8
#   一次喂入神经网络的特征最大值
seed = 23455

#   基于seed产生随机数
rng = np.random.RandomState(seed)
#   随机数返回32行2列的矩阵，表示32组体积和重量，作为输入数据集
X = rng.rand(32,2)
#   X是32组，每组2个特征构成的32行2列矩阵
#   从X这个32行2列的矩阵中，取出一行，判断如果和小于1，给Y赋值1，如果和不小于1，给Y赋值0
#   Y作为输入数据集的标签（正确答案）
Y = [[int(x0 + x1 < 1)] for (x0, x1) in X]
#   Y是人为给出一个零件合格与否的标准：体积加重量小于1，标记为1，表示合格。0表示为不合格。
#   这只是因为我们手头没有数据集，虚拟的样本和标签。神经网络训练判断零件是否合格是基于数据和概率的。
#   代码15行实现了数据标注的功能
print("X:\n",X)
print("Y:\n",Y)

#  1定义神经网络的输入.参数和输出，定义前向传播过程
x = tf.placeholder(tf.float32, shape=(None, 2))
#   知道有体积和重量2个特征，不知道可以拿到多少组特征。shape()第一位表示有多少组，第二位表示每组有多少个
y_ = tf.placeholder(tf.float32, shape=(None, 1))
#   y_表示标准答案，也就是合格是1，不合格是0的标签。有多少个标签不知道，用None占位。只有一个元素，就是合格还是不合格。


#   参数要匹配输入和输出。输入是2个特征，输出是1个数。所以w1是2行，对应x；w2是1列，对应y。隐藏层用3个神经元。
#   为了保证所有同学生成的随机参数一致，我们加入了随机种子 seed=1。
w1 = tf.Variable(tf.random_normal([2, 3], stddev=1, seed=1))
w2 = tf.Variable(tf.random_normal([3, 1], stddev=1, seed=1))


#   这是前向传播的矩阵过程描述，用矩阵乘法实现
a = tf.matmul(x, w1)
y = tf.matmul(a, w2)

#   2定义损失函数及反向传播方法
loss = tf.reduce_mean(tf.square(y-y_))
#   reduce_mean均方误差 计算loss
train_step = tf.train.GradientDescentOptimizer(0.001).minimize(loss)
#   GradientDescentOptimizer梯度下降 实现训练过程。学习率填0.001。也可以使用下面两种训练方法。
#   train_step = tf.train.GradientDescentOptimizer(0.001,0.9).minimize(loss)
#   train_step = tf.train.AdamOptimizer(0.001).minimize(loss)

#   3生成会话，训练STEPS轮
with tf.Session() as sess:
    init_op = tf.global_variables_initializer()
    sess.run(init_op)
    #   输出目前（未经训练）的参数取值
    print("w1:\n", sess.run(w1))
    print("w2:\n", sess.run(w2))

    #   训练模型
    STEPS = 3000
    #   训练3000轮
    for i in range(STEPS):
        start = (i*BATCH_SIZE) % 32
        end = start + BATCH_SIZE
        sess.run(train_step, feed_dict={x: X[start:end], y_:Y[start:end]})
        #   每轮从X的数据集和Y的标签中，抽取相应的从start到end个特征和标签喂入神经网络，用sess.run执行训练过程
        #   每500轮打印一次loss值
        if i % 500 == 0:
            total_loss = sess.run(loss, feed_dict={x: X,y_: Y})
            print("After %d training step(s), loss on all data is %g" % (i,total_loss))
    #   输出训练后的参数取值
    print("\n")
    print("w1:\n", sess.run(w1))
    print("w2:\n", sess.run(w2))

#   总结：1.大家可以把代码的训练次数增大，观察loss的减少过程。
#   2.还可以更改train_step为别的优化器（总共3种），试一下哪个优化器效果更好。
#   3.还可以更改BATCH_SIZE，观察对loss的影响。

'''
搭建神经网络的八股：准备，前传，反传，迭代

0准备     import
         常量定义
         生成数据集 
1前向传播：  定义输入，参数和输出
        x=
        y_=
        
        w1=
        w2
        
        a=
        y=
2反向传播：  定义损失函数，反向传播方法
        loss=
        train_step=
3生成会话，训练STEPS轮
        with tf.Session() as sess:
            init_op=tf.global_variables_initializer()
            sess_run(init_op)
            
            STEPS=3000
            for i in range(STEPS):
                start=
                end=
                sess.run(train_step,feed_dict:)


            

'''








