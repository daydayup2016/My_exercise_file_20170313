

# '''
# __Author = binx 
# !/user/bin
# _*_ coding:utf-8 _*_
# '''
import os

# def func(n):
    # if n < 1:
        # print('please enter a int number which larger than 1')
    # if n == 1:
        # return 1
    # else:
        # return n*func(n-1)

        

# if __name__ == '__main__' :
    # print(func(5))
    # print(func(10))
# L=[3*x for x in range(1,20,3) if x%2 == 0]   
# print(L)

# ll = [d for d in os.listdir()]
# print(ll)

g=(x*x for x in range(0,5))
for n in g:
    print(n)