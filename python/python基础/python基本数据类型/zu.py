'''
python基本数据类型之组：有很多
1。列表
2.元组

特点：无序

'''

#列表
print(type([1,2,3,4]))
print(['你','我','她']*3);
print(['你','我','她']+['我']);
print([['巴西','墨西哥'],['美国']]);

print('---------------------------');

#元组
print((1,'-1',True));
print((1,2,3)+(4,5));

# int str list列表
print(type((1,2,3)));
print(type([1,2,3]));
print(type(1));
print(type('hello'));



print('一个奇怪的现象:');
print(type((1)));
print(type(('hello')));
print(type(('hello','you')));
#只有一个元素的元组类型是元素本身类型
#解释如下：
print(type((1)));
print((1+1)*2);
#他并不知道type((1))中的()是元组还是数学运算符。规则上，默认它是数学运算符。等同于type(1)。
#由此出现一个问题，如何定义只有一个元素的元组。正解，在单元素后面加一个逗号,(1,)
print(type((1,)));
#如何表示一个空的元组呢？直接使用（）
print(type(()));


print('--------------列表共有的一些操作---------------');
print('序列有 str list tuple');
print('hello world'[2]);
print([1,2,3][2]);
print([1,2,3,4,5][0:3]);
print('hello world'[0:8:2]);

print('判断3在序列中，结果如下:');
print(3 in [1,2,3,4,5]);
print('判断3不在序列中，结果如下:');
print(3 not in [1,2,3,4,5]);

print('统计字符串内部包含的子元素：');
print(len([1,2,3,4]));
print('求最大的一个元素：');
print(max([1,2,3,4,5,6]));
print('求最小的一个元素：');
print(min([1,2,3,4,5,6]));

print(max('helloworld'));
print(min('helloworld'));

# ord() 转换成ascll码
print(ord('w'));









