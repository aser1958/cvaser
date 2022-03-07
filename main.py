
from twilio.rest import Client
import os
import smtplib
import requests

import json

my_email = os.environ.get("my_email")  # "aser58@gmail.com"
password = os.environ.get("password")  # "iai68177"

api_key = "bf56730b1bb5b0c07483d175b7c9b3a5"

excluded = ["current", "minutely", "daily", "alerts"]

param = {"lat": 31.903410, "lon": 34.806831, "appid": api_key, "units": "metric",
         "exclude": "current,minutely,daily"}

# "exclude":"current,minutely,daily"

response = requests.get(url="https://api.openweathermap.org/data/2.5/onecall",
                        params=param, verify=True)
# response.raise_for_status()
data = response.text

dat_dict = json.loads(data)


data_hourly = dat_dict["hourly"][10]["weather"]

# aaa=[bb for bb in dat_dict["hourly"]]

aaa = [bb["weather"][0]["id"] for bb in dat_dict["hourly"]]

rain_list = {i: aaa[i] for i in range(len(aaa))}

is_rain = False

for hour in rain_list:
    # print(f"{hour} {rain_list[hour]}")
    if int(rain_list[hour]) < 700:
        is_rain = True
        break


print(is_rain)

# if is_rain:
#     my_email =  "aser58@gmail.com" # os.environ.get("my_email")  #
#     password =  "iai68177" # os.environ.get("password")  #

#     with smtplib.SMTP("smtp.gmail.com") as connection:
#         connection.starttls()
#         connection.login(user=my_email, password=password)
#         connection.sendmail(from_addr=my_email, to_addrs="aser58@yahoo.com",
#                             msg=f"Subject:Happy Birth Day\n\nIts is raining\nTAKE UMNRELA !!!")

from dotenv import load_dotenv

load_dotenv()

# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure

account_sid = os.environ.get("account_sid")
auth_token = os.environ.get("auth_token")

client = Client(account_sid, auth_token)

message = client.messages \
                .create(
                    body="Find your Account SID and Auth Token at twilio.com/console",
                    from_='+19107273066',
                    to='+9720523579146'
                )

print(message.sid)


# data_string="".join(data_hourly)
# print(type(data_hourly))
# print(rain_list)

# json_string = json.dumps(data)
# print(json_string)

# with open('json_data.json', 'w') as outfile:
#     outfile.write(json_string)

# with open("weather.txt", mode="w") as file:
#     file.write(data)
# #

# print(data)
