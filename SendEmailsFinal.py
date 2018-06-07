# -*- coding: cp1252 -*-
import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
from time import sleep
import csv
import random

with open('csvfilepath.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        first_name = str(row['First Name'].strip())
        toaddr = str(row['Email Address'].strip())
        job_title = str(row['Job title'])
        #company = str(row['Company'])
        fromaddr = "ADD_YOUR_EMAIL"
        
        msg = MIMEMultipart()
        msg.add_header('reply-to', 'ADD_YOUR_EMAIL')
        msg['From'] = fromaddr
        msg['To'] = toaddr
        msg['Subject'] = "ADD_YOUR_SUBJECT"
        body = """
<html>
<head></head>
<body>
<p>Hey,<br><br>

THIS TEXT SHOULD BE REPLACED WITH SOMETHING MEANINGFUL

Sincerly,<br>

</p>
</body>
</html>""" % (toaddr)
        try:
            msg.attach(MIMEText(body, 'html'))
         
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()
            server.login(fromaddr, "YOUR_PASSWORD")
            text = msg.as_string()
            server.sendmail(fromaddr, toaddr, text)
            server.quit()
        

            print "Email succesfully sent to: %s" % toaddr
            sleep(random.randrange(20,35))

        except:
            print "Email FAILED to %s" % toaddr
            pass

