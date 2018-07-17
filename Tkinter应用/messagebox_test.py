#! /usr/bin/env python
# coding:utf-8

import Tkinter as tk
import tkMessageBox as messagebox

str1=("showinfo", "showwarning", "showerror", "askquestion", "askokcancel", "askyesno", "askretrycancel")

def showMsg(str):
    print str
    if str == str1[0]:
        messagebox.showinfo("showinfo","信息提示框！")
    elif str == str1[1]:
        messagebox.showwarning("showwarning","警告框！")
    elif str == str1[2]:
        messagebox.showerror("showerror","错误信息框！")
    elif str == str1[3]:
        if messagebox.askquestion("askquestion","askquestion提示框") == messagebox.YES:
            messagebox.showinfo("yes","你点了yes!")
        else:
            messagebox.showinfo("no","你点了no")
    elif str == str1[4]:
        if messagebox.askokcancel("askokcancel","askokcancel提示框"):
            messagebox.showinfo("OK","你点Ok")
        else:
            messagebox.showwarning("cancel","你点了cancel")
    elif str == str1[5]:
        print messagebox.askyesno("askyesno","askyesno提示框")
    elif str == str1[6]:
        print messagebox.askretrycancel("askretrycancel","askretrycancel提示框")

root = tk.Tk()
root.title("messagebox 弹出对话框使用例子")

show_frame = tk.Frame(root)
show_frame.pack(fill=tk.X, side=tk.TOP)
btn1= tk.Button(show_frame, text=str1[0],command=lambda showMsg = showMsg : showMsg(str1[0]) ).pack(side=tk.LEFT)
btn2= tk.Button(show_frame, text=str1[1],command=lambda showMsg = showMsg : showMsg(str1[1]) ).pack(side=tk.LEFT)
btn3= tk.Button(show_frame, text=str1[2],command=lambda showMsg = showMsg : showMsg(str1[2]) ).pack(side=tk.LEFT)

asky_frame = tk.Frame(root)
asky_frame.pack(fill=tk.X,side=tk.TOP)
bt4 = tk.Button(asky_frame,text=str1[3],command=lambda showMsg = showMsg : showMsg(str1[3]) ).pack(side=tk.LEFT)
bt5 = tk.Button(asky_frame,text=str1[4],command=lambda showMsg = showMsg : showMsg(str1[4]) ).pack(side=tk.LEFT)
bt6 = tk.Button(asky_frame,text=str1[5],command=lambda showMsg = showMsg : showMsg(str1[5]) ).pack(side=tk.LEFT)
bt7 = tk.Button(asky_frame,text=str1[6],command=lambda showMsg = showMsg : showMsg(str1[6]) ).pack(side=tk.LEFT)
root.mainloop()
