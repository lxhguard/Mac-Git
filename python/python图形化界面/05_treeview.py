import tkinter.ttk
from tkinter import *

root = Tk()
tree = ttk.Treeview(root, columns=('col1', 'col2', 'col3'))
tree.column('col1', width=100, anchor='center')
tree.column('col2', width=100, anchor='center')
tree.column('col3', width=100, anchor='center')
tree.heading('col1', text='col1')
tree.heading('col2', text='col2')
tree.heading('col3', text='col3')


def onDBClick(event):
    item = tree.selection()[0]
    print("you clicked on ", tree.item(item, "values"))


for i in range(10):
    tree.insert('', i, values=('a' + str(i), 'b' + str(i), 'c' + str(i)))
tree.bind("<Double-1>", onDBClick)

tree.pack()
root.mainloop()

'''
ttk貌似是python自带的。
Treeview本质上是一棵树。
以上是弱化版，也就是我们通常见到的listview
支持事件的绑定，通过tree.bind配合tree.item以及tree.selection()使用，可以针对单击，双击等事件写代码。
'''