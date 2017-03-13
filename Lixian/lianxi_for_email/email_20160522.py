#! usr/bin 

import smtplib,os
from email.mime.text import MIMEText
mailto_list = ['963306101@qq.com']
mail_host = "smtp.126.com"
mail_user = "zhengbin2006"
mail_pass = "zhengbin080921"
mail_postfix = "126.com"
def send_mail(to_list,sub,content):
	me = mail_user+"@"+mail_postfix
	msg = MIMEText(content,_subtype='plain')
	msg['Subject'] = sub
	msg['From'] = me
	msg['To'] = ";".join(to_list)
	try:
		server = smtplib.SMTP()
		server.connect(mail_host)
		server.login(mail_user,mail_pass)
		server.sendmail(me,to_list,msg.as_string())
		server.close()
		return True
	except Exception as e:
		print(e)
		return False
for i in range(5):
	if send_mail(mailto_list,'hello','haha!'):
		print("done!")
	else:
		print('failed!')