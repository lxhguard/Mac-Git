import tkinter
from tkinter import *
from tkinter import ttk

win = tkinter.Tk()
b=list([])
c=list([])
win.title("纳税人信用指标权重确定")
win.geometry("600x400+200+50")

# 表格1
label1 = ttk.Label(win, text="用户的比较结果表示为矩阵")
label1.pack()
tree1 = ttk.Treeview(win)
tree1.pack()
label2 = ttk.Label(win, text="符号的意义")
label2.pack()
tree2 = ttk.Treeview(win)
tree2.pack()



# 定义列
tree1["columns"] = ("A1", "A2", "A3", "A4", "A5", "A6", "A7", "A8")


# 设置列，列还不显示
tree1.column("A1", width=150)
tree1.column("A2", width=150)
tree1.column("A3", width=150)
tree1.column("A4", width=150)
tree1.column("A5", width=150)
tree1.column("A6", width=150)
tree1.column("A7", width=150)
tree1.column("A8", width=150)

# 设置表头
tree1.heading("A1", text="A1")
tree1.heading("A2", text="A2")
tree1.heading("A3", text="A3")
tree1.heading("A4", text="A4")
tree1.heading("A5", text="A5")
tree1.heading("A6", text="A6")
tree1.heading("A7", text="A7")
tree1.heading("A8", text="A8")

# 添加数据
tree1.insert("", 0, text="A1")
tree1.insert("", 1, text="A2")
tree1.insert("", 2, text="A3")
tree1.insert("", 3, text="A4")
tree1.insert("", 4, text="A5")
tree1.insert("", 5, text="A6")
tree1.insert("", 6, text="A7")
tree1.insert("", 7, text="A8")



# 定义列
tree2["columns"] = ("语言项", "意义")

# 设置列，列还不显示
tree2.column("语言项", width=150)
tree2.column("意义", width=150)

# 设置表头
tree2.heading("语言项", text="语言项")
tree2.heading("意义", text="意义")


# 添加数据
tree2.insert("", 0, text="", values=("S0", "绝对不重要"))
tree2.insert("", 1, text="", values=("S1", "非常不重要"))
tree2.insert("", 2, text="", values=("S2", "不重要"))
tree2.insert("", 3, text="", values=("S3", "较为不重要"))
tree2.insert("", 4, text="", values=("S4", "同等重要"))
tree2.insert("", 5, text="", values=("S5", "较为重要"))
tree2.insert("", 6, text="", values=("S6", "重要"))
tree2.insert("", 7, text="", values=("S7", "非常重要"))
tree2.insert("", 8, text="", values=("S8", "绝对重要"))

name = ["A1"]
ipcode = ['欠税规模']

for i in range(min(len(name), len(ipcode))):  # 写入数据
    tree1.insert('', i, values=(name[i], ipcode[i]))


def treeview_sort_column(tv, col, reverse):  # Treeview、列名、排列方式
    l = [(tv.set(k, col), k) for k in tv.get_children('')]
    l.sort(reverse=reverse)  # 排序方式
    # rearrange items in sorted positions+
    for index, (val, k) in enumerate(l):  # 根据排序后索引移动
        tv.move(k, '', index)
    tv.heading(col, command=lambda: treeview_sort_column(tv, col, not reverse))  # 重写标题，使之成为再点倒序的标题

def set_cell_value(event):  # 双击进入编辑状态
    for item in tree1.selection():
        # item = I001
        item_text = tree1.item(item, "values")
        # print(item_text[0:2])  # 输出所选行的值
    column = tree1.identify_column(event.x)  # 列
    row = tree1.identify_row(event.y)  # 行
    # cn = int(str(column).replace('#', ''))
    # rn = int(str(row).replace('', ''))
    cn = 0
    rn = 0
    entryedit = Text(win, width=10 + (cn - 1) * 16, height=1)
    entryedit.place(x=20 + (cn - 1) * 130, y=20 + rn * 20)

    def saveedit():
        global b
        c=b.copy()
        tree1.set(item, column=column, value=entryedit.get(0.0, "end"))#保存编辑
        a=entryedit.get(0.0, "end")
        a=list(a)
        b=c+a
        #b=d.copy()
        entryedit.destroy()
        okb.destroy()
        print(b)


    okb = ttk.Button(win, text='OK', width=4, command=saveedit)
    okb.place(x=665 + (cn - 1) * 242, y=200 + rn * 20)

def newrow():
    name.append('等待输入数据')
    ipcode.append('等待输入数据')
    tree1.insert('', len(name) - 1, values=(name[len(name) - 1], ipcode[len(name) - 1]))
    tree1.update()
    newb.place(x=0, y=0)
    newb.update()

tree1.bind('<Double-1>', set_cell_value)  # 双击左键进入编辑
newb = ttk.Button(win, text='新建联系人', width=20, command=newrow)
newb.place(x=0, y=0)

for col in tree1["columns"]:  # 绑定函数，使表头可排序
    tree1.heading(col, text=col, command=lambda _col=col: treeview_sort_column(tree1, _col, False))



win.mainloop()



