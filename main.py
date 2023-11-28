from typing import Union

from fastapi import FastAPI
import marvin
import json
from model.IdentityCard import IdentityCard
from model.Logbook import Logbook
from dto.TextDto import TextDto

app = FastAPI()

marvin.settings.openai.api_key = ''

@app.post("/identity_card_json")
async def extract_id_json(text: TextDto) -> IdentityCard:
    id = IdentityCard(text)
    return json.loads(id.model_dump_json())


@app.post("/logbook_card_json")
async def extract_logbook_json(text: TextDto) -> Logbook:
    logbook = Logbook(text)
    return json.loads(logbook.model_dump_json())