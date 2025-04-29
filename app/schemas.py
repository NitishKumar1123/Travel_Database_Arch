from typing import List, Optional
from pydantic import BaseModel, Field, ConfigDict

class HotelStayBase(BaseModel):
    name: str = Field(..., json_schema_extra={"example": "Ananta Villa Krabi"})
    location: str = Field(..., json_schema_extra={"example": "Ao Nang, Krabi"})

class TransferBase(BaseModel):
    from_location: str = Field(..., json_schema_extra={"example": "Krabi Airport"})
    to_location: str = Field(..., json_schema_extra={"example": "Hotel"})
    mode: str = Field(..., json_schema_extra={"example": "Private Taxi"})

class ActivityBase(BaseModel):
    name: str = Field(..., json_schema_extra={"example": "4-Island Tour"})
    description: str = Field(..., json_schema_extra={"example": "Snorkeling and beach visit to Chicken Island, Poda Island, etc."})

class ItineraryDayBase(BaseModel):
    day_number: int = Field(..., json_schema_extra={"example": 1})
    hotel: Optional[HotelStayBase]
    transfers: List[TransferBase] = []
    activities: List[ActivityBase] = []

class ItineraryBase(BaseModel):
    name: str = Field(..., json_schema_extra={"example": "Nitish's Krabi Getaway"})
    days: List[ItineraryDayBase]

class ItineraryCreate(ItineraryBase):
    pass

class Itinerary(ItineraryBase):
    id: int

    model_config = ConfigDict(from_attributes=True)
