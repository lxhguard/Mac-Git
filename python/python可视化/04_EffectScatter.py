from pyecharts import EffectScatter

v1 = [10, 20, 30, 40, 50, 60]
v2 = [25, 20, 15, 10, 60, 33]
es = EffectScatter("动态散点图示例")
es.add("effectScatter1", v1, v2)
#  add添加名字，第二个参数是横坐标，第三个参数是纵坐标
es.add("effectScatter2", v2, v1)
es.render('04_EffectScatter.html')

