#! C:\Program Files\Python35\pythonw.exe
# _*_ coding:utf-8 _*_

import tkinter
import tkinter.messagebox
login_data = {'quanbo':'1234','zhengbin':'4321','cc':'2121','dd':'3343'}
login_data_username = login_data.keys()
print(login_data_username)

def infoCheck():
	str_username = entry_username.get()
	str_password = entry_password.get()
	if str_username in login_data_username:
		if str_password == login_data[str_username]:
			tkinter.messagebox.showinfo('登录成功','密码正确,登录成功,oh ,yeah \n5s 后将进入系统，请等待')
		else:
			tkinter.messagebox.showinfo('登录失败','密码不正确,登录失败，oh no')
	else:
		tkinter.messagebox.showinfo('用户出错','系统无此账户,登录失败，oh no')
top = tkinter.Tk()
top.wm_title('欢迎登录')
top.geometry('150x100')

label1 = tkinter.Label(top,text='账号：',fg='blue')
label1.grid(row=0,column=0)
entry_username = tkinter.Entry(top)
entry_username.grid(row=0,column=1)
label2 = tkinter.Label(top,text='密码：',fg='blue')
label2.grid(row=1,column=0)
entry_password= tkinter.Entry(top)
entry_password.grid(row=1,column=1)
button1 = tkinter.Button(top,text='确定',command=infoCheck)
button1.grid(row=2,column=0)
button2 = tkinter.Button(top,text='取消(退出)',command=top.quit)
button2.grid(row=2,column=1)
top.mainloop()
