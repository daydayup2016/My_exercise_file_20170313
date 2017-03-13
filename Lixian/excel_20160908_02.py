# usr/bin
# _*_ coding:utf-8 _*_

import os
import time

all_file = os.listdir()
# print(all_file)

def get_result(file):
    with open(file) as f:
        if "return code:0" in f.readlines():
            # result = PASS 
            return PASS
        else:
            # result = FALSE
            return FALSE
            


# current_path = os.getcwd(),replace('\\','\')
for everyone in all_file:
    if os.path.isdir(everyone):
        log_path = os.path.join(os.getcwd(),everyone)
        for i in os.listdir(log_path):
            if everyone in "".join(i):
                log_file_name = i
                log_file = os.path.join(log_path,log_file_name)
                #解析log
                case_name = everyone
                result = get_result(log_file)
                print(case_name,result)
