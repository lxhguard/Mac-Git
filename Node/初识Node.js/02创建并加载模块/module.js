// 创建模块
//module.js

// 在Node.js, 创建一个模块非常简单，因为一个文件就是一个模块，
// 我们要关注的问题仅仅只是如何在其他文件获取这个模块，
// Node.js提供了exports和require俩个对象，
// 其中exports是模块公开的接口，require用于从外部获取一个模块的接口，
// 即获取模块的exports对象。

var name;
exports.setName = function (thyName) {
    name = thyName;
}

exports.sayHello = function () {
    console.log('hello ' + name)
}