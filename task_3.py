import email
import smtplib
import imaplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


class EmailClient:

    GMAIL_SMTP = "smtp.gmail.com"
    GMAIL_IMAP = "imap.gmail.com"

    def __init__(self, login, password) -> None:
        self.login = login
        self.password = password

    #send message
    def send_email(self, recipients, subject, message):
        msg = MIMEMultipart()
        msg['From'] = self.login
        msg['To'] = ', '.join(recipients)
        msg['Subject'] = subject
        msg.attach(MIMEText(message))

        with smtplib.SMTP(self.GMAIL_SMTP, 587) as ms:
            # идентифицировать себя как smtp-клиент gmail
            ms.ehlo()
            # защитите нашу электронную почту с помощью tls-шифрования
            ms.starttls()
            # повторно идентифицировать себя как зашифрованное соединение
            ms.ehlo()

            ms.login(self.login, self.password)

            # Рекомендация: ms.sendmail(self.login, recipients, msg.as_string())
            ms.sendmail(self.login, ms, msg.as_string())

    def receive_email(self, header=None):
        with imaplib.IMAP4_SSL(self.GMAIL_IMAP) as mail:
            mail.login(self.login, self.password)
            mail.list()
            mail.select("inbox")

            criterion = '(HEADER Subject "%s")' % header if header else 'ALL'
            result, data = mail.uid('search', None, criterion)
            assert data[0], 'There are no letters with current header'

            latest_email_uid = data[0].split()[-1]
            result, data = mail.uid('fetch', latest_email_uid, '(RFC822)')
            raw_email = data[0][1]

            # Рекомендации: email_message = email.message_from_bytes(raw_email)
            email_message = email.message_from_string(raw_email)

        return email_message


if __name__ == '__main__':

    login = 'login@gmail.com'
    password = 'qwerty'
    recipients = ['vasya@email.com', 'petya@email.com']
    header = None
    subject = 'Subject'
    message = 'Message'

    user1 = EmailClient(login, password)
    user1.send_email(recipients, subject, message)
    email_message = user1.receive_email(header=header)
    print(email_message)