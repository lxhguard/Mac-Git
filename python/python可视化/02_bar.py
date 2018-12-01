from pyecharts import Bar

bar = Bar("标记线和标记点示例")
attr = ["jin", "tan", "te", "bie", "mei", "hao"]
v1 = [2.0, 4.9, 7.0, 23.2, 25.6, 76.7]
v2 = [2.6, 5.9, 9.0, 26.4, 28.7, 70.7]
bar.add("商家A", attr, v1, mark_point=["average"])
bar.add("商家B", attr, v2, mark_line=["min", "max"])
bar.render('02_bar.html')

