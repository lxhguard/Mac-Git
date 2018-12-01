// 创建数据库
// 要在 MongoDB 中创建一个数据库，首先我们需要创建一个 MongoClient 对象，
//然后配置好指定的 URL 和 端口号。

// 如果数据库不存在，MongoDB 将创建数据库并建立连接。


const MongoClient = require('mongodb').MongoClient;

MongoClient.connect("mongodb://localhost:27017/runoob",
            { useNewUrlParser: true },
            function (err) {
                if (err) {
                    console.log('Connection Error:' + err)
                } else {
                    console.log('Connection success!')
                }
})
// var MongoClient = require('mongodb').MongoClient;
// var url = "mongodb://localhost:27017/runoob";

// MongoClient.connect(url, function (err, db) {
//     if (err) throw err;
//     console.log("数据库已创建!");
//     db.close();
// });