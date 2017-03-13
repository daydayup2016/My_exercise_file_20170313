#! user/bin
# _*_ coding:gbk _*_

class myclass_stu:
	Guo = 'CHINA'

	def __init__(self,name='null',age=18):
		self.name = name
		self.age = age
	def study(index='python'):
		print("I'm study :",index,)

lily = myclass_stu()
print(lily.Guo,lily.name,lily.age)
lintao = myclass_stu(name='lintao',age=22)
print(lintao.Guo,lintao.name,lintao.age)

class myexcept(Exception):
	