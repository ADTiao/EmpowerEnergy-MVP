from fastapi import APIRouter
from fastapi.responses import JSONResponse
from backend.services.analyze import analyze
from backend.info import info as final

router = APIRouter()

@router.get("/analyze")
def provide_scores():
    result = analyze(final)
    # suppose analyze() returns {"impact":…, "feed":…}
    return JSONResponse(content=result)