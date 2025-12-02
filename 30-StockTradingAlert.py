import requests
from twilio.rest import Client
import os

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
STOCK_API_URL = "https://www.alphavantage.co/query"
STOCK_API_KEY = os.environ.get("STOCK_API_KEY")

NEWS_API_URL = "https://newsapi.org/v2/everything"
NEWS_API_KEY = os.environ.get("NEWS_API_KEY")

stock_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": STOCK_API_KEY
}

news_params = {
    "qInTitle": COMPANY_NAME,
    "apiKey": NEWS_API_KEY
}

response = requests.get(STOCK_API_URL, stock_params)
response.raise_for_status()

daily_data = response.json().get('Time Series (Daily)')

yesterday_date = list(daily_data.keys())[0]
yesterday_close = float(daily_data.get(f"{yesterday_date}")["4. close"])

two_days_ago_date = list(daily_data.keys())[1]
two_days_ago_close = float(daily_data.get(f"{two_days_ago_date}")["4. close"])

diff = (yesterday_close - two_days_ago_close)/two_days_ago_close*100

SEND_MSG = False
if diff >= 5 or diff <= -5:
    news_response = requests.get(NEWS_API_URL, news_params)
    news_response.raise_for_status()
    first_three = [news_response.json()['articles'][n] for n in range(3)]
    print(first_three)
    SEND_MSG = True


if SEND_MSG:
    # The programmer preferred to send it all in one message to reduce white noise
    client = Client(os.environ.get("ACCOUNT_SID"), "auth_token")

    sign = "🔺" if diff > 0 else "🔻"
    message = f"{STOCK}: {sign}{int(abs(diff))}%"
    for news in Example:
        message += f"\nHeadline: {news["title"]}\nBrief: {news["description"]}\n"

    message = client.message.create(body=message, from_="+15017122661", to="+15558675310")

