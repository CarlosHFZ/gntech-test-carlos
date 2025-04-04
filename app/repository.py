from app.database import SessionLocal, WeatherData


def save_weather_data(data: dict):
    session = SessionLocal()

    try:
        weather = WeatherData(
            city=data['city'],
            current_temperature=data["current_temperature"],
            max_temperature=data["max_temperature"],
            min_temperature=data["min_temperature"],
            timestamp=data["timestamp"]
        )

        session.add(weather)
        session.commit()
        print(f'Saved data for the city: {data['city']}')

    except Exception as e:
        session.rollback()
        raise e

    finally:
        session.close()
