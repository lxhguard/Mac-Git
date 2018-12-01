'''
python基本数据类型之str:字符串
如何表示字符串？单引号，双引号，三引号。（一定要成对出现）
'''

print('hello world')
print("hello world")

print(type(1))
print(type('1'))

print("let 's go")
print('let "s go')
print('let \'s go')
#     \ 转义字符.不推荐用这种方法。推荐使用第一二种方式

print('----------------------三引号----------------')
# 每行宽度为79个字符。
#用三引号(单或双)可以表示  多行字符串
print('''hello\nworld''')
'''
转义字符 
    特殊的字符
    无法"看见"的字符
    与语言本身语法有冲突的字符
\n  换行
\'  单引号
\t  横向制表符
'''
print('hello \\n world')
print(r'hello \n world')
#字符串拼接
print('hello'+'world')
print('hello'*3)
print('hello'[-1])
print('hello'[0:2])
print('hello'[0:-2])

