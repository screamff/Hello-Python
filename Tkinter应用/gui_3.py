#!/usr/bin/env python
import Tkinter as tk

class Application(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.grid(sticky=tk.N+tk.S+tk.E+tk.W)
        self.createWidgets()

    def createWidgets(self):
        top = self.winfo_toplevel()
        top.rowconfigure(0,weight=1)
        top.columnconfigure(0,weight=1)
        self.rowconfigure(0,weight=1)
        self.columnconfigure(0,weight=1)
        self.quit = tk.Button(self, text='Quit',command=self.quit)
        self.quit.grid(row=0, column=0,sticky=tk.N+tk.S+tk.E+tk.W)

app = Application()
app.master.title('Sample application')
app.mainloop()
