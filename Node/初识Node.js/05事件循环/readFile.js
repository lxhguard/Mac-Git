var fs = require("fs");

fs.readFile('input1.txt', function (err, data) {
    if (err) {
        console.log(err.stack);
        console.log(err);
        return;
    }
    console.log(data.toString());
});
console.log("程序执行完毕");


//以上程序中 fs.readFile() 是异步函数用于读取文件。 
//如果在读取文件过程中发生错误，错误 err 对象就会输出错误信息。

//如果没发生错误，readFile 跳过 err 对象的输出，文件内容就通过回调函数输出。