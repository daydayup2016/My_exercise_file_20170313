#! usr/bin
# _*_ coding:utf-8 _*_
import os
import sys
# reader = open('scores.txt')
# t = open('scores.txt','r')
# p = t.read().split('\n')
# print(p)
# line = reader.readline() #读取第一行数据
# temp = line.split(' ')[2]
# print('type is :',type(temp))
# print(line)
# print('temp is :',temp)
# os.system('pause')


f = open('scores.txt','r')
line = f.readline()

while len(line) > 0:
	line = line.strip('\n')
	line_str = line.split(' ')
	print(line_str,'lenght is ',len(line_str))
	os.system('pause')
	if 'pass' in line_str:
		temp = line_str.index('pass')
		pass_number = line_str[temp+1]
		fail_number = line_str[temp+3]
		break
		
	line = f.readline()

f.close()
print("pass number is :",pass_number)
print("fail number is :",fail_number)



'''
scores = [] #放分数值的数值
stander = 0 #及格人数
while line != '' and line != None: #循环读取数据行
    tempScore = line.split(' ')[1].replace('\n','') #将姓名和成绩分开，并取分数
    scores.append(tempScore) #将得到的分数添加到数组中
    if float(tempScore) >= 60: #记录大于60分的成绩
        stander += 1
    line = reader.readline()
reader.close()
print(scores)
print(stander)
'''