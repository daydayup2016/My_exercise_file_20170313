# usr/bin
# _*_ coding:utf-8 _*_

import os
import time

all_file = os.listdir(os.getcwd())
# print(all_file)

def get_result(file1):
    with open(file1,encoding="utf-8") as f:
        file_line = f.readlines().decode()
        print(file_line)
        if "return code:0" in file_line:
            return True
        else:
            return False

def export_to_excel(Name,Result):
    style0 = xlwt.easyxf('font:name Times New Roman,color-index red,bold on',num_format_str='#,##0.00')
    style1 = xlwt.easyxf('font:name Times New Roman,color-index blue,bold on',num_format_str='#,##0.00')
    style2 = xlwt.easyxf('font:name Times New Roman,color-index green,bold on',num_format_str='#,##0.00')
    style3 = xlwt.easyxf(num_format_str='D-MMM-YY')
    
    file = xlwt.Workbook()
    wb = file.add_sheet('result')
    
    wb.write(0,0,ID,style1)
    wb.write(1,0,case_name,style1)
    wb.write(2,0,result,style1)
    wb.write(1,1,Name,Result,style2)
    
    
    
    ws.write(0,0,1234.56,style0)
    ws.write(1,0,datetime.now(),style1)
    ws.write(2,0,1)
    ws.write(2,1,1)
    ws.write(2,2,xlwt.Formula("A3+B3"))
    ws.write(3,2,xlwt.Formula("A3+B3"),style2)
    
# current_path = os.getcwd(),replace('\\','\')
for every_file in all_file:
    if os.path.isdir(every_file):
        log_path = os.path.join(os.getcwd(),every_file)
        for i in os.listdir(log_path):
            if every_file in "".join(i):
                log_file_name = i
                log_file = os.path.join(log_path,log_file_name)
                
                case_name = every_file
                print('before change',log_file)
                print(type(log_file))
                log_file = log_file.replace('\\',"\\\\")
                print('after change ',log_file)
                result = get_result(log_file)
                # result = get_result()
                print (case_name,'-->',result) 
                export_to_excel(case_name,result)
        