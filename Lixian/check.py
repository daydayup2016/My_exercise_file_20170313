

'''
for check whether a number is a square number ...

'''
from math import sqrt
import time
import os
while 1:
    a = input('please enter a number ...')
    if a == "":
        print('no data')
        continue
    else:
         print(a)
         a = float(a)
    b = sqrt(a)
    if b == int(b):
        print('occur...')
        os.system('color 2f')
        time.sleep(4)
        os.system('color ')
        break

else:
    print('no')