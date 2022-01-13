import requests
import os
import datetime
import smtplib


date_format = '%Y-%m-%d'
yesterday = datetime.datetime.now() - datetime.timedelta(days=1)
b_yesterday = datetime.datetime.now() - datetime.timedelta(days=2)
yesterday = yesterday.strftime(date_format)
b_yesterday = b_yesterday.strftime(date_format)
STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

# STEP 1: Use https://newsapi.org
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
stock_params = {
    'function': 'TIME_SERIES_DAILY',
    'symbol': STOCK,
    'apikey': os.environ.get('ALPHA_VANTAGE_API_KEY'),
}
response = requests.get('https://www.alphavantage.co/query', params=stock_params)
response.raise_for_status()
stock_data = response.json()

yesterday_closed_price = float(stock_data['Time Series (Daily)'][yesterday]['4. close'])
b_yesterday_closed_price = float(stock_data['Time Series (Daily)'][b_yesterday]['4. close'])

percentage = round((yesterday_closed_price - b_yesterday_closed_price) / b_yesterday_closed_price * 100, 2)

# STEP 2: Use https://www.alphavantage.com
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.
news_params = {
    'q': COMPANY_NAME,
    'apiKey': os.environ.get('NEWS_API_KEY')
}
response = requests.get('https://newsapi.org/v2/everything', params=news_params)
response.raise_for_status()
response_news = response.json()
news_slice = response_news['articles'][:3]


def send_email(end_percentage, headline, brief, info):
    with smtplib.SMTP('smtp.gmail.com') as connection:
        connection.starttls()
        connection.login(user=os.environ.get('TEST_GMAIL'), password=os.environ.get('EMAIL_PW'))
        connection.sendmail(from_addr=os.environ.get('TEST_GMAIL'), to_addrs='mskmee2@gmail.com',
                            msg=f'Subject: TSLA: changed {str(end_percentage)}\n\nHeadline: {headline}\nBrief: {brief}'
                                f'\nMore information: {info}'.encode('utf-8'))


news_alert = False
if percentage >= 1 or percentage <= -1:
    news_alert = True

if news_alert:
    if percentage > 0:
        percentage = f'🔺{percentage}'
    else:
        percentage = f'🔻{percentage * -1}'
    for article in news_slice:
        title = article['title']
        url = article['url']
        description = article['description']
        send_email(percentage, title, description, url)
# STEP 3: Use https://www.twilio.com
# Send a separate message with the percentage change and each article's title and description to your phone number.


"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to 
file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of
 the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file
 by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the
  coronavirus market crash.
"""