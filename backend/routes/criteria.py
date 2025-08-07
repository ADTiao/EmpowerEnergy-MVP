from fastapi import APIRouter, Request
from fastapi.responses import JSONResponse
router = APIRouter()
from backend.info import info as final

@router.post("/criteria")
async def receive_criteria(request: Request):
    part = "criteria"
    criteria = await request.json()
    final[part] = criteria
    return JSONResponse("information registered!")


