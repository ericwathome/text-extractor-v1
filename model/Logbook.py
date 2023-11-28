from marvin import ai_model
from pydantic import BaseModel, Field

@ai_model
class Logbook(BaseModel):
    registration: str
    chassis_frame: str
    make: str
    model: str
    type: str
    body: str
    fuel: str
    manYear: int
    rating: int
    engineNo: str
    color: str
    regDate: str
    grossWeight: float
    duty: str
    noOfPreviousOwners: int
    passengers: int
    tareWeight: float
    taxClass: str
    axies: int
    loadCapacity: int
    previousReg: str
    country: str
    previousRegistration: str
    pin: str
    name: str
    boxNo: str
    code: str
    town: str
