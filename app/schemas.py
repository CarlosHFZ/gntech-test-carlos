from pydantic import BaseModel
from datetime import datetime


class WeatherDataOut(BaseModel):
    city: str
    current_temperature: float
    max_temperature: float
    min_temperature: float
    timestamp: datetime
