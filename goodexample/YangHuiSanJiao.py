# /usr/bin env python3
# _*_coding:utf-8 _*_

def triangles():
    L = [1]
    while True:
        yield L
        L.append(0)
        L = [ L[i - 1]+L[i] for i in range(len(L)) ]
        
if __name__ == '__main__':
    a = triangles()
    i = 0
    while i < 15 :
        print(next(a))
        i+=1
    