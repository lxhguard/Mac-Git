from pyecharts import Funnel

attr = ["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"]
value = [20, 40, 60, 80, 100, 120]
funnel = Funnel("漏斗图示例")
funnel.add("商品", attr, value, is_label_show=True, label_pos="inside", label_text_color="black")
#    类型名称  样品名  数量  样品名是否可见  样品名显示在图表内或外  样品名字体颜色
funnel.render('06_Funnel.html')
