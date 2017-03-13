#! /usr/bin 
# _*_ coding:gbk _*_

def testlist(val,list1=None):
	if list1 is None:
		list1 = []
	list1.append(val)
	return list1
	
list4=testlist(123)
list2=testlist(123,[])
list3=testlist('a')

print('list4 is :',list4)
print('list2 is :',list2)
print('list3 is :',list3)