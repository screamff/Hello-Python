#!/usr/bin/env python
#coding:utf-8
import Tkinter as tk
import tkFileDialog as File
import time
import re
import xlsxwriter as xls
import win32gui
import win32api
import win32con

master = tk.Tk()

def save_file():
    xl_name = time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime())
    new = win32gui.FindWindow(None,'Data Storage')
    win32gui.SetForegroundWindow(new)
    time.sleep(0.1)
    win32api.keybd_event(65,0,0,0)      #
    win32api.keybd_event(65,0,win32con.KEYEVENTF_KEYUP,0)
    time.sleep(0.1)
    save = win32gui.FindWindow(None,'Save File'.decode('utf-8'))
    # win32gui.SetForegroundWindow(save)
    dlg = win32gui.FindWindowEx(save, None, 'Edit', None)
    win32gui.SendMessage(dlg,win32con.WM_SETTEXT,None,xl_name)
    win32api.keybd_event(13,0,0,0)      #
    win32api.keybd_event(13,0,win32con.KEYEVENTF_KEYUP,0)

def get_filename():
    """
    打开对话框获取文件路径,将其传至输入框
    """
    filename = File.askopenfilename(initialdir="D:\pythonwork",title='知其来处',filetypes=[("csv file", "*.csv"),("all files","*.*")])
    content.set(filename)

def save_filename():
    """
    设置文件保存路径
    """
    savename = File.asksaveasfilename(initialdir="D:\pythonwork",title="择其去处",filetypes=[("xlsx file","*.xlsx"),("all files","*.*")],defaultextension='.xlsx')
    content02.set(savename)

def make_lable():
    """
    建立标签
    """
    message01 = tk.Label(master, text='上限阈值mm:',height=2)
    message02 = tk.Label(master, text='下限阈值mm:',height=2)
    message03 = tk.Label(master, text='输入文件路径:',height=2)
    message04 = tk.Label(master, text='保存处理文件路径:',height=2)
    message01.grid(row=0, column=0)
    message02.grid(row=1, column=0)
    message03.grid(row=2, column=0)
    message04.grid(row=3, column=0)

def make_button():
    """
    建立按钮
    """
    getnameButton = tk.Button(master, text='浏览文件夹',command=get_filename)
    getnameButton.grid(row=2, column=2)

    savepathButton = tk.Button(master, text="保存至...",command=save_filename)
    savepathButton.grid(row=3, column=2)

    autosaveButton = tk.Button(master, text="自动保存原始数据",command=save_file)
    autosaveButton.grid(row=5, column=1)


    analizeButton = tk.Button(master, text="开始计算", command=data_analize)
    analizeButton.grid()

def tran(txt):
    return float(txt)

#写入路线程序
def route(data,worksheet,x=0,y=0):
    while y<14:
        worksheet.write(x,y,data[y][x])
        x += 1
        if x == 14:
            x=0
            y+=1

def data_analize():
    f = open(e3.get())
    new = f.read()
    #筛选中间的over,并且替换成0
    over = re.compile(r'\d\n(#over)\n.?\d')
    error = over.findall(new)
    no_over = re.sub(r'#[-]OVER','1',new)
    #对替换完成后的内容列表化
    raw_list = re.split(r'\n+', no_over)
    #对所有数据格式化
    list = map(tran, raw_list[4:-2])
    data = []
    flag = 0
    for i in range(0, len(list)):
        if list[i]>float(e1.get()) and flag==0:
            a = i
            flag = 1
        if float(e2.get())>list[i] and flag==1:
            b = i
            value = max(list[a:b])
            flag = 0
            data.append(value)
    print "numbers of data :",len(data)
    print "errors of #over:",len(error)
    new_data=[]
    for i in range(len(data),588):
        data.append(0)

    for i in range(0,14):
        max_list = max(data[14*i*3:14*(i*3+1)],data[14*(i*3+1):14*(i*3+2):-1],data[14*(i*3+2):14*(i+3)])
        if i/2*2==i:
            new_data.append(max_list)#14x14 table
        else:
            new_data.append(max_list[::-1])

    workbook = xls.Workbook(e4.get())
    worksheet = workbook.add_worksheet()
    route(new_data,worksheet)
    workbook.close()
    f.close()

e1 = tk.Entry(master,width=10)
e1.grid(row=0, column=1)
e2 = tk.Entry(master,width=10)
e2.grid(row=1, column=1)
content = tk.StringVar()
e3 = tk.Entry(master,  textvariable=content, width=50)
content.set('D:\pythonwork')
e3.grid(row=2, column=1)
content02 = tk.StringVar()
e4 = tk.Entry(master, textvariable=content02, width=50)
content02.set('D:\pythonwork')
e4.grid(row=3, column=1)

make_lable()
make_button()
master.title("Data Analize 1.0.2")
master.mainloop(0)
