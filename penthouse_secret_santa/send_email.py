
import smtplib
from email.message import EmailMessage


class Mailer:
    def __init__(self):
        with open('credentials', 'r') as f:
            self.__EMAIL_ADDRESS = f.readline().strip()
            self.__EMAIL_PASSWORD = f.readline().strip()

    def send_email(self, email, subject, message):
        msg = EmailMessage()
        msg['Subject'] = subject
        msg['From'] = self.__EMAIL_ADDRESS
        msg['To'] = email

        msg.set_content(message)

        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(self.__EMAIL_ADDRESS, self.__EMAIL_PASSWORD)
            smtp.send_message(msg)
