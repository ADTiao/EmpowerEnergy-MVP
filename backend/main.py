from fastapi import FastAPI, responses
from backend.routes import criteria
from backend.routes import upload
from backend.routes import weights
from backend.routes import scores

gate = FastAPI()

gate.include_router(criteria.router)
gate.include_router(upload.router)
gate.include_router(weights.router)
gate.include_router(scores.router)

@gate.get("/")
def health_check():
    return {"status": "API is running"}
