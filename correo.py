#!/usr/bin/env python3
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
import sys
import json

data={}
with open('data.json') as f:
        data=json.load(f)

# create message object instance
msg=MIMEMultipart()

# setup the parameters of the message
msg['From']=data['user']
msg['To']=str(sys.argv[1])
msg['Subject']=str(sys.argv[2])
message=str(sys.argv[3])

# add in the message body
msg.attach(MIMEText(message, 'plain'))

#create server
server=smtplib.SMTP('smtp.office365.com:587')
server.starttls()

# Login Credentials for sending the mail
server.login(data['user'], data['pass'])

# send the message via the server.
server.sendmail(msg['From'], msg['To'], msg.as_string())
server.quit()
print("successfully sent email to %s:" % (msg['To']))
