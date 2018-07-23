#!/usr/bin/env python
#coding:utf-8
# version:python2.7.15
# windows 10
# reference: python gui cookbook
import Tkinter as tk
import ttk
import ScrolledText as scrolledtext
from Tkinter import Menu
import tkMessageBox as mBox
import oop_gui as tt

class OOP():
    def __init__(self):
        self.win = tk.Tk()
        self.win.title('python gui')
        self.createWidgets()

    # 按钮回调函数
    def ClickMe(self):
        self.action.configure(text="Hello " + self.name.get() +
        ' ' + self.numberChosen.get())

    def _spin(self):
        value = self.spin.get()
        print value
        self.scr.insert(tk.INSERT, value+'\n')

    def checkCallback(self, *ignored_args):
        if self.chVarUn.get():
            self.check3.configure(state='disabled')
        else:
            self.check3.configure(state='normal')
        if self.chVarEn.get():
            self.check2.configure(state='disabled')
        else:
            self.check2.configure(state='normal')

    def radCall(self):
        radSel = self.radVar.get()
        if radSel == 0:
            self.monty2.configure(text=self.colors[0]) # bg无效，只能用于win,但已被其它框架挡住
        elif radSel == 1:
            self.monty2.configure(text=self.colors[1])
        elif radSel == 2:
            self.monty2.configure(text=self.colors[2])

    def _quit(self):
        self.win.quit()
        self.win.destroy()
        exit()

    def _msgBox(self):
        mBox.showinfo(' ', '使用Tkinter的图形界面，于2018')

    def createWidgets(self):
        tabControl = ttk.Notebook(self.win)
        tab1 = ttk.Frame(tabControl)
        tabControl.add(tab1, text="Tab 1")
        tab2 = ttk.Frame(tabControl)
        tabControl.add(tab2, text="Tab 2")
        tabControl.grid(padx=5, pady=5)

        # 创建框架方便布局
        self.monty = ttk.LabelFrame(tab1, text=" self.monty python ")
        self.monty.grid(column=0, row=0, padx=8, pady=4)

        self.monty2 = ttk.LabelFrame(tab2, text=" the snake ")
        self.monty2.grid(column=0, row=0, padx=8, pady=4)

        # 创建按钮
        self.action = ttk.Button(self.monty, text="Click Me!", command=self.ClickMe)
        self.action.grid(column=2, row=1)

        # 创建标签
        ttk.Label(self.monty, text="Enter a name:").grid(column=0, row=0)
        ttk.Label(self.monty, text="Choose a number:").grid(column=1, row=0)

        # 创建输入框
        self.name = tk.StringVar()
        self.nameEntered = ttk.Entry(self.monty, width=12, textvariable=self.name)
        self.nameEntered.focus() #place a cursor
        self.nameEntered.grid(column=0, row=1)

        # 创建下拉菜单
        number = tk.StringVar()
        self.numberChosen = ttk.Combobox(self.monty, width=12, textvariable=number)
        # self.numberChosen = ttl.Combobox(self.monty, width=12, textvariable=number, state='readonly') # 禁止自己填写
        self.numberChosen["values"] = [1, 2, 4, 42, 100]
        self.numberChosen.grid(column=1, row=1, padx=8, pady=4)
        self.numberChosen.current(1) #选择默认value

        # 创建滚动文本框，定义长宽
        scrolW = 30
        scrolH = 5
        # wrap=tk.WORD防止单词在行末被分割，直接换到下一行
        self.scr = scrolledtext.ScrolledText(self.monty, width=scrolW, height=scrolH, wrap=tk.WORD)
        # 扩充所占单元格布局，合并3格
        self.scr.grid(column=0, columnspan=3, sticky="WE")

        #创建3个checkbutton
        chVarDis = tk.IntVar()
        check1 = tk.Checkbutton(self.monty2, text="Disabled", variable=chVarDis, state="disabled")
        check1.select()
        check1.grid(column=0, row=0, sticky=tk.W)

        chVarUn = tk.IntVar()
        check2 = tk.Checkbutton(self.monty2, text="Unchecked", variable=chVarUn)
        check2.deselect()
        check2.grid(column=1, row=0, sticky=tk.W)

        chVarEn = tk.IntVar()
        check3 = tk.Checkbutton(self.monty2, text="Enabled", variable=chVarEn)
        check3.select()
        check3.grid(column=2, row=0, sticky=tk.W)


        self.colors = ["Blue", "Gold", "Red"]
        self.radVar = tk.IntVar()
        self.radVar.set(99)
        for col in range(3):
            curRad = "rad" + str(col)
            curRad = tk.Radiobutton(self.monty2, text=self.colors[col], variable=self.radVar, value=col, command=self.radCall)
            curRad.grid(column=col, row=1, sticky=tk.W)
            tt.createToolTip(curRad, 'This is Radiobutton control')

        # 创建菜单栏
        menuBar = Menu(self.win)
        self.win.config(menu=menuBar)

        # 向栏目中添加各类菜单
        fileMenu = Menu(menuBar, tearoff=0) # tearoff删除第一行虚线
        fileMenu.add_command(label="New")
        fileMenu.add_separator()
        fileMenu.add_command(label="Exit", command=self._quit)
        menuBar.add_cascade(label="File", menu=fileMenu)

        helpMenu = Menu(menuBar, tearoff=0) # tearoff删除第一行虚线
        helpMenu.add_command(label="About", command=self._msgBox)
        menuBar.add_cascade(label="Help", menu=helpMenu)

        self.spin = tk.Spinbox(tab1, values=(1,2,4,8,16), width=5, bd=8, command=self._spin)
        self.spin.grid()
        tt.createToolTip(self.spin, 'This is a Spin control.')
        tt.createToolTip(self.nameEntered, 'This is an Entry control')
        tt.createToolTip(self.action, 'This is a Button control')
        tt.createToolTip(self.scr, 'This is a ScrolledText control')

oop = OOP()
oop.win.mainloop()
