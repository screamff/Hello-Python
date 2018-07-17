#! /usr/bin/env python
# coding:utf=8
import Tkinter as tk
def callback():
    print 'called the callback'

root = tk.Tk()
root.title('This is a test window!')
root.geometry('500x300+300+300')

menu = tk.Menu(root)
root.config(menu=menu)
filemenu = tk.Menu(menu)
menu.add_cascade(label='File', menu=filemenu)

filemenu.add_command(label='New', command=callback)
filemenu.add_command(label='Open', command=callback)
filemenu.add_checkbutton(label='checkbutton')
filemenu.add_separator()
filemenu.add_radiobutton(label='radiobutton')
filemenu.add_separator()
filemenu.add_command(label='Exit', command=callback)

helpmenu = tk.Menu(menu)
menu.add_cascade(label='help', menu=helpmenu)
helpmenu.add_command(label='About...', command=callback)

#右键弹出菜单
def popup(event):
    menu.post(event.x_root, event.y_root)

root.bind('<Button-3>', popup)
root.mainloop()
