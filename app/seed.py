# Directory: project/app/seed.py
from app.database import SessionLocal, engine
from app import models
from app.crud import create_itinerary
from app.schemas import ItineraryCreate, ItineraryDayBase, HotelStayBase, TransferBase, ActivityBase

models.Base.metadata.create_all(bind=engine)

def seed():
    db = SessionLocal()

    itineraries = [
        ItineraryCreate(
            name="Phuket 2-Night Getaway",
            days=[
                ItineraryDayBase(day_number=1,
                    hotel=HotelStayBase(name="Sea View Hotel", location="Patong"),
                    transfers=[TransferBase(from_location="Airport", to_location="Hotel", mode="Taxi")],
                    activities=[ActivityBase(name="Beach Relax", description="Relax on Patong Beach")]),
                ItineraryDayBase(day_number=2,
                    hotel=HotelStayBase(name="Sea View Hotel", location="Patong"),
                    activities=[ActivityBase(name="City Tour", description="Explore Phuket Town")])
            ]
        ),
        ItineraryCreate(
            name="Krabi 3-Night Escape",
            days=[
                ItineraryDayBase(day_number=1,
                    hotel=HotelStayBase(name="Krabi Resort", location="Ao Nang"),
                    transfers=[TransferBase(from_location="Airport", to_location="Hotel", mode="Van")],
                    activities=[ActivityBase(name="Beach Walk", description="Relax at Ao Nang beach.")]),
                ItineraryDayBase(day_number=2,
                    hotel=HotelStayBase(name="Krabi Resort", location="Ao Nang"),
                    activities=[ActivityBase(name="Island Hopping", description="Phi Phi tour.")]),
                ItineraryDayBase(day_number=3,
                    hotel=HotelStayBase(name="Krabi Resort", location="Ao Nang"),
                    transfers=[TransferBase(from_location="Hotel", to_location="Airport", mode="Van")],
                    activities=[])
            ]
        )
    ]

    for itinerary in itineraries:
        create_itinerary(db, itinerary)

    db.close()

if __name__ == '__main__':
    seed()