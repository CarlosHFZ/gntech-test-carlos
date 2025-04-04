from app.services import fetch_and_save_weather_data


def main():
    city = 'Biguaçu'
    fetch_and_save_weather_data(city)


if __name__ == "__main__":
    main()
