from fastapi import FastAPI
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from fastapi.requests import Request
from pymongo import MongoClient

app = FastAPI()

templates = Jinja2Templates(directory="templates")


def get_database():
    """Connect to the MongoDB database and return the collection."""
    client = MongoClient("mongodb://mongo/rapidPrototype")
    return client['data_collection']


@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    collection = get_database()

    noises = [
        {"id": "white", "title": "White Noise", "description": "Consistent, balanced sound across all frequencies, ideal for blocking distractions", "max_volume": 1, "step": 0.01},
        {"id": "pink", "title": "Pink Noise", "description": "More natural, soothing frequency distribution, often used to improve focus", "max_volume": 1, "step": 0.01},
        {"id": "brown", "title": "Brown Noise", "description": "Deeper, bass-heavy sound, great for reducing stress and maintaining concentration", "max_volume": 1, "step": 0.01}
    ]

    videos = [
        {"title": "Rain Sounds", "description": "Gentle rain sounds to help you relax and sleep better", "id": "BSmYxnvUDHw"},
        {"title": "Ocean Waves", "description": "Calming ocean waves for stress relief and meditation", "id": "Nep1qytq9JM"},
        {"title": "Forest Ambience", "description": "Soothing forest sounds to create a peaceful environment", "id": "xNN7iTA57jM"},
        {"title": "Star Trek Engine", "description": "Deep humming", "id": "ZPoqNeR3_UA"}
    ]

    return templates.TemplateResponse("index.html.jinja2", {"request": request, "noises": noises, "videos": videos})
