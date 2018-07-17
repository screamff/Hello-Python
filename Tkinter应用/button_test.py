#!/usr/bin/env python
#coding:utf-8
# version:python2.7.15
# windows 10
# reference: python gui cookbook
import Tkinter as tk
import ttk

win = tk.Tk()
win.title("Python gui")

aLabel = ttk.Label(win, text="A label")
aLabel.grid(column=0, row=0)

def ClickMe():
    action.configure(text="** I have been Clicked  **")
    aLabel.configure(foreground="red")

action = ttk.Button(win, text="Click Me", command=ClickMe)
action.grid(column=1, row=0)

win.mainloop()
