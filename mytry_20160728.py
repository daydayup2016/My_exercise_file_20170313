# user/bin
#! _*_ coding:utf-8 _*_

import logging
import sys
# what I want to input : python xxxxx.py --cycle=100 --executeCmd=reboot --platform=KNL

def Usage():
	print('#########################################################################')
	print('you can execute like this :')
	print('python xxxxx.py --cycle=100 --executeCmd=reboot --platform=KNL')
	print('cycle : this is the cycle number you want to do')
	print('executeCmd : this is the command you want to execute ')
	print('platform : this is the server equipment platform which you want to execute on ')
	print('#########################################################################')
	

logging.error('your input is:{} '.format(sys.argv))
print(sys.argv)

for arg in sys.argv:
	if arg.startswith('--cycle'):
		cycleNumber = arg.split('=')[1].strip()
		print('cycleNumber is :',cycleNumber)
	elif arg.startswith('--executeCmd'):
		executeCmd = arg.split('=')[1].strip()
		print('executeCmd is :',executeCmd)
		

	