
'''

在生成部件对象时可以设置对象事件的处理函数，
实现各种“人机交互”功能——让我们继续改进程序，
为按钮对象加入点击事件的处理函数，
把你在输入框输入的文本添加到文本区的现有文本中：

'''

import tkinter as tk


def change(widget, var):
    """
    事件处理函数：改变Text部件的文本
    在widget现有文本末尾插入新的文本var
    """
    widget.config(state="normal")
    widget.insert("end", var + "\n")
    widget.config(state="disabled")


def main():
    """
    主函数：设置窗口部件，指定按钮点击事件处理函数
    """
    window = tk.Tk()
    window.geometry("400x300")
    window.title("简单图形界面程序")
    label = tk.Label(window, text="请输入文本并点击添加")
    label.grid(row=0, column=0)
    entry = tk.Entry(window, width=50)
    entry.grid(row=1, column=0, columnspan=2, padx=20, pady=10)
    text = tk.Text(window, width=50, height=12, background="wheat")
    text.config(state="disabled")
    text.place(x=20, y=100)
    button = tk.Button(window, text="添加",
                       command=lambda: change(text, entry.get()))
    button.grid(row=0, column=1)
    tk.mainloop()


if __name__ == "__main__":
    main()