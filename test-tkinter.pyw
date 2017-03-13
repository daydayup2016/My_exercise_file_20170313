
# _*_ coding:utf-8 _*_

def addLabel():
	global root
	newLabel = tkinter.Label(root,text='love you')
	newLabel.pack()
	
import tkinter
root = tkinter.Tk()
root.wm_title('daydayup to you,你好 ')

label1 = tkinter.Label(root,text='here is my steps for python study，大蟒蛇',bg='red')
label1.pack()
label2 = tkinter.Label(root,text='here is my steps for python study，，大蟒',bg='blue')
label2.pack()
label3 = tkinter.Label(root,text='here is my steps for python study，巨蟒',bg='green')
label3.pack()

button1 = tkinter.Button(root,text='add label',command=addLabel)
button1.pack()

root.mainloop()

