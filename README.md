GNTech Test - Carlos

API RESTful de Clima com FastAPI, PostgreSQL e Docker
🌤️ GNTech Weather Data API

Este projeto é uma API RESTful desenvolvida com FastAPI para consultar dados climáticos da OpenWeather API, armazenar essas informações em um banco de dados PostgreSQL e disponibilizá-las por meio de endpoints. Todo o ambiente é orquestrado via Docker e Docker Compose e com boa praticas de programação.
🔧 Tecnologias Utilizadas

    🐍 Python 3.10

    ⚡ FastAPI

    🐘 PostgreSQL

    🐳 Docker & Docker Compose

    🌐 OpenWeather API

🚀 Como Executar o Projeto Localmente
1. Clone o repositório

git clone https://github.com/seu-usuario/gntech-test-carlos.git
cd gntech-test-carlos

2. Configure as variáveis de ambiente

Crie um arquivo .env na raiz do projeto com o seguinte conteúdo (exemplo disponível em .env.example):

POSTGRES_USER=carlos
POSTGRES_PASSWORD=carlos123
POSTGRES_DB=weather_db

# Você pode obter sua chave da OpenWeather gratuitamente em: https://openweathermap.org/api
OPENWEATHER_API_KEY=your_api_key_here

# URL de conexão com o banco
DATABASE_URL=postgresql://carlos:carlos123@db:5432/weather_db


3. Construa o ambiente virutal e inicie os containers Docker( comandos depende do sitema )

python -m venv venv
source venv/bin/activate ou .\venv\Scripts\Activate

pip install -r requirements.txt

docker-compose up --build

🧪 Como Utilizar a API
📘 Documentação Interativa (FastAPI)

Após iniciar o projeto, acesse:

    http://localhost:8000/docs — Interface Swagger da API


🔁 Endpoints Disponíveis
GET /weather - Retorna todos os dados climáticos salvos no banco de dados.


POST /weather?city=NomeDaCidade - Puxa os dados climáticos da cidade informada na OpenWeather API,
armazena no banco de dados e retorna mensagem de sucesso, podendo visualizada em GET /weather.



📌 Exemplo de requisição via Postman:

    POST http://localhost:8000/weather?city=London
    GET http://localhost:8000/weather

🖥️ Executar Script Diretamente
Você também pode rodar o script main.py diretamente dentro do container,
Colocando o nome da cidade via input, após, e vai retornar todas as requisições realizadas

# Acessar o container da API (Docker)
docker exec -it gntech-api bash

python main.py






Desenvolvido por Carlos — Teste técnico GNTech 2025

