import os
import io
import smtplib
#from string import Template
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

#read mail body file
def read_template(filename):
template_file_content = open(filename, "r").read()
return template_file_content

#assigning env_variables from job 
SENDER_ADDR = os.environ['SENDER_ADDRESS']
RECEIVER = os.environ['RECEIVER_ADDRESS']
SMTP_ADDR = os.environ['SMTP_SERVER']

def main():
message = read_template('output.html')
# set up the SMTP server
s = smtplib.SMTP(SMTP_ADDR)
s.set_debuglevel(1)
s.ehlo()
# create a message
msg = MIMEMultipart() 
# setup the parameters of the message
msg['From']=SENDER_ADDR
msg['To']=RECEIVER
msg['Subject']="[SPARTA] Navigation releasecandidate build"
# add in the message body
msg.attach(MIMEText(message, 'html'))
# send the message via the server set up earlier.
s.send_message(msg)
del msg
s.quit()

if __name__ == '__main__':
main()
