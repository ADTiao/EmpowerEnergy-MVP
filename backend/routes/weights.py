from fastapi import APIRouter
from pydantic import BaseModel
from typing import Union
from backend.info import info as final
from fastapi.responses import JSONResponse
from fastapi import Request

router = APIRouter()

@router.post("/weights")
async def process_weights(request: Request):
    part = "weights"
    weights = await request.json()
    final[part] = weights
    return JSONResponse(content="weights processed", status_code=200)