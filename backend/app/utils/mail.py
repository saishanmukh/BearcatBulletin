# This program is to send email to the user
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def send_email(to_email, body):
    fromaddr = 'bearcat.bulletin@gmail.com'
    rcpt = [to_email]
    msg = MIMEMultipart()    
    body = f"""<!DOCTYPE html>
    <html>
    <body>
    <p></p>
    <p>Hello,</p>
    <p>
    Please use this code for signing up with bearcat bulletin.
    </p>
    <p>
    Here is your code: {body}
    </p>
    <p>
    Thank you,
    </p>
    <p>
    Bearcat Bulletin Team.
    </p>
    </body>
    </html>"""
    text = MIMEText(body,'html')
    msg['Subject'] = 'Bearcat bulletin account activation'
    msg['To'] = to_email
    msg.attach(text)
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    try:
        nm = "bearcat.bulletin@gmail.com"
        pm = "cgevkvxeaxuzixcp"
        server.login(nm , pm)
    except Exception as e:
        print(e)
    server.sendmail(fromaddr, rcpt, msg.as_string())
    server.quit()

