'''
循环是一种思想： while  for
二者都可以和 else 搭配
while else 是有一个判断条件的，当不满足判断条件就是执行else
for   else 当遍历完所有的元素，就会执行else


while codition:
    代码块

'''

# CONDITION=True
# while CONDITION:
#     print('i am while')

#   在递归场景下，使用while还是很好的。
# counter = 1
#
# while counter <= 10:
#     counter += 1
#     print(counter)
# else:
#     print('EOF')



#for循环主要用来遍历/循环    序列或者集合，字典

# a = [['apple','orange','banana','grape'],(1,2,3)]
# for x in a:
#     for y in x:
#         if y=='orange':
#             break
#         print(y,end=' ')
# else:
#     print('fruit is gone')

'''
上面代码中break跳出的是内部的for循环，即for y in x: 而外部的for循环还是继续的。

print打印出来的将呈现一个列的排布
如果你想一行输出，可以 print(y,end='')
'''


'''
break       强行终止当前循环，并且以后的循环都不会再执行。连else里面的语句也不会执行。
continue    不执行当前循环，继续执行后续循环。可以执行else里面的语句。    
'''
# a = [1,2,3]
# for x in a:
#     if x == 2:
#         break
#     print(x)
# else:
#     print('EOF')



'''
    for(i=0;i<=10;i++)
    {
    
    }
    这种for循环在python中如何表示呢
'''
#   递增
# for x in range(0,10):
#     print(x,end=' | ')
# print('')
# #   递减
# for x in range(10,0,-2):
#     print(x,end=" | ")


'''
取出里面的奇数
'''
a=[1,2,3,4,5,6,7,8]
for i in range(0,len(a),2):
    print(a[i],end=' | ')

b=a[0:len(a):2]
print(b)

#   高性能，封装性（可复用），抽象











