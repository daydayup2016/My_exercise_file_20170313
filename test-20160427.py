#! user/bin
# _*_ coding:utf-8 _*_
import os
import calendar

file1 = open('testfile.txt','w')
file1.write('hello')
file1.write('My python\n')
file1.close()

os.system(r'type testfile.txt')
os.system(r'color 0a')

os.system(r'pause')
os.system(r'echo xxxxxxxxxxxxxx')
os.system(r'color')  # color why not changed
os.system(r'dir')
os.system(r'echo 123')

# file2 = open('testfile.txt')

# print(file2.read(4))
# print('file content is :\n',file2.read())
# file2.close()
# os.rename('testfile.txt','testfile2.txt')