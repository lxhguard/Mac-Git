//引入模块
// getmodule.js

var myModule = require('./module');
myModule.setName('zhangsan');
myModule.sayHello();

//在命令行运行node getmodule.js   输出 hello zhangsan

// 以上该例子中, 
// module.js通过exports对象吧setName 和 sayHello作为模块的访问接口，
// 在getmodule.js中通过require（'./module'）加载这个模块，
// 然后就可以之间访问module.js中exports对象的成员函数了

// require 不会重复加载模块, 无论调用多少次require,
// 获得的模块都是同一个, 修改一下上面的getmodule.js，代码如下所示：
// var hello1 = require('./module');
// hello1.setName('zhangsan');
// var hello2 = require('./module');
// hello2.setName('zhangsan2');
// hello1.sayHello(); 
// 输出结果为zhangsan2!
// 因为变量hello1和变量hello2执行都是同一个实例, 
// 因此hello1.setName的结果被hello2.setName覆盖
// 结果由后者决定




