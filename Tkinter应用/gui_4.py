#!/usr/bin/env python
#coding:utf-8
import Tkinter as tk
import tkFileDialog as File

def get_filename():
    filename = File.askopenfilename()
    print filename

class Application(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.grid()
        self.createWidgets()
        # self.get_filename()

    def createWidgets(self):
        self.quitButton = tk.Button(self, text='Quit',command=self.quit)
        self.getnameButton = tk.Button(self, text='选择文件',command=get_filename,default=tk.DISABLED)
        self.quitButton.grid()
        self.getnameButton.grid()

    # def get_filename(self):
    #     self.filename = File.askopenfilename()
    #     return self.filename

app = Application()
app.master.title('Sample application')
app.mainloop()
