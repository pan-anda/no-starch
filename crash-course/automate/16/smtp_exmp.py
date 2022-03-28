import smtplib

smtpObj = smtplib.SMTP('smtp.163.com', 25)
print(smtpObj.ehlo())    #问候服务器(返回250表成功)
print(smtpObj.starttls())   #建立加密连接（220表成功）
sl = smtpObj.login('panpanda5759@163.com', 'KZKSZZUVKIGFTRKY')
print(sl)    #235表成功

ss = smtpObj.sendmail('panpanda5759@163.com', 'mengsi403@sina.com', 'Subject: So long.\nDear one, so long and thank you. Sincerely Bob')
print(ss)    #返回空字典：发送成功
print(smtpObj.quit())   #断开服务器











