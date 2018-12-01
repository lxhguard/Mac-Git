Node.js模块系统
为了让Node.js的文件可以相互调用，Node.js提供了一个简单的模块系统。
模块是Node.js 应用程序的基本组成部分，文件和模块是一一对应的。
换言之，一个 Node.js 文件就是一个模块，
这个文件可能是JavaScript 代码、JSON 或者编译过的C/C++ 扩展。

一。创建模块
1.在 Node.js 中，创建一个模块非常简单，如下我们创建一个 main.js 文件，代码如下:
    var hello = require('./hello');
    hello.world();
以上实例中，代码 require('./hello') 引入了当前目录下的
hello.js 文件（./ 为当前目录，node.js 默认后缀为 js）。

2.Node.js 提供了 exports 和 require 两个对象，
其中 exports 是模块公开的接口，require 用于从外部获取一个模块的接口，
即所获取模块的 exports 对象。

3.接下来我们就来创建 hello.js 文件，代码如下：
    exports.world = function() {
        console.log('Hello World');
    }
在以上示例中，hello.js 通过 exports 对象把 world 作为模块的访问接口，
在 main.js 中通过 require('./hello') 加载这个模块，
然后就可以直接访 问 hello.js 中 exports 对象的成员函数了。

有时候我们只是想把一个对象封装到模块中，格式如下：
    module.exports = function() {
        // ...
    }

4.模块接口的唯一变化是使用 module.exports = Hello 
代替了exports.world = function(){}。 
在外部引用该模块时，其接口对象就是要输出的 Hello 对象本身，
而不是原先的 exports。

二。服务端的模块放在哪里
也许你已经注意到，我们已经在代码中使用了模块了。像这样：
    var http = require("http");
    ...
    http.createServer(...);
Node.js 中自带了一个叫做 http 的模块，我们在我们的代码中请求它并把返回值赋给一个本地变量。
这把我们的本地变量变成了一个拥有所有 http 模块所提供的公共方法的对象。
Node.js 的 require 方法中的文件查找策略如下：
由于 Node.js 中存在 4 类模块（原生模块和3种文件模块），
尽管 require 方法极其简单，但是内部的加载却是十分复杂的，其加载优先级也各自不同。


