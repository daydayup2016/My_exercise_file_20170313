#! user/bin
# _*_ coding: gbk _*_

import os
import time

def except_test():
	for i in list(range(5)):
		
		try:
			if i%3 == 0:
				print(i)
				raise 
		except :
			print('e656565rr')

except_test()