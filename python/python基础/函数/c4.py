#   默认参数.想设置默认参数，必须放在后面.也就是默认参数后面不能有未赋值的参数。
def print_student_files(name,gender='男',age=18,college='人民路小学'):
    print('我叫'+name)
    print('我今年' + str(age) + '岁')
    print('我是' + gender + '生')
    print('我在' + college + '上学')

print_student_files('鸡小萌','男',18,'人民路小学')
print('`````````````````````````````')
print_student_files('鸡小萌')
print('`````````````````````````````')
print_student_files('石敢当')
print_student_files('洗小乐',age = 15)

