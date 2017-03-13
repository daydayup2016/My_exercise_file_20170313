#! /usr/bin env python
# _*_ coding:gbk _*_

import tkinter
def Resize(ev='Null'):
	label.config(font='Helvetica -%d bold' % scale.get())
def hQueren(ev='null'):
	Queren = tkinter.Tk()
	Queren.geometry('130x80') 
	label=tkinter.Label(Queren,text='are you sure?',fg='red',font='Helvetica -13 bold')
	label.pack(fill='x',expand=1)

top = tkinter.Tk()
top.geometry('600x400')
label=tkinter.Label(top,text='Hello ,love my python!',fg='green',font='Helvetica -12 bold')
label.pack(fill='y',expand=1)

scale=tkinter.Scale(top,from_=10,to=50,orient='horizontal',command=Resize)
scale.set(30) 
scale.pack(fill='x',expand=1)

quit=tkinter.Button(top,text='QUIT',command=top.quit,bg='blue',activeforeground='white',activebackground='red',height='5',width='20')
quit.pack()

Queren=tkinter.Button(top,text='Queren',command=hQueren,bg='purple',height='5',width='20')
Queren.pack()

tkinter.mainloop()