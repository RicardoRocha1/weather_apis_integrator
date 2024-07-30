import requests
import os
from dotenv import load_dotenv
from datetime import date

def fetch_open_weather_data(location):
    load_dotenv()
    open_weather_api_key = os.getenv("OPENWEATHER_API_KEY")
    url = f"http://api.openweathermap.org/data/2.5/weather?q={location}&appid={open_weather_api_key}"
    response = requests.get(url)
    open_weather_data = response.json()
    return open_weather_data

def fetch_weatherapi_data(location):
    load_dotenv()
    weatherapi_api_key = os.getenv('WEATHERAPI_API_KEY')
    url = f"http://api.weatherapi.com/v1/current.json?key={weatherapi_api_key}&q={location}"
    response = requests.get(url)
    data = response.json()
    if response.status_code == 200:
        return {
            "location": data["location"]["name"],
            "region": data["location"]["region"],
            "country": data["location"]["country"],
            "latitude": data["location"]["lat"],
            "longitude": data["location"]["lon"],
            "temperature_c": data["current"]["temp_c"],
            "temperature_f": data["current"]["temp_f"],
            "condition": data["current"]["condition"]["text"],
            "humidity": data["current"]["humidity"],
            "wind_kph": data["current"]["wind_kph"],
            "wind_mph": data["current"]["wind_mph"],
            "precip_mm": data["current"]["precip_mm"],
            "precip_in": data["current"]["precip_in"],
            "last_updated": data["current"]["last_updated"]
        }
    else:
        return {"error": response.json()}