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
win.withdraw()
mBox.showinfo("python信息提示框", "a python gui created using tkinter:\n The year is 2018")
