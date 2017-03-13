

# AuthoredBy 
import re

test_flag = True
while test_flag:
    test_string=input('your input is :')
    if re.match(r'^\d{3}',test_string):
        print('ok')
        test_flag = False
    else:
        print('not match ,please enter again ...')