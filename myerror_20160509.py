#! user/bin
# _*_ coding:gbk _*_

class myError(Exception):
	def __init__(self,value):
		self.value=value

try:
	raise myError(100)
except myError as err:
	print('error found\n',err)
	