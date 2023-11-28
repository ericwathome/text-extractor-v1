from pydantic import BaseModel, Field

class TextDto(BaseModel):
    text: str