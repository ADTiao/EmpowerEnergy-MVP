from fastapi import APIRouter
from backend.services.analyze import analyze
from backend.info import info as final

router = APIRouter()

@router.get("/analyze")
def provide_scores():
    output = analyze(final)
    return (output)