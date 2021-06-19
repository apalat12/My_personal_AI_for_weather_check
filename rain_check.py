import requests

import os
from twilio.rest import Client

api_key = "e473e1b8f10b4ba7401a8b54e94bcf88"
city = "santa clara"
country = "usa"

MY_LAT = 37.392727185
MY_LONG = -121.9486459

# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid = 'AC22d36274c59681a3d827df9aa5df5cdb'
auth_token = 'a43fc4450854e059ce2653237923cb66'

weather_param = {
    'lat': MY_LAT,
    'lon': MY_LONG,
    'exclude': "hourly,minutely,daily,alerts",
    'appid': api_key
}

ONECALL = 'https://api.openweathermap.org/data/2.5/onecall?'

weather_info = requests.get(url="http://api.openweathermap.org/data/2.5/weather?q={},{}&appid={}"
                            .format(city, country, api_key))
# print(weather_info.json())
# one_call_api = requests.get(url="https://api.openweathermap.org/data/2.5/onecall?lat={}&lon={}&appid={}"
#                             .format(MY_LAT,MY_LONG,api_key))

one_call_api = requests.get(url=ONECALL, params=weather_param)

current_data = one_call_api.json()["current"]
print(current_data)


curr_temp_C = round(current_data['temp']-273.15,2)
curr_feels_C = round(current_data['feels_like']-273.15,2)
print(curr_temp_C,curr_feels_C)

client = Client(account_sid, auth_token)
message = client.messages \
    .create(
    body="Your AIjeet says: Weather is {}\u00b0C feels like {}\u00b0C. Enjoy your run!!🏃‍♀️ ".format(curr_temp_C,curr_feels_C),
    from_='+12158834018',
    to='+14086031986'
)

print(message.status,message.sid)

# per_hour_id = []
# for i in range(0, 12):
#     # print(hourly_data[i]['weather'][0]['id'])
#     per_hour_id.append(hourly_data[i]['weather'][0]['id'])
#
# print(per_hour_id)
# for i in per_hour_id:
#     if i < 800:
#         print("Bring Umbrella")

# client = Client(account_sid, auth_token)
# message = client.messages \
#     .create(
#     body="Hey Sid, I am your AIjeet",
#     from_='+12158834018',
#     to='+14086031986'
# )
#
# print(message.sid)
