import time
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

mail_from = ""  # 'from' email address
mail_to   = ""  # 'to'   email address
account_id = "" # your gmail account
account_pw = "" # your gmail password
cycle_time = 5  # minutes to send cycle

msg = MIMEMultipart('alternative')
msg['Subject'] = "Checking Mail!"
msg['From'] = mail_from;
msg['To'] = mail_to;

# Available BOTH(plain, html) code
#text_plain = "Hello, World!\n Bye, World!"
text_html = """\
<html>
    <head></head>
    <body>
        <p>This is automatically sending mail.</p> 
            As a result of this mail, reduce Gmail's external message checking cycle to less than 'your setting' minutes. <br>
            If you set up sending mail every 10 minutes, gmail's mail checking cycle will be at least 10 minutes.
    </body>
</html>"""

#part_plain = MIMEText(text_plain, 'plain')
part_html = MIMEText(text_html, 'html')

#msg.attach(part_plain)
msg.attach(part_html)

while True:
    send = smtplib.SMTP('smtp.gmail.com', 587);
    send.ehlo()
    send.starttls()
    send.login(account_id, account_pw)
    send.sendmail(mail_from, mail_to, msg.as_string())
    send.quit()
    time.sleep(60*cycle_time)