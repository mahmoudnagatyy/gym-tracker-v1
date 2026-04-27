from fastapi import FastAPI, Depends, HTTPException
from fastapi.responses import FileResponse, HTMLResponse
from fastapi.staticfiles import StaticFiles
from sqlalchemy.orm import Session
from typing import List
import os

from database import engine, SessionLocal, init_db, SessionDB, SetDB
from models import SessionCreate, SessionModel
from export_service import generate_xlsx, XLSX_FILENAME

app = FastAPI(title="Gym Tracker API")

# Initialize DB
init_db()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/sessions", response_model=SessionModel)
def create_session(session: SessionCreate, db: Session = Depends(get_db)):
    db_session = SessionDB(
        date=session.date,
        time=session.time,
        session_type=session.session_type,
        bodyweight=session.bodyweight,
        total_volume=session.total_volume,
        total_sets=session.total_sets,
        duration=session.duration
    )
    db.add(db_session)
    db.commit()
    db.refresh(db_session)
    
    for s in session.sets:
        db_set = SetDB(
            session_id=db_session.id,
            exercise_name=s.exercise_name,
            set_num=s.set_num,
            weight_kg=s.weight_kg,
            reps=s.reps,
            volume=s.volume
        )
        db.add(db_set)
    db.commit()
    db.refresh(db_session)
    
    # Auto-generate XLSX on save
    generate_xlsx(db)
    
    return db_session

@app.get("/sessions", response_model=List[SessionModel])
def read_sessions(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    sessions = db.query(SessionDB).order_by(SessionDB.id.desc()).offset(skip).limit(limit).all()
    return sessions

@app.get("/sessions/{session_id}", response_model=SessionModel)
def read_session(session_id: int, db: Session = Depends(get_db)):
    session = db.query(SessionDB).filter(SessionDB.id == session_id).first()
    if session is None:
        raise HTTPException(status_code=404, detail="Session not found")
    return session

@app.get("/export/xlsx")
def export_xlsx(db: Session = Depends(get_db)):
    filepath = generate_xlsx(db)
    if not os.path.exists(filepath):
        raise HTTPException(status_code=404, detail="XLSX file not generated")
    return FileResponse(filepath, media_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet', filename="mahmoud_gym_tracker.xlsx")

@app.get("/", response_class=HTMLResponse)
def read_root():
    with open("index.html", "r") as f:
        return f.read()
