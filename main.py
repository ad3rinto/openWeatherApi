import requests
import os

f = open("file.txt", "r")
APPID = f.readline()
f.close()

URL = "https://api.openweathermap.org/data/2.5/weather"
LAT = 53.380149
LON = -2.193189

SITE_PARAMS = {
    "lat": LAT,
    "lon": LON,
    "appid": APPID
}

r = requests.get(URL, params=SITE_PARAMS)
r.status_code
data = r.json()
print(data)
