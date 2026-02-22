import os 
import requests
import datetime as dt

facebook = os.environ.get("FACEBOOK")
parameters = os.environ.get("PARAM")
parameters = eval(parameters)



url = requests.get("https://api.openweathermap.org/data/2.5/forecast?", params=parameters)
data = url.json()
date = dt.datetime.now()

current_date = (f"{date.day}/{date.month}/{date.year}")
slot = []
will_rain = False
for x in range(4):
    if data["list"][x]["weather"][0]["id"] < 700:
        will_rain = True
        slot.append(1)
    else:
        slot.append(0)

for x in range(4):
    if slot[x] == 1:
        slot[x] = "☔"
    else:
        slot[x] = "☀️"

details = f"\n\n9am:{slot[0]}\n12pm:{slot[1]}\n3pm:{slot[2]}\n6pm:{slot[3]}"

if will_rain:
    requests.post(f"{facebook}️🌡️Weather Forecast️🌡️️️\n{current_date}\n\n☔ It will rain today, you will need an umbrella! ☔{details}")
else:
    requests.post(f"{facebook}🌡️Weather Forecast️🌡️️️\n{current_date}\n\n☀️ It will be a dry day! ☀️{details}")
