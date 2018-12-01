import tkinter as tk

window = tk.Tk()  # 生成窗口对象
window.geometry("500x300")  # 设置窗口大小
window.title("简单图形界面程序")  # 设置窗口标题

# 这里可以生成其他部件并放入窗口

'''
#    第一个demo  pack()把它们放进容器对象，默认从上到下放置：
label = tk.Label(window, text="测试标签")
label.pack()
button = tk.Button(window, text="测试按钮")
button.pack(side="bottom")  # 放到容器底部
entry = tk.Entry(window, width=50)  # 输入框宽50字符
entry.pack()
text = tk.Text(window, width=50, height=12, background="wheat")  # 文本区宽50字符高12字符，麦色背景
text.pack()
'''
'''
常用的可视化部件有“标签”（Label）、“按钮”（Button）、“输入框”（Entry）、“文本区”（Text）等等，
这些部件都不能独立存在而是从属于窗口这样的“容器”，
你可以使用特定的布局方法例如pack()把它们放进容器对象，默认从上到下放置：
'''


'''
#    第二个demo  使用网格布局方法grid()可以在同一行放置多个部件，但此方法不可与pack()同时使用。
label = tk.Label(window, text="测试标签")
label.grid(row=0, column=0)  # 标签放在0行0列
button = tk.Button(window, text="测试按钮")
button.grid(row=0, column=1)  # 按钮放在0行1列
entry = tk.Entry(window, width=50)
entry.grid(row=1, column=0, columnspan=2, padx=20, pady=10)  # 输入框在1行0列，横跨两列，横向留空20像素，纵向留空10像素
text = tk.Text(window, width=50, height=12, background="wheat")
text.place(x=20, y=100)  # 文本区放在指定的坐标
'''
'''
还有一种定位布局方法place()指定部件在容器中的绝对坐标（原点在左上角，x轴向右，y轴向下），
以上代码改用grid()和place()调整窗口布局：
'''

tk.mainloop()  # 开始主循环
