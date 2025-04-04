# GNTech Test - Carlos

Projeto FastAPI + PostgreSQL + Docker que consome uma API pública de clima e armazena os dados no banco.

---

# GNTech - Weather Data API ☁️

Este projeto é uma API RESTful desenvolvida com FastAPI, que extrai dados climáticos da OpenWeather API, armazena em um banco PostgreSQL e os disponibiliza via endpoints. O ambiente completo é conteinerizado com Docker.

## 🔧 Tecnologias utilizadas

- 🐍 Python 3.10
- ⚡ FastAPI
- 🐘 PostgreSQL
- 🐳 Docker & Docker Compose
- 🌐 OpenWeather API

---

## 🚀 Como executar o projeto localmente

### 1. Clone o repositório

```bash
git clone https://github.com/seu-usuario/gntech-test-carlos.git
cd gntech-test-carlos
```
Crie um arquivo .env com as seguintes variáveis(está em .env.exemple tambem):
POSTGRES_USER=carlos
POSTGRES_PASSWORD=carlos123
POSTGRES_DB=weather_db
OPENWEATHER_API_KEY=your_api_key_here
                        #//user:password@gntech_postgres:port/my_db
DATABASE_URL=postgresql://carlos:carlos123@gntech_postgres:5432/weather_db

🔑 Você pode obter a OPENWEATHER_API_KEY gratuitamente em https://openweathermap.org/api


3. Suba os containers com Docker
docker-compose up --build
A API estará disponível em: http://localhost:8000

---- FastAPI ------

http://localhost:8000/docs - para usar o FastAPI
/weather "GET" - para puxar os dados salvos no banco de dados
/weather "POST" - voce coloca apenas o nome da cidade que deseja armazenar os dados

---- Postman ------
http://localhost:8000/weather "Get" - para puxar os dados salvos no banco de dados
http://localhost:8000/weather?city=London "POST" - voce coloca apos '=' apenas o nome da cidade que deseja armazenar os dados

---- Rodar o Main.py ----
Dentro do terminal do Docker:

python main.py Biguaçu
docker exec -it gntech-api bash


