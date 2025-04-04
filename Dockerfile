FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["py", "-m", "uvicorn", "run_api:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]

RUN pip show uvicorn && which uvicorn

