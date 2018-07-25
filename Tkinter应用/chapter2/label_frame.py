#!/usr/bin/env python
#coding:utf-8
# version:python2.7.15
# windows 10
# reference: python gui cookbook
import Tkinter as tk
import ttk
import ScrolledText as scrolledtext

# 创建主窗口
win = tk.Tk()
win.title("Python gui")

# 按钮回调函数
def ClickMe():
    action.configure(text="Hello " + name.get() + ' ' + numberChosen.get())

# 创建按钮
action = ttk.Button(win, text="Click Me!", command=ClickMe)
action.grid(column=2, row=1)

# 创建标签
ttk.Label(win, text="Enter a name:").grid(column=0, row=0)
ttk.Label(win, text="Choose a number:").grid(column=1, row=0)

# 创建输入框
name = tk.StringVar()
nameEntered = ttk.Entry(win, width=12, textvariable=name)
nameEntered.focus() #place a cursor
nameEntered.grid(column=0, row=1)

# 创建下拉菜单
number = tk.StringVar()
numberChosen = ttk.Combobox(win, width=12, textvariable=number)
# numberChosen = ttl.Combobox(win, width=12, textvariable=number, state='readonly') # 禁止自己填写
numberChosen["values"] = [1, 2, 4, 42, 100]
numberChosen.grid(column=1, row=1)
numberChosen.current(1) #选择默认value

#创建3个checkbutton
chVarDis = tk.IntVar()
check1 = tk.Checkbutton(win, text="Disabled", variable=chVarDis, state="disabled")
check1.select()
check1.grid(column=0, row=2, sticky=tk.W)

chVarUn = tk.IntVar()
check2 = tk.Checkbutton(win, text="Unchecked", variable=chVarUn)
check2.deselect()
check2.grid(column=1, row=2, sticky=tk.W)

chVarEn = tk.IntVar()
check3 = tk.Checkbutton(win, text="Enabled", variable=chVarEn)
check3.select()
check3.grid(column=2, row=2, sticky=tk.W)

# 使用列表循环改写单选按钮
colors = ["Blue", "Gold", "Red"]

def radCall():
    radSel = radVar.get()
    if radSel == 0:
        win.configure(background=colors[0])
    elif radSel == 1:
        win.configure(background=colors[1])
    elif radSel == 2:
        win.configure(background=colors[2])

radVar = tk.IntVar()
radVar.set(99)
for col in range(3):
    curRad = "rad" + str(col)
    curRad = tk.Radiobutton(win, text=colors[col], variable=radVar, value=col, command=radCall)
    curRad.grid(column=col, row=3, sticky=tk.W)


# 创建滚动文本框，定义长宽
scrolW = 30
scrolH = 3
# wrap=tk.WORD防止单词在行末被分割，直接换到下一行
scr = scrolledtext.ScrolledText(win, width=scrolW, height=scrolH, wrap=tk.WORD)
# 扩充所占单元格布局，合并3格
scr.grid(column=0, columnspan=3, sticky="WE")

# 建立单独框架,适当扩充边界
labelFrame = ttk.LabelFrame(win, text="labels in a frame")
labelFrame.grid(column=0, row=7, padx=20, pady=40)
ttk.Label(labelFrame, text="Label1").grid(column=0, row=0)
ttk.Label(labelFrame, text="Label2").grid(column=0, row=1)
ttk.Label(labelFrame, text="Label3").grid(column=0, row=2)
# 批量布局一个框架里的部件
for child in labelFrame.winfo_children():
    child.grid_configure(padx=8, pady=4)


win.mainloop()
