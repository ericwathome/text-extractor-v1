from marvin import ai_model
from pydantic import BaseModel, Field

@ai_model
class IdentityCard(BaseModel):
    country: str
    serialNumber: str
    idNumber: str
    name: str
    dateOfBirth: str
    gender: str
    placeOfIssue: str
    districtOfBirth: str
    dateOfIssue: str