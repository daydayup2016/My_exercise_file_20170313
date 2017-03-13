# _*_ coding:utf-8 _*_

from math import sqrt

for i in range(99,80,-5):
    n = sqrt(i)
    if n == int(n):  # used for check whether it is pingfang-number.
        print('find ',i)
        break
    
else:
    print('not find...')