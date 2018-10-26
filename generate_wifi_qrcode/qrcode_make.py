#! /usr/bin/env python
# coding:utf-8
import qrcode
import Tkinter as tk


def create_img():
    name = entry_name.get()
    password = entry_password.get()
    raw_code = 'WIFI:T:WPA;S:' + name + ';P:' + password + ';;'
    img = qrcode.make(raw_code)
    print raw_code
    img.save(entry_img.get()+r'.png')
    img.show()


if __name__ == '__main__':
    master = tk.Tk()
    # wifi名字输入
    label_name = tk.Label(master, text='wifiname:', height=2)
    entry_name = tk.StringVar()
    entry_name_widget = tk.Entry(master, textvariable=entry_name, width=20)
    label_name.grid(row=0, column=0)
    entry_name_widget.grid(row=0, column=1)
    # wifi密码输入
    label_password = tk.Label(master, text='password:', height=2)
    entry_password = tk.StringVar()
    entry_password_widget = tk.Entry(master,
                                     textvariable=entry_password, width=20)
    label_password.grid(row=1, column=0)
    entry_password_widget.grid(row=1, column=1)
    # 图片名字
    label_img = tk.Label(master, text='image-name:', height=2)
    entry_img = tk.StringVar()
    entry_img_widget = tk.Entry(master, textvariable=entry_img, width=20)
    label_img.grid(row=2, column=0)
    entry_img_widget.grid(row=2, column=1)
    button_save = tk.Button(master, text='create', command=create_img)
    button_save.grid(row=2, column=2)
    master.mainloop()
