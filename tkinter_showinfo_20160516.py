#! /usr/bin env python
# _*_ coding:gbk _*_

import tkinter
import tkinter.messagebox

top = tkinter.Tk()

def helloCallBack():
   tkinter.messagebox.showinfo("Hello World")

B = tkinter.Button(top, text ="Hello,dddPython", command = helloCallBack)
B.pack()
top.mainloop()