import requests
from pprint import pprint

city = "Bangkok"

url = 'http://api.openweathermap.org/data/2.5/weather?q={}&appid=740b57568fa6e09f23f1da3f0df5aad0&units=metric'.format(city)

res = requests.get(url)

data = res.json()

temp = data['main']['temp']
wind_speed = data['wind']['speed']

latitude = data['coord']['lat']
longitude = data['coord']['lon']

description = data['weather'][0]['description']

print('Temperature: {} degree Celsius'.format(temp))
print('Wind Speed: {} m/s'.format(wind_speed))
print('Latitude: {}'.format(latitude))
print('Longitude: {}'.format(longitude))
print('Description: {}'.format(description))
