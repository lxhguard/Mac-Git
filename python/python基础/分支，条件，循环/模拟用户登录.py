'''
模块：一个python文件就属于一个模块。这里不详细解释。
'''

ACCOUNT = 'qiyue'
PASSWORD = '123456'
#   python中没有常量的概念。因为python没有机制去阻止值的改变。
#   所以python有一个约定：所有的常量全部用大写字母表示


print('please input account')
user_account = input()
#   pylint对常量的解析规则：不属于函数和类里的都认为是一个常量。


print('please input password')
user_password = input()



if ACCOUNT == user_account and PASSWORD == user_password :
    print('success')
else:
    print('fail')





