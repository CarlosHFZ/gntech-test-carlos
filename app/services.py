from datetime import datetime
from app.weather_api import WeatherClient
from app.repository import save_weather_data
from run_api import read_weather
from requests.exceptions import HTTPError, RequestException


def fetch_and_save_weather_data(city: str):
    client = WeatherClient()

    try:
        data = client.get_weather(city)
        save_weather_data(data)
        print(f"✅ Weather data for '{city}' fetched and saved successfully!")

    except HTTPError as http_err:
        print(f"❌ HTTP error occurred while fetching data for '{city}': {http_err}")
        return
    except RequestException as req_err:
        print(f"❌ Request error occurred for '{city}': {req_err}")
        return
    except Exception as e:
        print(f"❌ An unexpected error occurred: {e}")
        return

    try:
        data = read_weather()
    except Exception as e:
        print(f"❌ Failed to read data from the database: {e}")
        return

    for entry in data:
        try:
            print(f"📍   City: {entry['city']}")
            print(f"🌡️   Current Temp : {entry['current_temperature']:.2f}°C")
            print(f"🌡️   Min Temp     : {entry['min_temperature']:.2f}°C")
            print(f"🌡️   Max Temp     : {entry['max_temperature']:.2f}°C")

            timestamp = entry['timestamp']
            if isinstance(timestamp, datetime):
                timestamp = timestamp.strftime("%Y-%m-%d %H:%M:%S")
            print(f"🕒   Timestamp     : {timestamp}")
            print("-" * 40)
        except Exception as e:
            print(f"⚠️  Error displaying data entry: {e}")