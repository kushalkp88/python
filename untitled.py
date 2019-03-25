import smtplib
s=smtplib.SMTP('smtp.gmail.com','587')
s.starttls()
sender='kushal.18bcs@gmail.com'
reciver='kushalkp88@gmail.com'
msg="hii"
s.login(sender,'password')
s.sendmail(sender,reciver,m)