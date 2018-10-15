#!/usr/bin/env python
# coding:utf-8
# version:python2.7.15
# windows 10
# reference: python gui cookbook
import Tkinter as tk
import ttk

win = tk.Tk()
win.title("Python gui")


def ClickMe():
    action.configure(text="Hello " + name.get() + ' ' + numberChosen.get())


action = ttk.Button(win, text="Click Me!", command=ClickMe)
action.grid(column=2, row=1)

ttk.Label(win, text="Enter a name:").grid(column=0, row=0)
ttk.Label(win, text="Choose a number:").grid(column=1, row=0)

name = tk.StringVar()
nameEntered = ttk.Entry(win, width=12, textvariable=name)
nameEntered.focus()  # place a cursor
nameEntered.grid(column=0, row=1)

number = tk.StringVar()
numberChosen = ttk.Combobox(win, width=12, textvariable=number)
# numberChosen = ttl.Combobox(win, width=12,
#                             textvariable=number, state='readonly')
# 禁止自己填写
numberChosen["values"] = [1, 2, 4, 42, 100]
numberChosen.grid(column=1, row=1)
numberChosen.current(1)  # 选择默认value

# 创建3个checkbutton
chVarDis = tk.IntVar()
check1 = tk.Checkbutton(win, text="Disabled",
                        variable=chVarDis, state="disabled")
check1.select()
check1.grid(column=0, row=2, sticky=tk.W)

chVarUn = tk.IntVar()
check2 = tk.Checkbutton(win, text="Unchecked", variable=chVarUn)
check2.deselect()
check2.grid(column=1, row=2, sticky=tk.W)

chVarEn = tk.IntVar()
check3 = tk.Checkbutton(win, text="Enabled", variable=chVarEn)
check3.select()
check3.grid(column=2, row=2, sticky=tk.W)

win.mainloop()
