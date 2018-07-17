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
    action.configure(text="Hello " + name.get())

action = ttk.Button(win, text="Click Me", command=ClickMe)
# action.configure(state='disabled') # Disable the Button Widget
action.grid(column=1, row=1)

ttk.Label(win, text="Enter a name:").grid(column=0, row=0)

name = tk.StringVar()
nameEntered = ttk.Entry(win, width=12, textvariable=name)
nameEntered.focus() #place a cursor
nameEntered.grid(column=0, row=1)

win.mainloop()
