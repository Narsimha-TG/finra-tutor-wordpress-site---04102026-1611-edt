from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Optional

app = FastAPI(title="FINRA Tutor API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

class ThemeSettings(BaseModel):
    theme_mode: str = "light"
    user_id: Optional[int] = None

class SEOMetadata(BaseModel):
    page_id: int
    seo_keywords: list[str]
    last_updated: str

# In-memory seed data
db = {
    "theme": {"theme_mode": "light", "user_id": 1},
    "seo": {"page_id": 1, "seo_keywords": ["FINRA", "Tutor", "Exam Prep"], "last_updated": "2026-04-10"}
}

@app.get("/wp-json/finra/v1/theme-settings")
def get_theme():
    return db["theme"]

@app.post("/wp-json/finra/v1/toggle-theme")
def toggle_theme(settings: ThemeSettings):
    db["theme"]["theme_mode"] = settings.theme_mode
    return {"status": "success", "new_mode": db["theme"]["theme_mode"]}

@app.get("/wp-json/finra/v1/seo-metadata")
def get_seo():
    return db["seo"]