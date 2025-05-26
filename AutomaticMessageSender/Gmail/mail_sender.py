import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import datetime
import time
import os
from email.mime.base import MIMEBase
from email import encoders
def sender():
    sender_id=input("Enter your email id:")
    password=input("Enter your App password:")
    print("Enter the mail ids of the recipients separated by commas:")
    receivers_id=input().split(",")
    print("Enter the subject of the mail:")
    subject=input()
    print("Enter the text of the mail:")
    text=input()
    attachment_=input("Enter the path of the attachment (or leave blank if no attachment):")
    html=f"""\
    <html>
        <body style="font-family: Arial, sans-serif;
                    background-color:#CEE9F9FF;
                    padding: 20px;"> 
            <div style="background-color:##90EE90;">
            <h1>Exciting to Share this mail.</h1> 
            <hr style="border: 1px solid #2171EAFF;">
            </div>
            <p><b>Hello</b></p>
            <p>This the mail that I have designed using html code.<br>
            <b>It is a simple mail sender program.</b><br>
            </p>
            <p><b>Hope you like it.</b></p>
            <div style= " text-align:center;">
            <img src="https://www.menosfios.com/wp-content/uploads/2015/11/code-logo.png" 
                 alt="Image" style="width:100%; max-width:200px;">
            </div>
            <p style="text-align:center;font-size:24px; " >Thank you!</p>
            <hr style="border: 1px solid #0CA9E7FF;">
            <div style="text-align:right;">
            <p>Best regards,<br>
            <b>Mail Sender Program</b></p>
            
            <p style="background-color:#5BDA56FF;text-align:center;font-size:24px;"><b>Have a great day!</b></p>
            </div>
        </body>                     
    </html>
    """
     
    print("Enter the date and time to send the mail in DD/MM/YYYY HH:MM format:")
    Date_time_=input()
    print(f"Waiting for the time to send the mail...at {Date_time_}")
    while True:
        current_time=datetime.now().strftime("%H:%M")
        if current_time>=Date_time_:
            send_mail(receivers_id,sender_id,Date_time_,subject,text,html,password,attachment_)
            break
def send_mail(receivers_,sender_,time_,subject,text,html,password,attachment_path=None):
    for receiver in receivers_:
        msg= MIMEMultipart("alternative")
        msg['From'] = sender_
        msg['To'] = receiver
        msg['Subject'] = subject
        msg['Date'] = time.strftime("%d/%m/%Y %H:%M:%S")
        msg.attach(MIMEText(text, 'plain'))

        msg.attach(MIMEText(html, 'html'))
        # Check if the attachment path is provided and is a file
        if attachment_path and os.path.isfile(attachment_path):
            with open(attachment_path, "rb") as file:
                part = MIMEBase("application", "octet-stream")
                part.set_payload(file.read())
                encoders.encode_base64(part)
                part.add_header("Content-Disposition", f"attachment; filename={os.path.basename(attachment_path)}")
                msg.attach(part)
        try:
            with smtplib.SMTP('smtp.gmail.com', 587) as server:
                server.starttls()
                server.login(sender_, password)
                server.sendmail(sender_, receiver, msg.as_string())
                print(f"Mail sent to {receiver} at {time_}")
        except Exception as e:
            print(f"Failed to send mail to {receiver}: {e}")
if __name__=="__main__":
    print("Welcome to the mail sender program!")
    print("The password should be an App password generated from your email account.")
    print("Please Enter the details carefully.")
    sender()