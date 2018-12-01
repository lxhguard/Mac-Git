//可以看到当前目录下生成了 input.txt 的压缩文件 input.txt.gz。
//接下来，让我们来解压该文件
var fs = require("fs");
var zlib = require('zlib');

// 解压 input.txt.gz 文件为 input.txt
fs.createReadStream('input.txt.gz')
    .pipe(zlib.createGunzip())
    .pipe(fs.createWriteStream('input.txt'));

console.log("文件解压完成。");