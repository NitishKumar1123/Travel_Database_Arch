# Directory: project/app/mcp.py
from .database import SessionLocal
from .models import Itinerary

def get_recommendations(nights: int):
    db = SessionLocal()
    try:
        results = db.query(Itinerary).all()
        matching = [i for i in results if len(i.days) == nights]
        return matching
    finally:
        db.close()