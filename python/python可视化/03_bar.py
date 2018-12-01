from pyecharts import Bar

bar = Bar("x 轴和 y 轴交换")
attr = ["jin", "tan", "te", "bie", "mei", "hao"]
v1 = [2.0, 4.9, 7.0, 23.2, 25.6, 76.7]
v2 = [2.6, 5.9, 9.0, 26.4, 28.7, 70.7]
bar.add("商家A", attr, v1)
bar.add("商家B", attr, v2, is_convert=True)
bar.render('03_bar.html')