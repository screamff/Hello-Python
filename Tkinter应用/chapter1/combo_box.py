#!/usr/bin/env python
#coding:utf-8
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
nameEntered.focus() #place a cursor
nameEntered.grid(column=0, row=1)

number = tk.StringVar()
numberChosen = ttk.Combobox(win, width=12, textvariable=number)
# numberChosen = ttl.Combobox(win, width=12, textvariable=number, state='readonly') # 禁止自己填写
numberChosen["values"] = [1, 2, 4, 42, 100]
numberChosen.grid(column=1, row=1)
numberChosen.current(1) #选择默认value

win.mainloop()
