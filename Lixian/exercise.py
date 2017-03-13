
def fact(n=1):
    if n < 1:
        print('wrong number')
    else:
        if n==1:
            return 1
        else:
            return n*fact(n-1)


if __name__ == '__main__':
    n = int(input('please input a int number...'))
    print(fact(5))
    print(fact(10))
