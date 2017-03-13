import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header

# third part mail service info 
# mail_host = 'smtp.sina.com'
# mail_user = 'xxxx'
# mail_password = 'xxxxxxxx'

# sender = 'binx.zheng@intel.com'
# receiver = ['963306101@qq.com']

# mail_msg = '''
# <p>python 邮件测试...wowowoowo</p>
# <p><a href='http://www.runoob.com'>这是一个链接</a></p>

# '''

# message = MIMEText(mail_msg,'html','utf-8')
# message['From'] = Header('frommmmmmmm@sina.com','utf-8')
# message['To'] = Header('toooo@sina.com','utf-8')

# subject = 'python send test sub'
# message['Subject'] = Header(subject,'utf-8')


# try:
    # smtpobj = smtplib.SMTP('mail.intel.com')
    # smtpobj.sendmail(sender,receiver,message.as_string())
    # print('send success')
    # smtpobj.quit()
# except :
    # print('error')
    
    
sender = 'binx.zheng@intel.com'
reciever = ['963306101@qq.com']

obj = MIMEMultipart('alternative')
obj['From'] = Header('intel mail')
obj['to'] = Header('myqq')
obj['Subject'] = Header('form intel to my qq')

obj.attach(MIMEText('hello , this is plain','plain','utf-8'))
obj.attach(MIMEText('<html><body><h1>Hello,this is html</h1></body></html>','html','utf-8'))

att1 = MIMEText(open('test.txt','rb').read(),'base64','utf-8')
att1["Content-Type"] = 'application/octet-stream'
att1["Content-Disposition"] = 'attachment; filename="teeeeeeeest.txt"'
obj.attach(att1)

try:
    sendobj = smtplib.SMTP('mail.intel.com')
    sendobj.sendmail(sender,reciever,obj.as_string())
    print('success')
except:
    print('error')
    