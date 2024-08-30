from fastapi import FastAPI
from fastapi.params import Depends
from fastapi.requests import Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from db import SessionLocal, get_db

app = FastAPI()

templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request, db: SessionLocal = Depends(get_db)):
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
