# main.py

from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

# Veri modeli (hikaye yapısı)
class Story(BaseModel):
    mode: str
    problem: str
    advice: str
    anon_name: Optional[str] = None

# Ana sayfa - basit test
@app.get("/")
def read_root():
    return {"message": "HLSS backend is working!"}

# Hikaye alma endpointi
@app.post("/intake")
def intake_story(story: Story):
    return {"message": "Story received", "data": story}
