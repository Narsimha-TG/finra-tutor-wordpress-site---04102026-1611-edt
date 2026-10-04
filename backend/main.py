from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

app = FastAPI(title="FINRA Tutor API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

class TutorProfile(BaseModel):
    id: int
    tutor_name: str
    subject_expertise: List[str]
    hourly_rate: float
    availability_status: str
    created_at: str

class BookingRequest(BaseModel):
    tutor_id: int
    student_name: str
    session_date: str

# Seed Data
tutors = [
    {"id": 1, "tutor_name": "Jane Doe", "subject_expertise": ["SIE", "Series 7"], "hourly_rate": 150.0, "availability_status": "available", "created_at": "2026-04-10T10:00:00Z"}
]

@app.get("/wp-json/finra/v1/tutor-profiles", response_model=List[TutorProfile])
async def get_tutors():
    return tutors

@app.post("/wp-json/finra/v1/booking")
async def create_booking(booking: BookingRequest):
    return {"status": "success", "message": f"Booking confirmed for {booking.student_name}"}

@app.get("/wp-json/finra/v1/seo-metadata")
async def get_seo():
    return {"title": "FINRA Exam Prep", "description": "Expert tutoring for SIE, Series 7, and 63 exams."}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)