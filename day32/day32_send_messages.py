import datetime as dt
import smtplib
from data import user_name, password
import random


email = user_name
password = password


def send_letter():
    global text
    with smtplib.SMTP('smtp.gmail.com') as connection:
        connection.starttls()
        connection.login(user=email, password=password)
        connection.sendmail(from_addr=email, to_addrs='mskmee@yahoo.com', msg=text)


with open('quotes.txt', 'r', encoding='utf-8') as f:
    data = f.read().split('\n')
letter = random.choice(data)
letter = 'Subject: Motivation\n\n' + letter
text = bytes(letter, 'utf-8')
now = dt.datetime.now()
week_day = now.weekday()
if week_day == 1:
    send_letter()
