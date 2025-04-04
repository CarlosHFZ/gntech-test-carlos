import requests
from datetime import datetime


class WeatherClient:
    def __init__(self, api_key: str) -> None:
        self.api_key = api_key
        self.base_url = "https://api.openweathermap.org/data/2.5/weather"

    def get_weather(self, city: str) -> dict:

        params = {
            "q": city,
            "appid": self.api_key,
            "units": "metric",
            "lang": "pt_br"
        }

        # Tradiotional way
        # url = (
        #    f"https://api.openweathermap.org/data/2.5/weather"
        #    f"?q={city}&appid={self.api_key}&units=metric&lang=pt_br"
        # )

        response = requests.get(self.base_url, params=params)

        if response.status_code == 200:

            data = response.json()
            return self._parse_weather_data(data)
        else:
            raise Exception(
                f"Request failed: {response.status_code}\n"
                "Reason: {response.text}"
            )

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
