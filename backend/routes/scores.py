from fastapi import APIRouter
from backend.services.analyze import analyze

router = APIRouter()

@router.get("/analyze")
def provide_scores():
    return (analyze())