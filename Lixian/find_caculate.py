#! usr/bin
# _*_ coding:utf-8 _*_

'''
This is a function to calculate how many times that a specific object appear
'''
def find_calculate(list):
	# just simple check input
	if list == None :
		print('you have not input anything,please check...')
	else:
		print('you have input:',list)	
	#find all object appear from input list
	list_new = []
	for i in list:
		if i not in list_new:
			list_new.append(i)
	#create a dictionary to show all object and its times
	dict = {}
	dict = dict.fromkeys(tuple(list_new))
	# calculate
	flag = 0
	for i in list_new:
		for j in list:
			if i == j:
				flag += 1
		print('object',i,'times:',flag)
		dict[i] = flag
		flag = 0

	print(dict)
	
if __name__ == '__main__':
	find_calculate([1,2,5,3,4,5,3,2,3,4,5,6,5,4,3,7])
