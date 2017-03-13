#! usr/bin
# _*_ coding:utf-8 _*_

#求0~7所能组成奇数的个数

n = input('please enter a number(0<n<50)  :')
a=int(n)

while True:
	if a>0 and a<50 :
		for i in range(a):
			print('*',end='')
		print('\n')
		a = int(input('compare done,you can enter another number :' ))
		
	else :
		a = int(input('you have enter a wrong number,please enter again :'))
