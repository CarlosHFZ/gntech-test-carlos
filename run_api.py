from fastapi import FastAPI, HTTPException, Query
import requests
from app.database import init_db, SessionLocal
from app.repository import save_weather_data
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy import text
from app.schemas import WeatherDataOut
from app.weather_api import WeatherClient


app = FastAPI()

init_db()

# Habilitar CORS (Cross-Origin Resource Sharing)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def root():
    return {"message": "Hello, World!"}


@app.get("/weather", response_model=list[WeatherDataOut])
def read_weather():
    db = SessionLocal()
    try:
        result = db.execute(text("SELECT * FROM weather_data"))
        rows = result.fetchall()
        weather_data = [{
            "city": row[1],
            "current_temperature": row[2],
            "max_temperature": row[3],
            "min_temperature": row[4],
            "timestamp": row[5]
        } for row in rows]
        return weather_data
    except Exception as e:
        print(f"Error: {e}")
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        db.close()


@app.post("/weather")
def save_weather(city: str = Query(..., min_length=2, description="Name of the city to fetch weather data for")):
    client = WeatherClient()
    try:
        weather_data = client.get_weather(city)
        save_weather_data(weather_data)
        return {"message": f"Weather data for '{city}' saved successfully!"}
    except requests.exceptions.HTTPError as http_err:
        if http_err.response.status_code == 404:
            raise HTTPException(
                status_code=404, detail=f"City '{city}' not found.")
        raise HTTPException(status_code=http_err.response.status_code,
                            detail="Failed to access the weather API.")
    except Exception as e:
        raise HTTPException(
            status_code=500, detail=f"Internal server error: {str(e)}")


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
