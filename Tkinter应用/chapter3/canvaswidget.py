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

tabControl = ttk.Notebook(win) # Create Tab Control
tab1 = ttk.Frame(tabControl) # Create a tab
tabControl.add(tab1, text='Tab 1') # Add the tab
tab2 = ttk.Frame(tabControl) # Add a second tab
tabControl.add(tab2, text='Tab 2') # Make second tab visible
tab3 = ttk.Frame(tabControl) # Add a third tab
tabControl.add(tab3, text='Tab 3') # Make second tab visible
tabControl.pack(expand=1, fill="both") # Pack to make visible

tab3 = tk.Frame(tab3, bg='blue')
tab3.pack()
for orangeColor in range(2):
    canvas = tk.Canvas(tab3, width=150, height=80,
highlightthickness=0, bg='orange')
    canvas.grid(row=orangeColor, column=orangeColor)

win.mainloop()
