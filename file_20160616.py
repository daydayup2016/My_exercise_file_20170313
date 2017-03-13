#! usr/bin
# _*_ coding:utf-8 _*_

import time
import re



# 时间字符串格式处理
test_time = time.strftime("%Y#%m#%d#%H#%M#%S", time.localtime())
time_list = re.split("#",test_time)
time_str = time_list[0]+time_list[1]+time_list[2]+'_'+time_list[3]+time_list[4]+time_list[5]

#文件操作
f = open("test_%s.txt" %(time_str),"w+")
print('模式:',f.mode)
print('name:',f.name)

f.write("test time is :\n"+time_str+"\n")

f1=open('test_20160616_155952.txt','r+')
str1=f1.read()
print(str1)



f.close()
f1.close()

# f = open("test_%s%s%s_%s%s%s.txt" %( time_list[0],time_list[1],time_list[2],time_list[3],time_list[4],time_list[5]),"w+")