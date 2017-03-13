# _*_ coding:utf-8 _*_

import logging,time
# output to a console
# console = logging.StreamHandler()
# console.setLevel(logging.DEBUG)

# formatter = logging.Formatter('%(asctime)s %(filename)s line:%(lineno)s - %(levelname)s %(message)s')
# console.setFormatter(formatter)
# logging.getLogger('').addHandler(console)

#output to a file
start_time=time.strftime('%Y-%m-%d_%H-%M-%S')
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(filename)s --> line:%(lineno)s - %(levelname)s - %(message)s',
                    # datefmt='%Y-%m-%d %H:%M:%S',
                    filename='test_@_%s.txt' %start_time,
                    filemode='a'
                    )

logging.debug('debug')
logging.info('info')
logging.warning('warning')
logging.error('error')
logging.critical('critical')


logging.info('xxxxxxxxxxxxx')



dic = {1:'debug',2:'info',3:'warning',4:'error',5:'critical'}
listt=['debug','info','warning','error','critical']
a = 0
while a < 30:
    logging.info('================= @ %d ====================' %a)
    print('================= @ %d ====================' %a)
    logging.info('time is :%s,number:%d' %(time.strftime('%Y-%m-%d_%H-%M-%S'),a))
    print('time is :%s,number:%d' %(time.strftime('%Y-%m-%d_%H-%M-%S'),a))
    time.sleep(1)
    for i in listt:
        eval('logging.'+i)('%s' %i)
    a += 1
