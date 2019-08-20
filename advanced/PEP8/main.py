import email
import smtplib
import imaplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


class Mail:
    def __init__(self, login, password, smtp='smtp.gmail.com', imap='imap.gmail.com'):
        self.login = login
        self.password = password
        self.smtp = smtp
        self.imap = imap

    def send_message(self, message_text, subject, recipients):
        message = MIMEMultipart()
        message['From'] = self.login
        message['To'] = ', '.join(recipients)
        message['Subject'] = subject
        message.attach(MIMEText(message_text))

        mail_sender = smtplib.SMTP(self.smtp, 587)
        mail_sender.ehlo()
        mail_sender.starttls()
        mail_sender.ehlo()
        mail_sender.login(self.login, self.password)
        mail_sender.sendmail(self.login, mail_sender, message.as_string())
        mail_sender.quit()

    def receive_message(self, header=None):
        mail_getter = imaplib.IMAP4_SSL(self.smtp)
        mail_getter.login(self.login, self.password)
        mail_getter.list()
        mail_getter.select("inbox")

        criterion = f'(HEADER Subject {header if header else "ALL"})'
        result, data = mail_getter.uid('search', None, criterion)
        assert data[0], 'There are no letters with current header'
        latest_email_uid = data[0].split()[-1]
        result, data = mail_getter.uid('fetch', latest_email_uid, '(RFC822)')
        raw_email = data[0][1]
        email_message = email.message_from_string(raw_email)
        mail_getter.logout()

        return email_message


if __name__ == '__main__':
    mailbox = Mail('login@gmail.com', 'qwerty')
    mailbox.send_message('Message', 'Subject', ['vasya@email.com', 'petya@email.com'])
    mailbox.receive_message()
