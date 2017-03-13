#! usr/bin
# _*_ coding:utf-8 _*_



def my_math_square(x):
	if x == None:
		print('at least one para is needed !')
	else:
		return x*x
		
if __name__ == '__main__':
	print('test',my_math_square(10))


def my_math_lifang(x):
	if x == None:
		print('at least one para is needed !')
	else:
		print('__name__ is :',__name__)
		return x*x*x

if __name__ == '__main__':
	print('lifang',my_math_lifang(5))