# user/bin
# _*_ coding:utf-8 _*_

import logging
import sys

logging.basicConfig(level=logging.DEBUG,
					format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
					# datefmt='%a,%d,%b %Y %H:%M:%S',
					datefmt='%Y-%m-%d_%H:%M:%S',
					# filename='my_logging.log',
					# stream='sys.stdout',
					filemode='a')
		
console = logging.StreamHandler()
console.setLevel(logging.INFO)
formatter = logging.Formatter('%(name)-10s:%(levelname)-10s %(message)s')
console.setFormatter(formatter)
logging.getLogger('').addHandler(console)
				
logging.debug('xxxxxxxxxxxxx')
logging.info('yyyyyyyyyyyyyy')
logging.warning('zzzzzzzzzzzzzz')

