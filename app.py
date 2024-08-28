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

    return templates.TemplateResponse("index.html.jinja2", {"request": request, "noises": noises})
