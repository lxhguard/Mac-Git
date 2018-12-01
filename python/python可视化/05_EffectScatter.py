from pyecharts import EffectScatter

es = EffectScatter("动态散点图各种图形示例")
es.add("1", [10], [10], symbol_size=20, effect_scale=3.5, effect_period=3, symbol="pin")
#  名字 横坐标 纵坐标 标志大小 跑的弧度角度  扩散时间或者说周期 标志类型
es.add("2", [20], [20], symbol_size=12, effect_scale=4.5, effect_period=4,symbol="rect")
es.add("3", [30], [30], symbol_size=30, effect_scale=5.5, effect_period=5,symbol="roundRect")
es.add("4", [40], [40], symbol_size=10, effect_scale=6.5, effect_brushtype='fill',symbol="diamond")
es.add("5", [50], [50], symbol_size=16, effect_scale=5.5, effect_period=3,symbol="arrow")
es.add("6", [60], [60], symbol_size=6, effect_scale=2.5, effect_period=3,symbol="triangle")
es.render('05_EffectScatter.html')
