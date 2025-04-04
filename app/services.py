from datetime import datetime
from app.weather_api import WeatherClient
from app.repository import save_weather_data
from run_api import read_weather


def fetch_and_save_weather_data(city: str):
    client = WeatherClient()
    data = client.get_weather(city)
    save_weather_data(data)

    data = read_weather()

    for entry in data:
        print(f"📍   City: {entry['city']}")
        print(f"🌡️   Current Temp : {entry['current_temperature']:.2f}°C")
        print(f"🌡️   Max Temp     : {entry['max_temperature']:.2f}°C")
        print(f"🌡️   Min Temp     : {entry['min_temperature']:.2f}°C")

        timestamp = entry['timestamp']
        if isinstance(timestamp, datetime):
            timestamp = timestamp.strftime("%Y-%m-%d %H:%M:%S")
        print(f"🕒   Timestamp     : {timestamp}")
        print("-" * 40)
