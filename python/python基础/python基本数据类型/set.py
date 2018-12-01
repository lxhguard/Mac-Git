'''
集合 set
特点：无序,不重复


'''

print(type({1,2,3,4}));
print({1,1,2,2,3,3,4,4});

print('\n');
print('看set的一些特性：');
print(len({1,2,3}));
print(1 not in {1,2,3});

print('\n');
print('如何把{1，2，3，4，5，6}中的3，4两个元素剔除：');
print('方法：求两个集合的差集。');
print({1,2,3,4,5,6}-{3,4});
print('方法：求两个集合的交集。');
print({1,2,3,4,5,6}&{3,4});
print('方法：求两个集合的并集。');
print({1,2,3,4,5,6}|{3,7,8});

print(type({}));
print("定义一个空集合使用set():");
print(type(set()));
print(len(set()));










