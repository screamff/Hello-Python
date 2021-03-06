#!/usr/bin/env python
#coding:utf-8
# version:python2.7.15
# windows 10
# reference: python gui cookbook
import Tkinter as tk
import ttk
import ScrolledText as scrolledtext

# 创建主窗口
win = tk.Tk()
win.title("Python gui")

# 创建框架方便布局
monty = ttk.LabelFrame(win, text=" monty python")
monty.grid(column=0, row=0)

# 按钮回调函数
def ClickMe():
    action.configure(text="Hello " + name.get() + ' ' + numberChosen.get())

# 创建按钮
action = ttk.Button(monty, text="Click Me!", command=ClickMe)
action.grid(column=2, row=1, padx=8, pady=4)

# 创建标签
ttk.Label(monty, text="Enter a name:").grid(column=0, row=0, padx=8, pady=4)
ttk.Label(monty, text="Choose a number:").grid(column=1, row=0, padx=8, pady=4)

# 创建输入框
name = tk.StringVar()
nameEntered = ttk.Entry(monty, width=12, textvariable=name)
nameEntered.focus() #place a cursor
nameEntered.grid(column=0, row=1, padx=8, pady=4)

# 创建下拉菜单
number = tk.StringVar()
numberChosen = ttk.Combobox(monty, width=12, textvariable=number)
# numberChosen = ttl.Combobox(monty, width=12, textvariable=number, state='readonly') # 禁止自己填写
numberChosen["values"] = [1, 2, 4, 42, 100]
numberChosen.grid(column=1, row=1, padx=8, pady=4)
numberChosen.current(1) #选择默认value

def _spin():
    value = spin.get()
    scr.insert(tk.INSERT, value+'\n')

# 创建选值框
# spin = tk.Spinbox(monty, from_=0, to=10, width=5, bd=8, command=_spin)
spin = tk.Spinbox(monty, values=(1,2,4,8,16), width=5, bd=8, command=_spin, relief=tk.GROOVE)
spin2 = tk.Spinbox(monty, values=(1,2,4,8,16), width=5, bd=8, command=_spin, relief=tk.SOLID)
spin3 = tk.Spinbox(monty, values=(1,2,4,8,16), width=5, bd=8, command=_spin, relief=tk.RIDGE)
spin.grid(column=0, row=2)
spin2.grid(column=1, row=2)
spin3.grid(column=2, row=2)

# 创建滚动文本框，定义长宽
scrolW = 30
scrolH = 3
# wrap=tk.WORD防止单词在行末被分割，直接换到下一行
scr = scrolledtext.ScrolledText(monty, width=scrolW, height=scrolH, wrap=tk.WORD)
# 扩充所占单元格布局，合并3格
scr.grid(column=0, columnspan=3, sticky="WE")

win.mainloop()
