import requests
from twilio.rest import Client

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

STOCK_API_KEY = "POKTDMMHQJMPKGR1"
NEWS_API_KEY = "e2fdacb0a1774859bcad88a295bb0e51"
TWILIO_SID = "AC45f7fba29b3105f60c27de87d20e5e60"
TWILIO_AUTH_TOKEN = "2fa735e7d881f2945f27082cf90debff"

stock_params = {
    "function": "TIME_SERIES_DAILY_ADJUSTED",
    "symbol": STOCK_NAME,
    "apikey": STOCK_API_KEY,
}

response = requests.get(STOCK_ENDPOINT, params=stock_params)
data = response.json()["Time Series (Daily)"]
data_list = [value for (key, value) in data.items()]
yesterday_data = data_list[0]
yesterday_closing_price = yesterday_data["4. close"]

day_before_yesterday = data_list[1]
day_before_yesterday_closing_price = day_before_yesterday["4. close"]

difference = float(yesterday_closing_price) - float(day_before_yesterday_closing_price)
up_down = None
if difference > 0:
    up_down = "📈"
else:
    up_down = "📉"

diff_percent = (difference / float(yesterday_closing_price)) * 100

if diff_percent > 3:
    news_params = {
        "apiKey": NEWS_API_KEY,
        "qInTitle": COMPANY_NAME
    }

    news_response = requests.get(NEWS_ENDPOINT, params=news_params)
    articles = news_response.json()["articles"]
    three_articles = articles[:3]

formatted_articles = [f"\n{STOCK_NAME}: {up_down}{round(diff_percent)}%\nHeadline: {article['title']}. \nBrief: {article['description']}" for article in three_articles]

client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)
for article in formatted_articles:
    message = client.messages \
                    .create(
                        body=article,
                        from_='+16184377241',
                        to='+91 9137091261'
                    )

print(message.sid)