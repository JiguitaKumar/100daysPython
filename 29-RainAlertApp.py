import requests
from twilio.rest import Client
import os

#export OMW_API_KEY=[value]
api_key = os.environ.get("OMW_API_KEY")
my_lat = 41.150150
my_lon = -8.610320
api_url = "https://api.openweathermap.org/data/2.5/forecast"

params = {
    "lat": my_lat,
    "lon": my_lon,
    "cnt": 4,
    "appid": api_key
}

response = requests.get(api_url, params)
response.raise_for_status()
response_json = response.json()


#export ACCOUNT_SID=[value]
account_sid = os.environ.get("ACCOUNT_SID")
auth_token = "your_auth_token"


will_rain = False
for item in response_json["list"]:
    if int(item["weather"][0]["id"]) < 700:
        will_rain = True
if will_rain:
    client = Client(account_sid, auth_token)
    message = client.message.create(body="Bring an umbrella.", from_="+15017122661", to="+15558675310")
    print(message.status)


