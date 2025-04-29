# Directory: project/app/main.py
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from . import crud, schemas, models, database, mcp

app = FastAPI(title="Travel Itinerary API")

# Dependency
def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def read_root():
    return {"message": "Welcome to the Travel Itinerary API!"}

@app.post("/itineraries/", response_model=schemas.Itinerary)
def create_itinerary(itinerary: schemas.ItineraryCreate, db: Session = Depends(get_db)):
    return crud.create_itinerary(db, itinerary)

@app.get("/itineraries/", response_model=list[schemas.Itinerary])
def read_itineraries(db: Session = Depends(get_db)):
    return crud.get_itineraries(db)

@app.get("/recommendations/{nights}", response_model=list[schemas.Itinerary])
def get_recommendations(nights: int):
    return mcp.get_recommendations(nights)