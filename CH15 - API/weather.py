
#---------------CHAPTER 15 - APIS---------------------------------------------

#--------------TASK 2+3 WEATHER APP-------------------------------------------

import requests

endpoint = "http://api.openweathermap.org/data/2.5/weather"
# endpoitn tells us where to get the data

payload = {"q":"Sydney, Australia", "units":"metric", "appid":"cf5fe6a2856ae3a9791c2f641bd84a26"}
#payload what data to obtain, we want to know about london.

response = requests.get(endpoint, params = payload)

data = response.json()

print("this is what data looks like  \n")
print(data['main'])
print(response.url)
print(response.status_code)
print(response.headers["content-type"])
print(response.text)

temperature = data['main']['temp']
name = data["name"]
weather = data["weather"][0]["main"]
print(u"It's {}C in {}, and the sky is {}".format(temperature, name, weather))



