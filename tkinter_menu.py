#! /usr/bin 
# _*_ coding:utf-8 _*_

import tkinter
top = tkinter.Tk()
top.wm_title('menu reference')

menubar = tkinter.Menu(top)
File_menu = tkinter.Menu(menubar)


Java_menu = tkinter.Menu(menubar)
for item in ['New','Open','Save','Save as ...']:
	Java_menu.add_command(label=item)

C_menu = tkinter.Menu(menubar)
for item in ['New','Open','Save','Save as ...']:
	C_menu.add_command(label=item)

Python_menu = tkinter.Menu(menubar)
for item in ['New','Open','Save','Save as ...']:
	Python_menu.add_command(label=item)

Linux_menu = tkinter.Menu(menubar)
for item in ['New','Open','Save','Save as ...']:
	Linux_menu.add_command(label=item)
	
About_menu = tkinter.Menu(menubar)
for item in ['Version info']:
	About_menu.add_command(label=item)

Check_update_menu = tkinter.Menu(About_menu)
for item in ['from local','from internet']:
	Check_update_menu.add_command(label=item)

menubar.add_cascade(label='File',menu=File_menu)
menubar.add_cascade(label='Java',menu=Java_menu)
menubar.add_cascade(label='C',menu=C_menu)
menubar.add_cascade(label='Python',menu=Python_menu)
menubar.add_cascade(label='Linux',menu=Linux_menu)
menubar.add_cascade(label='About',menu=About_menu)
About_menu.add_cascade(label='Check update',menu=Check_update_menu)

top['menu'] = menubar
top.mainloop()