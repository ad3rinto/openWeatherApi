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
    "cnt":4,
    "appid": os.getenv("APPID")
}

r = requests.get(URL, params=SITE_PARAMS)
r.status_code
data = r.json()
list_of_hourly = data["list"]

for p in list_of_hourly:
    if p["weather"][0]["id"] < 700:
        print(f"It is forecasted to rain at {p["dt_txt"].split()[1]} hrs")
    else:
        print(f'It is not forecasted to rain at {p["dt_txt"].split()[1]} hrs')
