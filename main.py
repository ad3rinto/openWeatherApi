import requests
import os
from dotenv import load_dotenv
from twilio.rest import Client

load_dotenv()
account_sid = os.getenv("ACC_SID")
auth_token = os.getenv("AUTH_TOKEN")

URL = "https://api.openweathermap.org/data/2.5/forecast"
LAT = 53.380149
LON = -2.193189

SITE_PARAMS = {
    "lat": LAT,
    "lon": LON,
    "cnt": 4,
    "appid": os.getenv("APPID")
}

r = requests.get(URL, params=SITE_PARAMS)
r.status_code
data = r.json()
list_of_hourly = data["list"]
will_rain = False

for p in list_of_hourly:
    if int(p["weather"][0]["id"]) < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
            body="You need an umbrella as it is going to rain sometime within the next 12 hours ☔️",
            from_='+447488879613',
            to='+447746302442'
        )
    print(message.sid)
