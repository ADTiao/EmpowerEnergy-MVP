from fastapi import APIRouter
from pydantic import BaseModel
from typing import Union
from backend.info import info as final

router = APIRouter()

class info(BaseModel):
    category : str
    metric : str
    weight : Union[float, int]

@router.post("/weights")
def process_weights(data : info):
    part = "weights"
    category = data.category
    name = data.metric
    weight = data.weight
    final.setdefault(part, {}).setdefault(category, {})[name] = weight