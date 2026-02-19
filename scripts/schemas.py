from pydantic import BaseModel, Field, field_validator
from typing import Optional

class TaxiRideInput(BaseModel):
    # Uso de Field como en el ejemplo del Profe
    vendor_id: int = Field(..., ge=1, le=2, description="1=Creative, 2=VeriFone")
    passenger_count: int = Field(..., ge=1, le=6)
    pickup_latitude: float = Field(..., ge=40.5, le=41.0)
    pickup_longitude: float = Field(..., ge=-74.1, le=-73.7)
    trip_duration: float = Field(..., ge=60, le=7200, description="Segundos")

    # Decorador @field_validator (Pydantic V2) para integridad GPS
    @field_validator('pickup_latitude')
    @classmethod
    def corroborar_ubicacion(cls, v: float) -> float:
        if v == 0:
            raise ValueError("Error de sensor: La latitud no puede ser cero.")
        return v
