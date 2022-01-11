import requests
import datetime as dt
import smtplib
from data import user_name, password
import time


MY_LAT = 49.046378
MY_LONG = 38.233924

EMAIL = user_name
PASSWORD = password


def is_iss_overhead():
    response = requests.get('http://api.open-notify.org/iss-now.json')
    response.raise_for_status()
    data = response.json()
    iss_latitude = float(data['iss_position']['latitude'])
    iss_longitude = float(data['iss_position']['longitude'])
    if MY_LAT-5 <= iss_latitude <= MY_LAT+5 and MY_LONG-5 <= iss_longitude <= MY_LONG+5:
        return True


def is_night():
    parameters = {'lat': MY_LAT, 'lng': MY_LONG, 'formatted': 0}
    response = requests.get('https://api.sunrise-sunset.org/json', params=parameters, )
    response.raise_for_status()
    data = response.json()
    sunrise = int(data['results']['sunrise'].split('T')[1].split(':')[0])
    sunset = int(data['results']['sunset'].split('T')[1].split(':')[0])
    now = dt.datetime.now().hour
    if now >= sunset or now <= sunrise:
        return True


while True:
    time.sleep(60)
    if is_iss_overhead() and is_night():
        with smtplib.SMTP('smtp.gmail.com') as connection:
            connection.starttls()
            connection.login(user=EMAIL, password=EMAIL)
            connection.sendmail(from_addr=EMAIL, to_addrs='mskmee@yahoo.com', msg='hey, look up')