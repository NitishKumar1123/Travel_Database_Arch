# Directory: project/app/models.py
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from .database import Base

class Itinerary(Base):
    __tablename__ = 'itineraries'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False, index=True, unique=True)
    days = relationship("ItineraryDay", back_populates="itinerary", cascade="all, delete")

class ItineraryDay(Base):
    __tablename__ = 'itinerary_days'

    id = Column(Integer, primary_key=True, index=True)
    day_number = Column(Integer, nullable=False)
    itinerary_id = Column(Integer, ForeignKey("itineraries.id"), nullable=False)

    itinerary = relationship("Itinerary", back_populates="days")
    hotel = relationship("HotelStay", back_populates="day", uselist=False, cascade="all, delete")
    transfers = relationship("Transfer", back_populates="day", cascade="all, delete")
    activities = relationship("Activity", back_populates="day", cascade="all, delete")

class HotelStay(Base):
    __tablename__ = 'hotel_stays'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    location = Column(String, nullable=False)
    day_id = Column(Integer, ForeignKey("itinerary_days.id"), nullable=False)

    day = relationship("ItineraryDay", back_populates="hotel")

class Transfer(Base):
    __tablename__ = 'transfers'

    id = Column(Integer, primary_key=True, index=True)
    from_location = Column(String, nullable=False)
    to_location = Column(String, nullable=False)
    mode = Column(String, nullable=False)
    day_id = Column(Integer, ForeignKey("itinerary_days.id"), nullable=False)

    day = relationship("ItineraryDay", back_populates="transfers")

class Activity(Base):
    __tablename__ = 'activities'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    description = Column(String, nullable=False)
    day_id = Column(Integer, ForeignKey("itinerary_days.id"), nullable=False)

    day = relationship("ItineraryDay", back_populates="activities")