一。Node.js Web 模块
什么是 Web 服务器？
Web服务器一般指网站服务器，是指驻留于因特网上某种类型计算机的程序，
Web服务器的基本功能就是提供Web信息浏览服务。它只需支持HTTP协议、HTML文档格式及URL，
与客户端的网络浏览器配合。
大多数 web 服务器都支持服务端的脚本语言（php、python、ruby）等，
并通过脚本语言从数据库获取数据，将结果返回给客户端浏览器。
目前最主流的三个Web服务器是Apache、Nginx、IIS。

二。Web 应用架构
Client - 客户端，一般指浏览器，浏览器可以通过 HTTP 协议向服务器请求数据。
Server - 服务端，一般指 Web 服务器，可以接收客户端请求，并向客户端发送响应数据。
Business - 业务层， 通过 Web 服务器处理应用程序，如与数据库交互，逻辑运算，调用外部程序等。
Data - 数据层，一般由数据库组成。

三。使用 Node 创建 Web 服务器
Node.js 提供了 http 模块，http 模块主要用于搭建 HTTP 服务端和客户端，
使用 HTTP 服务器或客户端功能必须调用 http 模块，代码如下：
    var http = require('http');

四。使用 Node 创建 Web 客户端
Node 创建 Web 客户端需要引入 http 模块，创建 client.js 文件    