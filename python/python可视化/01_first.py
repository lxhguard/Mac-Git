from pyecharts import Bar
bar = Bar("我的第一个图表", "这里是副标题")
bar.add("服装", ["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"], [5, 20, 36, 10, 75, 90])
bar.add("ss", ["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"], [5, 20, 36, 10, 75, 90])
bar.show_config()
bar.render('01_first.html')

'''
bar(left, height, width, color, align, yerr)  绘制柱形图
add()  主要方法，用于添加图表的数据和设置各种配置项
show_config()  打印输出图表的所有配置项
render()  默认将会在根目录下生成一个 render.html 的文件，支持 path 参数，设置文件保存位置，如 render(r"e:my_first_chart.html")，文件用浏览器打开。
          可以生成指定文件名的html文件，比如render('123.html')
'''

'''
基本上所有的图表类型都是这样绘制的：
1.chart_name = Type() 初始化具体类型图表。
2.add() 添加数据及配置项。
3.render() 生成 .html 文件。
'''