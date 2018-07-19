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

scrollbar = tk.Scrollbar(win, orient=tk.VERTICAL,)
lb = tk.Listbox(win, selectmode=tk.EXTENDED, bg='gray', xscrollcommand=scrollbar.set)
scrollbar.grid(sticky='E')
lb.selection_anchor(tk.END)
lb.grid()

def huge_number():
    for i in range(3):
        lb.insert(0, i)

ttk.Button(win, text='start', command=huge_number).grid()
win.mainloop()
