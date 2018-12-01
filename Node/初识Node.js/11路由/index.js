var server = require("./server");
var router = require("./router");

server.start(router.route);

//以上输出已经去掉了比较烦人的 / favicon.ico 请求相关的部分。

//浏览器访问 http://127.0.0.1:8888/，输出结果如下：
//hello world