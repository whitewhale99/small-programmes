''' You work at a company that sends daily reports to clients via email. The goal of this project is to automate the process of sending these reports via email.

Here are the steps you can take to automate this process:

    Use the smtplib library to connect to the email server and send the emails.

    Use the email library to compose the email, including the recipient's email address, the subject, and the body of the email.

    Use the os library to access the report files that need to be sent.

    Use a for loop to iterate through the list of recipients and send the email and attachment.

    Use the schedule library to schedule the script to run daily at a specific time.

    You can also set up a log file to keep track of the emails that have been sent and any errors that may have occurred during the email sending process. '''
    
    
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.application import MIMEApplication
from email import encoders
from os.path import basename
import schedule
import time




# define general  autoemail function

def autoemail_daily(recipient, message, att_path):
    
    msg=MIMEMultipart()
    msg['sender']='silviafrostin@gmail.com'
    msg['recipient']='frostinzhang@gmail.com'
    msg['subject']='Brainnest test email'
    msg.attach(MIMEText(message, 'plain'))


    # email attachment from local library
    with open(att_path,'rb') as f:
        attachment=MIMEBase('application', 'octet-stream')
        attachment.set_payload((f).read())
        encoders.encode_base64(attachment)
        attachment.add_header('Content-Disposition', 'attachemnt; filename="{}"'.format(basename(att_path)))
    msg.attach(attachment)


    server='smtp.gmail.com'
    sender_email='silviafrostin@gmail.com'
    password='qjslrzrnyiqpqrpn'
    reciever_email=[recipient]
    port=587

    #check the error
    try:
        # daily email sending automatic 
        server_SMTP=smtplib.SMTP(server, port)
        server_SMTP.connect(server, port)
        server_SMTP.starttls()
        server_SMTP.login(sender_email,password)
        server_SMTP.sendmail(sender_email,reciever_email,msg.as_string()) 
        server_SMTP.quit()
    except ConnectionRefusedError:
        print("there is an connection error in sender's email.")
    except smtplib.SMTPAuthenticationError:
        print("there is an authentication error in smtp server.")
    except:
        print("there is an error occurred")
    # email arriving check




# test function by specficic list of recipients
recipients=['silviafrostin@gmail.com','frostinzhang@gmail.com','yuxinzhang1015@outlook.com']
att_path='/Users/mwhitewhale/Downloads/fi.pdf'
message='this is an brainnest test email'


# define job
def job():
    for recipient in recipients:
        autoemail_daily(recipient,message,att_path)

# cancle the job at certain time
def cancel_job():
    return schedule.CancelJob   

# schedule to start the job
schedule.every().day.at('09:00').until('2023-02-04').do(job)



