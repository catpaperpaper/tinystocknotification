import app_config
import smtplib
from email.mime.text import MIMEText

def email(subj = app_config.EM_SUBJ, msg=app_config.EM_BODY):
    email_user = app_config.EM
    email_password = app_config.EM_KEY
    recipient = app_config.EM_RECP
    subject = subj
    body = msg
    message = MIMEText(body)
    message['From'] = email_user
    message['To'] = recipient
    message['Subject'] = subject
    try:
        server = smtplib.SMTP_SSL(app_config.SMTP, app_config.SMTP_PORT)
        server.ehlo()
        server.login(email_user, email_password)
        server.sendmail(email_user, recipient, message.as_string())
        print("Email sent successfully!")
        server.quit()
    except Exception as e:
        print("Error:", e)

