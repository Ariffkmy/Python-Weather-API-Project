import datetime as dt
import requests

BASE_URL = "http://api.openweathermap.org/data/2.5/weather?"
API_KEY = "1de911562e74d3aaa7ce7a1a5c2c05f8"
CITY = "London"


def kelvin_to_cel_fah(kelvin):
    celcius = kelvin - 273.15
    fahrenheit = celcius * (9/5) + 32
    return celcius, fahrenheit

url = BASE_URL + "appid=" + API_KEY + "&q=" + CITY

response = requests.get(url).json()

temp_kelvin = response['main']['temp']
temp_celcius, temp_fahrenheit = kelvin_to_cel_fah(temp_kelvin)
feels_like_kelvin = response['main']['feels_like']
feels_like_celcius, feels_like_fahrenheit = kelvin_to_cel_fah(feels_like_kelvin)
wind_speed = response['wind']['speed']
humidity = response['main']['humidity']
description = response['weather'][0]['description']
sunrise_time = dt.datetime.utcfromtimestamp(response['sys']['sunrise'])+response['timezone']
sunset_time = dt.datetime.utcfromtimestamp(response['sys']['sunset'])+response['timezone']

print(CITY,temp_celcius,temp_fahrenheit,temp_kelvin,humidity,wind_speed,description,sunrise_time,sunset_time)