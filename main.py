from app.weather_api import WeatherClient
import os

api_key = os.getenv("OPENWEATHER_API_KEY")
if not api_key:
    raise ValueError("API_KEY not found in environment variables")

client = WeatherClient(api_key=api_key)
weather = client.get_weather('São Paulo')
print(weather)
