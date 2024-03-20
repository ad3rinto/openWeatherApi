import requests
import os
from dotenv import load_dotenv

load_dotenv()

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
    print(f"It is forecasted to rain at {p["dt_txt"].split()[1]} hrs")
