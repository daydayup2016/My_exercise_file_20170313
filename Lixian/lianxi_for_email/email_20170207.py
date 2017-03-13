import smtplib
from email.mime.text import MIMEText
from email.header import Header

# third part mail service info 
mail_host = 'smtp.126.com'
mail_user = 'xxxx'
mail_password = 'xxxxxxxx'

sender = 'zhengbin2006@126.com'
receiver = ['963306101@qq.com']

message = MIMEText('python send test','plain','utf-8')
message['From'] = Header('frommmmmmmm@sina.com','utf-8')
message['To'] = Header('toooo@sina.com','utf-8')

subject = 'python send test sub'
message['Subject'] = Header(subject,'utf-8')


try:
    smtpobj = smtplib.SMTP()
    smtpobj.connect(mail_host,25)
    smtpobj.login(mail_user,mail_password)
    smtpobj.sendmail(sender,receiver,message.as_string())
    print('send success')
except :
    print('error')