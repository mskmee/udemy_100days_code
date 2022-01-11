import random
from data import user_name, password
import smtplib
import datetime as dt
import pandas


EMAIL = user_name
PASSWORD = password

data = pandas.read_csv('birthdays.csv')
data_birthday = data.to_dict(orient='records')
now = dt.datetime.now()
month = now.month
day = now.day


def choose_letter(name):
    with open(f'letter_templates/letter_{random.randint(1, 3)}.txt', 'r') as f:
        text = f.read()
        text = text.replace('[NAME]', name)
        text = text.replace('Angela', "Maksim")
        text = 'Subject: Happy Birthday\n\n' + text
        text = bytes(text, 'utf-8')
        return text


def send_message(text, email):
    with smtplib.SMTP('smtp.gmail.com') as connection:
        connection.starttls()
        connection.login(user=EMAIL, password=PASSWORD)
        connection.sendmail(from_addr=EMAIL, to_addrs=email, msg=text)


for el in data_birthday:
    if el['month'] == month:
        if el['day'] == day:
            birthday_name = el['name']
            letter = choose_letter(birthday_name)
            send_message(text=letter, email=el['email'])
