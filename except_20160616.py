#! usr/bin
# coding=utf-8
# 最全的try-except语句集合
class MyError_Nameerror(Exception):
	'''
	this is an error when you have use a unknown name,such as undefined object.
	'''
	def __init__(self,str='this is an error'):
		self.str = str
	def __str__(self):
		return repr(self.str)
		
class MyError_Nameerror_typeerr(MyError_Nameerror):
	'''
	this is a son class of MyError_Nameerror
	'''
	def __init__(self,info='son class '):
		self.info = info
	def __str__(self):
		return repr(self.info)
		
class MyErr(Exception):
	'''
	This is a error class for test.
	'''
	def __init__(self,info):
		self.info = info
	def __str__(self):
		return repr(self.info)
try :
	# fh = open('test_2010616_165722.txt','r')
	# print(fh.read())
	# raise MyError_Nameerror
	raise MyError_Nameerror_typeerr
except IOError: 
	pass
except IOError as e: 
	pass
except (IOError,ValueError) :
	pass
except (IOError,ValueError) as e :
	pass
except MyError_Nameerror as e:
	print(e)

except MyError_Nameerror_typeerr as e:
	print(e)
except :
	print('error')
else:
	print('open right')
finally :
	pass


class my_class_student_zhong():
	def read(self,topic):
		print("I'm reading %s now " %(topic))

class my_class_student_daxue():
	def write(self,topic):
		print("I'm writing %s now " %(topic))		
		
class my_class_student(my_class_student_zhong,my_class_student_daxue):
	sex = 0
	age = 16
	name = ''
	__weight = 45
	tt = ''
	def __setWeight(self,weight):
		self.__weight = weight
	def __init__(self,sex=0,age=18,name="HuJinTao",weight=46):
		self.sex = sex
		self.age = age
		self.name = name
		self.__weight = weight
	def setName(self,name):
		self.name = name
	def getName(self):
		return self.name
	def study(self):
		print("I'm study now...")
	def show_info(self):
		print(self.sex)
		print(self.age)
		print(self.name)
		
	def getWeight(self):
		print("weight is :",self.__weight)
	def read(self,topic,subject):
		print("I'm reading %s and %s now" %(topic,subject))
	
if __name__ == "__main__" :
	# liming = my_class_student(age=19,name='liming',weight=65)
	# liming.show_info()
	# liming.getWeight()
	# liming.tt = 1234
	# print('liming',liming.tt)
	
	# liming.read('xxx','eee')
	# liming.write('www')
	
	# lintao = my_class_student(age=123)
	# lintao.tt = 2345
	# print(lintao.age)
	# print('liming ',liming.age)
	# print('lintao tt',lintao.tt)
	# print("liming tt",liming.tt)
	pass