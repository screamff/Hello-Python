#!/usr/bin/env python
#coding:utf-8
# version:python2.7.15
# windows 10
# reference: python gui cookbook
import Tkinter as tk
import ttk
import tkMessageBox as mBox
from Tkinter import Menu

# 创建主窗口
win = tk.Tk()
win.title("Python gui")

def _msgBox():
    # mBox.showinfo("python信息提示框", "a python gui created using tkinter:\n The year is 2018")
    # mBox.showwarning("python警告框",
    # 'a python gui created using tkinter:\n Error:Houston~we do have a serious problem!')
    answer = mBox.askyesno("", "Are you sure to do this?")
    print answer

# 创建菜单栏
menuBar = Menu(win)
win.config(menu=menuBar)

# 向栏目中添加各类菜单
fileMenu = Menu(menuBar, tearoff=0) # tearoff删除第一行虚线
fileMenu.add_command(label="New")
fileMenu.add_separator()
fileMenu.add_command(label="Exit")
menuBar.add_cascade(label="File", menu=fileMenu)

helpMenu = Menu(menuBar, tearoff=0) # tearoff删除第一行虚线
helpMenu.add_command(label="About", command=_msgBox)
menuBar.add_cascade(label="Help", menu=helpMenu)

win.mainloop()
