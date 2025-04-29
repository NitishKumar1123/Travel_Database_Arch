# Directory: project/app/crud.py
from sqlalchemy.orm import Session
from . import models, schemas

def create_itinerary(db: Session, itinerary: schemas.ItineraryCreate):
    db_itinerary = models.Itinerary(name=itinerary.name)
    db.add(db_itinerary)
    db.commit()
    db.refresh(db_itinerary)

    for day in itinerary.days:
        db_day = models.ItineraryDay(day_number=day.day_number, itinerary_id=db_itinerary.id)
        db.add(db_day)
        db.commit()
        db.refresh(db_day)

        if day.hotel:
            db_hotel = models.HotelStay(**day.hotel.dict(), day_id=db_day.id)
            db.add(db_hotel)

        for transfer in day.transfers:
            db_transfer = models.Transfer(**transfer.dict(), day_id=db_day.id)
            db.add(db_transfer)

        for activity in day.activities:
            db_activity = models.Activity(**activity.dict(), day_id=db_day.id)
            db.add(db_activity)

    db.commit()
    return db_itinerary

def get_itineraries(db: Session):
    return db.query(models.Itinerary).all()
