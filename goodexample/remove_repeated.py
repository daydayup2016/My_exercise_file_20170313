#! /usr/bin 
# _*_ coding:utf-8 _*_
import sys
print('you have input :',sys.argv)
for i in range(1,len(sys.argv)-1):
	print(i,'para is',sys.argv[i])

def useage():
	print('input a list , then return a new list without repeated item \
	such as :remove_repeated(yourlistname)')
	
def remove_repeated(listt):
	if listt is None:
		print('parameter error')
		useage()

	listnew = []
	for i in listt:
		if i not in listnew:
			listnew.append(i)
	return listnew
	
c=[1,2,3,2,3,3,4,5,6,4,6,7,6]

if len(sys.argv) == 1 :
	dd = remove_repeated(c)
else:
	dd = remove_repeated(sys.argv[1])
print('result is ',dd)
