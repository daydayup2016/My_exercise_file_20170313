# /usr/bin
# _*_ coding:utf-8 _*_


# def foo(s):
    # n=int(s)
    # assert n == 5,'n is 5'
    # return 10/n

# if __name__ == '__main__':
    # foo('50')
    
    
import logging
logging.basicConfig(level=logging.DEBUG,filename='1234.txt',filemode='a')
logger = logging.getLogger()
s='1'
n=int(s)
logging.info('n = %d' % n)
# logging.notset('this is a not set')
logging.debug('this is a debug')
logger.info('this is a info')
logger.warning('this is a warning')
logging.error('this is a error ')
logging.critical('this is a critical')

print(10/n)

