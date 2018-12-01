#   函数
# a = 1.12386
# result = round(a,3)
# print(result)
'''
round()函数会四舍五入。第一个参数是操作数，第二个参数是小数点后保留的位数。它是python内置函数。
在命令行中输入 help(round) 可以查询相关命令。如果显示 -more- 表示解释太多，未显示完。你可以敲击回车进行翻页。
在命令行中输入 import this 会显示python之禅
'''
#   1。功能性   2。隐藏细节  3.避免写重复代码

'''
函数的定义及其运行特点
def funcname(parameter_list)
    pass
注意：1。参数列表可以没有   2。return value   没有设置返回值，自动默认返回None
'''
#   实现两个数字的相加
def add(x,y):
    result = x + y
    return result

#   打印输入的参数
def print_code(code):
    print(code)
    return
#Python有递归次数限制，默认最大次数为1000。
'''
可以设置最大递归次数
import sys
sys.setrecursionlimit(1000000)
一定避免python定义的变量和内置函数重名
'''



a = add(1,2)
b = print_code('Python')
print(a,b)
'''
a被赋值为3，但是还没有被打印。
b在运行函数的时候打印了Python.
b 赋值为None.打印a,b在一行
'''



















