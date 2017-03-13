#! user/bin
# _*_ coding:utf-8 _*_

flag = 0
for i in range(1,5):
	for j in range(1,5):
		for k in range(1,5):
			if i != j and j != k and i != k :
				flag = flag + 1
				print(100*i+10*j+k)
				
print('total number is :',flag)
				