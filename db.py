import os

from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()


class Noise(Base):
    __tablename__ = "noises"
    id = Column(String, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String)
    max_volume = Column(Float)
    step = Column(Float)


class Video(Base):
    __tablename__ = "videos"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String)
    video_id = Column(String)


# Ensure the POSTGRES_URL is correctly formatted
# Example: postgresql+psycopg2://username:password@hostname:port/database
engine = create_engine(os.getenv('POSTGRES_URL'))
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


Base.metadata.create_all(bind=engine)
