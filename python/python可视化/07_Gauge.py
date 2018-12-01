from pyecharts import Gauge

gauge = Gauge("仪表盘示例")
gauge.add("业务指标", "完成率", 70)
gauge.show_config()
gauge.render('07_Gauge.html')