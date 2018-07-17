#! /usr/bin/env python
# coding:utf-8

import Tkinter as tk

root = tk.Tk()
root.title('listbox test')
# 存放list的容器
list_frame = tk.Frame(root)
list_frame.grid()
button_frame = tk.Frame(root)
button_frame.grid()

def print_item(event):
    items = lb.curselection()
    for k in items:
        print lb.get(k)

var = tk.StringVar()
var.set(('aa','bb','cc','dd','ee'))

lb = tk.Listbox(list_frame, listvariable=var, selectmode=tk.EXTENDED)
lb.bind('<ButtonRelease-1>', print_item)
lb.grid()

def additem():
    lb.insert(tk.END, v.get())
    v.set('')

v = tk.StringVar()
en = tk.Entry(button_frame, textvariable = v)
en.grid()
b1 = tk.Button(button_frame, text='添加', command=additem)
b1.grid(sticky=tk.W)
b2 = tk.Button(button_frame, text='删除', command = lambda lb=lb:lb.delete(tk.ANCHOR))
b2.grid(sticky=tk.W)
root.mainloop()
