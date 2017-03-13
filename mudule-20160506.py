#! user/bin
# _*_ coding:gbk _*_

import os
import calendar
import print20160506
import time


for i in list(range(3,20,2)) :
	print20160506.tuxing_print(i)
	time.sleep(1)
	
time.sleep(3)
print20160506.tuxing_print(5)

# os.system(r'python print-20160506.py 3')
# os.system(r'python print-20160506.py 4')
# os.system(r'python print-20160506.py 5')
# os.system(r'python print-20160506.py 6')