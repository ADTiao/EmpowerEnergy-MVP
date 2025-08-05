from fastapi import APIRouter
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from typing import Union
router = APIRouter()
from backend.info import info as final

class Criteria(BaseModel):
    category : str
    metric : str
    val : Union[str, int, list, bool, float]

@router.post("/criteria")
def receive_criteria(data : Criteria):
    part = "criteria"
    category = data.category
    name = data.metric
    crit = data.val
    final.setdefault(part, {}).setdefault(category, {})[name] = crit    # once done send confirmation back to frontend
    return JSONResponse("information registered!")


