#! user/bin
# import os
# import calendar
# import time
# os.system(r'color 0a')
# print(calendar.month(2016,4),'\n',calendar.month(2016,5))
# os.system(r'pause')
# os.system(r"color")
# print(time.time())
# print(time.asctime())
# print(time.localtime())
# print(time.strftime("%Y-%m-%d %H:%M:%S %Z",time.localtime()))


def getSum (*partuple1):
	'''
		this is a function to get the sum for numbers you have input.
	'''
	print('your input is :\n',partuple1)
	sum=0
	for i in partuple1:
		sum=sum+i
	return (sum)
# print(getSum(3,4,5,6))
# print(getSum(11,22,33,44,55,66))

# money=200
# def addmoney():
	# global money
	# money=money+50
	
# print(money)
# addmoney()
# print(money)














