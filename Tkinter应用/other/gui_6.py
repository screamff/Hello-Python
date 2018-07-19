#!/usr/bin/env python
#coding:utf-8
import Tkinter as tk
import tkFileDialog as File
master = tk.Tk()

def get_filename():
    filename = File.askopenfilename(filetypes=[("yahaha","*.py")])
    content.set(filename)

getnameButton = tk.Button(master, text='浏览',command=get_filename)


message01 = tk.Label(master, text='上限阈值mm:',height=2)
message02 = tk.Label(master, text='下限阈值mm:',height=2)
message03 = tk.Label(master, text='输入文件路径:',height=2)
message04 = tk.Label(master, text='保存处理文件路径:',height=2)
message01.grid(row=0, column=0)
message02.grid(row=1, column=0)
message03.grid(row=2, column=0)
message04.grid(row=3, column=0)
e = tk.Entry(master,width=10)
e.grid(row=0, column=1)
e2 = tk.Entry(master,width=10)
e2.grid(row=1, column=1)
content = tk.StringVar()
e3 = tk.Entry(master,  textvariable=content, width=50)
content.set(20)

e3.grid(row=2, column=1)
getnameButton.grid(row=2, column=2)
e4 = tk.Entry(master,width = 50)
e4.grid(row=3, column=1)

def callback():
    print e.get()

b = tk.Button(master, text='get', width=10, command=callback)
b.grid()

master.mainloop()
