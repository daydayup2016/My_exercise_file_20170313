#! user/bin
# _*_ coding:gbk _*_

import time
import calendar
import os
import _thread
import _dummy_thread

def echo_time_now(ThreadName):
	for i in range(5):
		print(ThreadName,':',time.strftime("%Y-%m-%d %H:%M:%S",time.localtime()))
		time.sleep(1.5)
	
_thread.start_new_thread(echo_time_now,('thread-1',))

# _thread.start_new_thread(echo_time_now,('thread-2',))

