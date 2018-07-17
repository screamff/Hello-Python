#! /usr/bin/env python
# coding:utf-8
import Tkinter as tk

def isLogin(uname, pword):
    if uname == "python" and pword == "python":
        print "successfully logged in "
        out.insert(tk.END, "successfully logged in! \n")
    else:
        print "wrong"
        out.insert(tk.END, "wrong!")

root = tk.Tk()
root.title("entry test")
userinfo_frame = tk.Frame(root)
userinfo_frame.grid()

user_frame = tk.Frame(userinfo_frame)
user_frame.grid()

user_label = tk.Label(user_frame, text="username:",)
user_label.grid()
username =tk.Entry(user_frame, width=40)
username.grid()

pass_frame = tk.Frame(userinfo_frame)
pass_frame.grid()

pass_label = tk.Label(pass_frame, text="password")
pass_label.grid()
password = tk.Entry(pass_frame, width=40, show="$")
password.grid()

btn_frame = tk.Frame(userinfo_frame)
btn_frame.grid()
btn = tk.Button(btn_frame, text='log in', command=lambda isLogin=isLogin: isLogin(username.get(), password.get()))
btn.grid()

out = tk.Text(btn_frame, width=40)
out.insert(tk.END, "welcome \n")
out.grid()

root.mainloop()
