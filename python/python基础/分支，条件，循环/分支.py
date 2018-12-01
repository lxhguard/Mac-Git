'''
IDE 编程语言的集成开发环境
表达式是运算符和操作数所构成的序列
a or b and c  <=>  a or ( b and c )
一定注意运算符优先级：
指数次幂    一元加减    乘除，模数，地板除   向右和向左位移     与   异或，或    比较运算符   等于运算符   赋值运算符   身份运算符   成员运算符   逻辑运算符

用缩进来区分代码和代码块

学习流程控制语句    循环控制        分支
    if else       for while
    选择性问题

'''

if True:
    pass
    # pass  空语句/占位语句

a = 1
b = 2
c = 2
d = []

if d:
    print('let us go')
    print('go to left')
else:
    print('go to right')




#   这是两个代码块
if True:
    pass

if False:
    pass
'''
伪代码
if condition:
    code1
        code11
        code22
            code333
            code444
                code5555
                code6666
    code2
    code3
else:
    code1
    code2
    code3

if else 是一个代码块，下面的code1是一个新的代码块,code11又是一个新的代码块。。。
要有封装思维的代码，具体的逻辑封装到函数里面。

goto 可以跳转流程，幸好python中不存在这个。

python中没有switch,两种替代方案：  1. elif   2. 字典   

'''

'''
调试的时候使用print进行输出查看。下面代码有问题，并且代码过于冗长（可以用elif进行简化，且elif必须和if一起写，提高代码可读性，尽量减少了乔套）。
a = input()

if a==1:
    print('apple')
else:
    if a==2:
        print('orange')
    else:
        if a==3:
            print('banana')
        else:
            print('shopping')

存在问题：input()接受的是一个字符串，在下面的分支语句中你用字符串跟一个数字做比较，肯定得到结果是false。
        你可以使用type(a)打印出来来观看一下a接收的数据类型。
解决思路：把字符串转换成整型。 a=int(a)

'''
print('请输入a:\n')

a = input()

a=int(a)

if a==1:
    print('apple')
elif a==2:
    print('orange')
elif a==3:
    print('banana')
else:
    print('shopping')





