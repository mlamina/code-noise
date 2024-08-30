from fastapi import FastAPI
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from fastapi.requests import Request
from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

app = FastAPI()

templates = Jinja2Templates(directory="templates")

DATABASE_URL = "postgresql+psycopg2://user:password@postgresserver/db"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
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

Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request, db: SessionLocal = Depends(get_db)):
    noises = db.query(Noise).all()
    videos = db.query(Video).all()

    return templates.TemplateResponse("index.html.jinja2", {"request": request, "noises": noises, "videos": videos})
