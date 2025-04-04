from dotenv import load_dotenv
from app.weather_api import WeatherClient
from app.database import init_db
from app.repository import save_weather_data
import os

load_dotenv()

init_db()

api_key = os.getenv("OPENWEATHER_API_KEY")

if not api_key:
    raise ValueError("API_KEY not found in environment variables")

client = WeatherClient(api_key=api_key)

city = 'Santa Catarina'
data = client.get_weather(city)
print(data)
save_weather_data(data)
