一。Node.js Stream(流)
Stream 是一个抽象接口，Node 中有很多对象实现了这个接口。
例如，对http 服务器发起请求的request 对象就是一个 Stream，还有stdout（标准输出）。
Node.js，Stream 有四种流类型：
    Readable - 可读操作。
    Writable - 可写操作。
    Duplex - 可读可写操作.
    Transform - 操作被写入数据，然后读出结果。
所有的 Stream 对象都是 EventEmitter 的实例。常用的事件有：
    data - 当有数据可读时触发。
    end - 没有更多的数据可读时触发。
    error - 在接收和写入过程中发生错误时触发。
    finish - 所有数据已被写入到底层系统时触发。
本教程会为大家介绍常用的流操作。

二。管道流
管道提供了一个输出流到输入流的机制。
通常我们用于从一个流中获取数据并将数据传递到另外一个流中。

我们把文件比作装水的桶，而水就是文件里的内容，
我们用一根管子(pipe)连接两个桶使得水从一个桶流入另一个桶，
这样就慢慢的实现了大文件的复制过程。

三。链式流
链式是通过连接输出流到另外一个流并创建多个流操作链的机制。
链式流一般用于管道操作。