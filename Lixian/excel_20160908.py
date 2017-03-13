# usr/bin 
# _*_ coding:utf-8 _*_

import xlwt
from datetime import datetime

style0 = xlwt.easyxf('font:name Times New Roman,color-index red,bold on',num_format_str='#,##0.00')
style2 = xlwt.easyxf('font:name Times New Roman,color-index blue,bold on',num_format_str='#,##0.00')
style1 = xlwt.easyxf(num_format_str='D-MMM-YY')

wb = xlwt.Workbook()
ws = wb.add_sheet('just_for_test')
ws.write(0,0,1234.56,style0)
ws.write(1,0,datetime.now(),style1)
ws.write(2,0,1)
ws.write(2,1,1)
ws.write(2,2,xlwt.Formula("A3+B3"))
ws.write(3,2,xlwt.Formula("A3+B3"),style2)

wb.save("mytest.xls")


