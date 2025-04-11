
# 🌤️ GNTech Weather Data API

A RESTful API built with FastAPI, PostgreSQL, and Docker to fetch and store weather data from the OpenWeather API.

---

## 🔧 Technologies Used

- 🐍 Python 3.11
- ⚡ FastAPI
- 🐘 PostgreSQL
- 🐳 Docker & Docker Compose
- 🌐 OpenWeather API

---

## 🚀 How to Run the Project Locally

### 1. Clone the repository

```bash
git clone https://github.com/your-username/gntech-test-carlos.git
cd gntech-test-carlos
```

### 2. Configure environment variables

Create a `.env` file in the root directory (an example is available in `.env.example`):

```env
POSTGRES_USER=carlos
POSTGRES_PASSWORD=carlos123
POSTGRES_DB=weather_db
OPENWEATHER_API_KEY=your_api_key_here
DATABASE_URL=postgresql://carlos:carlos123@db:5432/weather_db
```

> You can get your free OpenWeather API key at: https://openweathermap.org/api

### 3. Run the application with Docker

```bash
docker-compose up --build
```

---

## 🧪 Using the API

### 📘 Interactive Documentation (Swagger UI)

After the project is running, visit:

[http://localhost:8000/docs](http://localhost:8000/docs)

---

## 🔁 Available Endpoints

- `GET /weather`  
  Returns all weather data stored in the database.

- `POST /weather?city=CityName`  
  Fetches weather data for the specified city from OpenWeather, stores it in the database, and returns a success message.

### 📌 Example with Postman:

```http
POST http://localhost:8000/weather?city=London
GET  http://localhost:8000/weather
```

---

## 🖥️ Running main.py directly inside the container

You can also run the `main.py` script manually to insert a city and fetch its weather data:

### Access the API container:

```bash
docker exec -it gntech-api bash
```

### Then run:

```bash
python main.py
```

---

## 👨‍💻 Developed by Carlos  
Technical Test — GNTech 2025