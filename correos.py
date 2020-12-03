#!/usr/bin/env python3
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
import json
import sys

#sending multiple emails
m=[]
data={}
with open('data.json') as f:
        data = json.load(f)

#create message object instance
#setup the parameters of the message
msg=MIMEMultipart()
msg['From']=data['user']
msg['Subject']=str(sys.argv[1])
message=str(sys.argv[2])

# add in the message body
msg.attach(MIMEText(message, 'plain'))
 
#create server
server=smtplib.SMTP('smtp.office365.com:587')
server.starttls()
 
# Login Credentials for sending the mail
server.login(data['user'], data['pass'])
 
#Open mails
g=open('Mails.txt','r')
for line in g:
    to=line
    m.append(to)
g.close

#send the message via the server
for element in m:
    print(element)
    msg['To']=element
    server.sendmail(msg['From'], msg['To'], msg.as_string())
    print("successfully sent email to %s:" % (msg['To']))
server.quit()
