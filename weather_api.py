import requests
import os
from datetime import datetime

api_key = os.environ.get('WEATHER_KEY')
query = {'q': 'minneapolis,mn,us', 'units': 'imperial', 'appid': api_key}

url = 'http://api.openweathermap.org/data/2.5/forecast'

data = requests.get(url, params=query).json()

for item in data['list']:
    timestamp = item['dt']
    date = datetime.fromtimestamp(timestamp)
    # Prints the Local Time for temperature
    # Times printed does not start from time where code is being run.  Starts from location of query.
    print(date)         
    all_temps = item['main']
    print(f'Temperature: {all_temps["temp"]} F')
    print(f'Description: {item["weather"][0]["description"]}')
    print(f'Wind Speed: {item["wind"]["speed"]}')
    print()



