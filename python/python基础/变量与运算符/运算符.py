'''python运算符
1.算数运算符
+   -   *   /   //整除    % 取余    ** 次方
2.赋值运算符
=   +=  *=  /=  %=  **=    //=
3.比较（关系）运算符     操作结果会返回一个布尔值
==  !=  >   <   <=  >=
4.逻辑运算符 操作布尔类型,返回结果也是布尔类型
and   or  not
5.成员运算符
in    not in
6.身份运算符
is    not is
7.位运算符  把数字当作二进制数进行运算
&   |   ^   ~   <<  >>

'''

print('关系运算符')
print('关系运算符一个有趣的题')
b = 1
#   用这个进行检验print(b>=1)
b+=b>=1
print(b)
print('-----字符,字符串之间比较ascII码   ord()    字符串顺序挨个字母进行比较   --------')
print('a'>'b')
print('列表，元组也是一样的，也可以比较')
print([1,2,3]<[2,3,4,5])
print((1,2,3)<(2,3,4))

print('逻辑运算符')
print('a' and 'b')
print('a' or 'b')
print(not 'a')
print('一个有趣的东西')
print(1 and 2)
#   计算机解析代码的顺序的意义：and计算机只有知道了第二个数值，才能判断表达式的结果
#   就像两个箱子一上一下1，2 ，如果一个人只要一个箱子，那肯定把上面的箱子给人方便一些

print(1 or 2)
#   or读到第一个数值，就可以得到结果，所以直接返回

print('成员运算符')
c = 1
print(c in [1,2,3])
#   字典的成员运算符匹配的是key

print('== 和 is 的区别')
#   ==比较的是值是否相等，is比较的是两个变量的身份是否相等
a = 1
b = 1.0
print(a==b)
print(a is b)
print(id(a))
print(id(b))

print('下面看两个比较有趣的题')
m = {1,2,3}
n = {2,1,3}
print(m == n)
print(m is n)

a = (1,2,3)
b = (2,1,3)
print(a ==b)
#   元组是序列，是有序排列
print(a is b)

print('isinstance(a,())')
a = 'hello'
print(isinstance(a,str))
print(isinstance(a,(int,str,float)))
#   对象的三个特征：id value type
#   is  ==  isinstance











