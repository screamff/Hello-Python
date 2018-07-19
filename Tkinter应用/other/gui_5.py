#!/usr/bin/env python
#coding:utf-8
import Tkinter as tk
import tkFileDialog as File

def get_filename():
    filename = File.askopenfilename(initialdir = "D:\pythonwork\gui/")
    print filename

window = tk.Tk()
window.title('test')
# window.minsize(300,200)
quitButton = tk.Button(window, text='Quit',command=quit)
getnameButton = tk.Button(window, text='选择文件',command=get_filename)
# print getnameButton.keys()
quitButton.grid()
getnameButton.grid()
window.mainloop()
