#   面向对象
#   有意义的面向对象的代码
#   类 = 面向对象
#   实例化
#   类的最基本的作用：封装代码
#   类和对象    类就像是一个模板，可以产生很多对象
class Student():
    #一个班级里所有学生的总数n
    sum = 0
    name = 'qiyue'
    age = 0
    # 类变量 实例变量
    def __init__(self,name,age):
        #   它是构造函数
        #   初始化对象的属性
        self.name = name
        self.age = age
        #print('student')
    #行为     与   特征
    def do_homework(self):
        print('homework')


# class Printer():
#     def print_file(self):
#         print('name:' + self.name)
#         print('age:' + str(self.age))

 #  调用类下面的函数
student1 = Student('石敢当',18)
# student2 = Student()
# student3 = Student()
# print(id(student1))
# print(id(student2))
# print(id(student3))
print(student1.name)
print(Student.name)
# print(student1.__dict__)
# print(Student.__dict__)
'''
__dict__表示的是一个类下对象所有信息
'''
# student1.print_file()

'''
类是现实世界或四维世界中的实体在计算机中的反映
它将数据以及这些数据上的操作封装在一起
'''



'''
class Student():
    name = 'qiyue'
    age = 0
    def __init__(self,name,age):
        name = name
        age = age

print(student1.name)
print(Student.name)

打印结果为:
qiyue
qiyue
分析原因:


'''





