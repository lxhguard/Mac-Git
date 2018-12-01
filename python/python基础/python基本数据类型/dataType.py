
'''
python基本数据类型之Number:数字
1。整数 :int 只有一种整数
2。浮点数 :float 双精度
3。bool :布尔类型  表示真假
4。complex 复数
'''
print("认识整数")
print(type(1))
print(type(-1))
print(type(1.11111))

print("加法运算")
print(type(1+1.1))
print(type(1+1))

print(type(1+1.0))
# python在做一个混合运算时,（整数+浮点数），2.0被认为是浮点数。python会自动转变成浮点型

print("乘法运算")
print(type(1*1))
print(type(1*1.0))

print("除法运算")
print(type(2/2))
print(2/2)
print(type(2//2))
print(2//2)
print(1//2)
# / 除法，py会自动转换成浮点型；  //  整除，保留整数部分

print('-----------------------------------------------------------')
# 10进制，2进制0b，8进制0o，16进制0x
print('进制；')
print(0b10)
print(0o10)
print(0x10)
print("bin()转换成二进制：")
print(bin(0xe))
print("int()转换成十进制：")
print(int(0o77))
print("hex()转换成十六进制：")
print(hex(888))
print("oct()转换成八进制：")
print(oct(0x777))

print('-----------------------------------------------------------')
print("布尔类型：")
print(type(True))
print(type(False))
print(int(True))
print(int(False))
print(bool(True))
print(bool(False))
print(bool([]))
print(bool({}))
print(bool(''))
print(bool(None))
#一系列的空值都会被认为为false

print('-----------------------------------------------------------')
#  用j表示复数








