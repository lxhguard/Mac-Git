// express_cookie.js 文件
var express = require('express')
var cookieParser = require('cookie-parser')
var util = require('util');

var app = express()
app.use(cookieParser())

app.get('/', function (req, res) {
    console.log("Cookies: " + util.inspect(req.cookies));
})

app.listen(8081);
//现在你可以访问 http://127.0.0.1:8081 并查看终端信息的输出