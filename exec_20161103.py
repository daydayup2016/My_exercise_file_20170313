import time
# sum = 0
# for i in range(1,5):
    # for j in range(1,5):
        # for k in range(1,5):
            # if i != j and i != k and j != k:
                # sum = sum +1
                # print(100*i+10*j+k,'is matchable .')

# print('total number is ',sum)
print('time before:',time.strftime("%Y-%m-%d-%H-%M-%S"))

for k in range(1,10000):
    for n in range(1,10000):
        if k+1000 == n*n :
            for m in range(1,10000):
                if k+168 == m*m:
                    print('======================')
                    print(k,'is matchable...')
                    print('k+1000=',n,'*',n)
                    print('k+168=',m,'*',m)
                    continue
            continue

print('======================') 
print('time after:',time.strftime("%Y-%m-%d-%H-%M-%S"))
print('search done ....')
