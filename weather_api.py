import requests
import os

api_key = os.environ.get('WEATHER_KEY')
print(api_key)
query = {'q': 'minneapolis,mn,us', 'units': 'imperial', 'appid': api_key}
url = 'http://api.openweathermap.org/data/2.5/forecast'

data = requests.get(url, params=query).json()


for item in data['list']:
    print(item['dt_txt'])
    all_temps = item['main']
    print(f'Temperature: {all_temps["temp"]} F')
    print(f'Description: {item["weather"][0]["description"]}')
    print(f'Wind Speed: {item["wind"]["speed"]}')
    print()



