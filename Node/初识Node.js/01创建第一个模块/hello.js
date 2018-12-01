var http = require('http');  //通过require对象（指令）来引用http模块
//参数request代表是发送请求对象    response代表是响应请求的对象
http.createServer(function (req, res) { //通过http对象的方法createServer创建一个服务器
    res.writeHead(200, { 'Content-Type': 'text/html' }); //规定数据的content-type文本类型为text/html
    res.write('<h1>Node.js</h1>');  //响应请求然后write 字体大小为h1标准的node.js字样
    res.end('<p>Hello World</p>');   //发送响应数据为 hello world；
}).listen(8888);  //该服务监听本地host 端口8888 

console.log('Server running at http://127.0.0.1:8888/'); //在终端告诉用户该服务运行与8888端口


// 我们调用 http 模块提供的函数： createServer 。
// 这个函数会返回 一个对象，这个对象有一个叫做 listen 的方法，
// 这个方法有一个数值参数， 指定这个 HTTP 服务器监听的端口号。

// 然后你打开当前目录, 打开命令行输入 node hello.js 
// 你就会在命令行处看到Server running at http://127.0.0.1:8888/ ,
// 然后就可以打开浏览器输入这个http://127.0.0.1:8888/ 就可以看到刚才写的响应数据

// 模块是Node.js应用程序的基本组成部分，
// 文件和模块是一一对应的。换句话说，
// 一个Node.js文件就是一个模块，
// 这个文件可能是JavaScript代码, JSON或者编译过的C / C++扩展。

// var http = require('http'), 
// 其中http是Node.js的一个核心模块，
// 其内部是用C++实现的，外部用Javascript封装。
// 我们通过require函数获取这个模块 ，从而才能使用其中的对象。




