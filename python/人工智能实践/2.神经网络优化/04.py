'''
学习率 learning_rate:每次参数更新的幅度
W(n+1) =  Wn  -  learning_rate ▽
更新后    当前     学习率      损失函数的梯度
的参数    参数                   （导数）

下面的例子中，最优解是-1,这个是看视频的图进行求解的。
'''
#coding:utf-8
#   设损失函数 loss=(w+1)^2, 令w初值是常数5。反向传播就是求最优w，即求最小loss对应的w值
import tensorflow as tf
#   定义待优化参数w初值赋5
w = tf.Variable(tf.constant(5, dtype=tf.float32))
#   定义损失函数loss
loss = tf.square(w+1)
#   定义反向损失方法
train_step = tf.train.GradientDescentOptimizer(0.2).minimize(loss)
#   生成会话,训练40轮
with tf.Session() as sess:
    init_op = tf.global_variables_initializer()
    sess.run(init_op)
    for i in range(40):
        sess.run(train_step)
        w_val = sess.run(w)
        loss_val = sess.run(loss)
        print("After %s steps: w is %f, loss is %f." % (i, w_val, loss_val))
#   学习率分别改为 1 ， 0.0001 进行观察
'''
学习率设置多少合适？学习率大了振荡不收敛，学习率小了收敛速度慢。
于是提出了  指数衰减学习率
learning_rate = LEARNING_RATE_BASE.LEARNING_RATE_DECAY ( global_step           /        LEARNING_RATE_STEP )
            学习率基数，学习率初始值     学习率衰减率（0，1）  运行了几轮BATCH_SIZE        多少轮更新一次学习率=样本总数/BATCH_SIZE
'''












