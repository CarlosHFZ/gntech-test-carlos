import requests
from datetime import datetime
from app.settings import OPENWEATHER_API_KEY


class WeatherClient:
    def __init__(self) -> None:
        self.api_key = OPENWEATHER_API_KEY
        self.base_url = "https://api.openweathermap.org/data/2.5/weather"

    def get_weather(self, city: str) -> dict:
        params = {
            "q": city,
            "appid": self.api_key,
            "units": "metric",
            "lang": "pt_br"
        }

        response = requests.get(self.base_url, params=params)

        try:
            response.raise_for_status()  # Raises HTTPError if status != 200
        except requests.exceptions.HTTPError as e:
            print(f"HTTPError: {e.response.status_code} - {e.response.text}")
            raise

        data = response.json()
        return self._parse_weather_data(data)

    def _parse_weather_data(self, data: dict) -> dict:
        timestamp = data.get("dt")
        if timestamp is None:
            raise ValueError("Missing timestamp in API response")
        dt = datetime.fromtimestamp(int(timestamp))
        return {
            "city": data.get("name"),
            "current_temperature": data["main"].get("temp"),
            "max_temperature": data['main'].get('temp_max'),
            "min_temperature": data['main'].get('temp_min'),
            "timestamp": dt
        }
