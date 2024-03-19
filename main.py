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

is_rain = "rain"

for i in list_of_hourly:
    if i.get(is_rain):
        print(f"E go rain o, for {i["dt_txt"].split()[1]}")
    else:
        print(f"No rain at {i["dt_txt"].split()[1]}")
