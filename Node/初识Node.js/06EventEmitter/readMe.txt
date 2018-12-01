一。Node.js EventEmitter
1.Node.js 所有的异步 I/O 操作在完成时都会发送一个事件到事件队列。
2.Node.js 里面的许多对象都会分发事件：一个 net.Server 对象会在每次有新连接时触发一个事件，
 一个 fs.readStream 对象会在文件被打开的时候触发一个事件。 
 所有这些产生事件的对象都是 events.EventEmitter 的实例。

 二。EventEmitter 类
 1.events 模块只提供了一个对象： events.EventEmitter。
 EventEmitter 的核心就是事件触发与事件监听器功能的封装。
你可以通过require("events");来访问该模块。
    // 引入 events 模块
    var events = require('events');
    // 创建 eventEmitter 对象
    var eventEmitter = new events.EventEmitter();
2.EventEmitter 对象如果在实例化时发生错误，会触发 error 事件。
当添加新的监听器时，newListener 事件会触发，
当监听器被移除时，removeListener 事件被触发。
3.EventEmitter 的每个事件由一个事件名和若干个参数组成，
事件名是一个字符串，通常表达一定的语义。
对于每个事件，EventEmitter 支持 若干个事件监听器。
当事件触发时，注册到这个事件的事件监听器被依次调用，事件参数作为回调函数参数传递。

三。error 事件
EventEmitter 定义了一个特殊的事件 error，它包含了错误的语义，
我们在遇到 异常的时候通常会触发 error 事件。
当 error 被触发时，EventEmitter 规定如果没有响 应的监听器，
Node.js 会把它当作异常，退出程序并输出错误信息。
我们一般要为会触发 error 事件的对象设置监听器，避免遇到错误后整个程序崩溃。例如：
    var events = require('events'); 
    var emitter = new events.EventEmitter(); 
    emitter.emit('error'); 
运行时会显示以下错误：
    node.js:201 
    throw e; // process.nextTick error, or 'error' event on first tick 
    ^ 
    Error: Uncaught, unspecified 'error' event. 

四。继承 EventEmitter
大多数时候我们不会直接使用 EventEmitter，而是在对象中继承它。
包括 fs、net、 http 在内的，只要是支持事件响应的核心模块都是 EventEmitter 的子类。
为什么要这样做呢？原因有两点：
首先，具有某个实体功能的对象实现事件符合语义， 事件的监听和发生应该是一个对象的方法。
其次 JavaScript 的对象机制是基于原型的，支持 部分多重继承，
继承 EventEmitter 不会打乱对象原有的继承关系。

