//获取用户列表：
//以下代码，我们创建了 RESTful API listUsers，用于读取用户的信息列表
//在浏览器中访问 http://127.0.0.1:8081/listUsers
var express = require('express');
var app = express();
var fs = require("fs");

app.get('/listUsers', function (req, res) {
    fs.readFile(__dirname + "/" + "users.json", 'utf8', function (err, data) {
        console.log(data);
        res.end(data);
    });
})

var server = app.listen(8081, function () {

    var host = server.address().address
    var port = server.address().port

    console.log("应用实例，访问地址为 http://%s:%s", host, port)

})