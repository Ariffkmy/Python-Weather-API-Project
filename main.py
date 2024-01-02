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

# Check if 'main' key is present in the response
if 'main' in response:
    temp_kelvin = response['main']['temp']
    temp_celcius, temp_fahrenheit = kelvin_to_cel_fah(temp_kelvin)
    feels_like_kelvin = response['main']['feels_like']
    feels_like_celcius, feels_like_fahrenheit = kelvin_to_cel_fah(feels_like_kelvin)
    humidity = response['main']['humidity']
else:
    # Handle the case when 'main' key is not present
    print("Error: 'main' key not found in the response.")
    # You might want to add more error-handling code or exit gracefully here

wind_speed = response.get('wind', {}).get('speed', 'N/A')
description = response['weather'][0]['description'] if 'weather' in response else 'N/A'
sunrise_time = dt.datetime.utcfromtimestamp(response['sys']['sunrise'])+response['timezone'] if 'sys' in response else 'N/A'
sunset_time = dt.datetime.utcfromtimestamp(response['sys']['sunset'])+response['timezone'] if 'sys' in response else 'N/A'

# Now you can use the retrieved values as needed

print(CITY,temp_celcius,temp_fahrenheit,temp_kelvin,humidity,wind_speed,description,sunrise_time,sunset_time)