
from sqlalchemy import create_engine, Column, Integer, String, Float, DateTime
from sqlalchemy.orm import sessionmaker, DeclarativeBase


DATABASE_URL = "sqlite:///weather.db"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)


class Base(DeclarativeBase):
    pass


class WeatherData(Base):
    __tablename__ = "weather_data"

    id = Column(Integer, primary_key=True, index=True)
    city = Column(String, index=True)
    current_temperature = Column(Float)
    max_temperature = Column(Float)
    min_temperature = Column(Float)
    timestamp = Column(DateTime)


def init_db():
    Base.metadata.create_all(bind=engine)
