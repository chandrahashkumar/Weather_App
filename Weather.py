#authored by: Chandrahash Kumar
import os
import requests
from dotenv import load_dotenv

load_dotenv('.env', override=True)
api_key = os.getenv('WEATHER_API_KEY')

location_input = input("Enter your city name or pin code: ").strip()

location_url = f"http://api.openweathermap.org/data/2.5/weather?q={location_input}&appid={api_key}"
response = requests.get(location_url)
data = response.json()

if response.status_code == 200 and data.get('cod') == 200:
    lat = data['coord']['lat']
    lon = data['coord']['lon']

    weather_url = f"https://api.openweathermap.org/data/2.5/forecast?units=metric&cnt=1&lat={lat}&lon={lon}&appid={api_key}"
    weather_response = requests.get(weather_url)
    weather_data = weather_response.json()

    temp = weather_data['list'][0]['main']['temp']
    description = weather_data['list'][0]['weather'][0]['description']
    humidity = weather_data['list'][0]['main']['humidity']
    feels_like = weather_data['list'][0]['main']['feels_like']
    pressure = weather_data['list'][0]['main']['pressure']
    wind_speed = weather_data['list'][0]['wind']['speed']

    print(f'''Weather details for {location_input.capitalize()}:
    Temperature: {temp}°C
    Description: {description}
    Feels Like: {feels_like}°C
    Wind Speed: {wind_speed} m/s
    Humidity: {humidity}%
    Pressure: {pressure} hPa
    ''')
   
else:
    print("City or pin code not found. Please check the details and try again.")
